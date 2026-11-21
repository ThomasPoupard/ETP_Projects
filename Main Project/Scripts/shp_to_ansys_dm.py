
"""
Convert an ESRI Shapefile (EPSG:2056) into an
ANSYS DesignModeler JavaScript Run Script.

The shapefile and its companion files (.shx, .dbf, .prj)
must be located in the same folder.
"""

from pathlib import Path
import math
import re

import shapefile
from pyproj import CRS


# ============================================================
# USER SETTINGS
# ============================================================

# Folder containing the shapefile.
INPUT_FOLDER = Path(__file__).parent / 'QGIS' / 'aar_banks'

# Name of the input shapefile (without .shp).
SHAPEFILE_NAME = "aar"

# Output JavaScript filename.
OUTPUT_NAME = "aar_banks.js"

# DesignModeler units: "mm" or "m".
UNITS = "m"

# Origin:
# "min" = automatically subtract minimum X and Y.
# Or specify coordinates in metres, e.g. (2600000, 1200000).
ORIGIN = "min"

# Name of the sketch in ANSYS DesignModeler.
SKETCH_NAME = "Aar"


# ============================================================
# CONVERSION FUNCTIONS
# ============================================================

def safe_js_name(name):
    """Return a valid JavaScript identifier."""
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", name)

    if not cleaned:
        cleaned = "ImportedGeometry"

    if cleaned[0].isdigit():
        cleaned = "_" + cleaned

    return cleaned


def validate_files(shp_path):
    """Check that all required shapefile files exist."""

    for extension in [".shp", ".shx", ".dbf", ".prj"]:
        path = shp_path.with_suffix(extension)

        if not path.exists():
            path = shp_path.with_suffix(extension.upper())

        if not path.exists():
            raise FileNotFoundError(
                f"Missing shapefile component: {path.name}"
            )


def validate_crs(shp_path):
    """Check that the shapefile uses EPSG:2056."""

    prj_path = shp_path.with_suffix(".prj")

    if not prj_path.exists():
        prj_path = shp_path.with_suffix(".PRJ")

    crs = CRS.from_wkt(
        prj_path.read_text(encoding="utf-8")
    )

    if not crs.equals(CRS.from_epsg(2056)):
        raise ValueError(
            f"Expected EPSG:2056, found: {crs.to_string()}"
        )


def extract_line_parts(reader):
    """Extract all independent polyline parts."""

    supported = {
        shapefile.POLYLINE,
        getattr(shapefile, "POLYLINEZ", -999),
        getattr(shapefile, "POLYLINEM", -999),
    }

    if reader.shapeType not in supported:
        raise ValueError(
            f"Expected polyline geometry. "
            f"Found shape type: {reader.shapeType}"
        )

    all_parts = []

    for shape in reader.iterShapes():

        points = shape.points

        if not points:
            continue

        starts = list(shape.parts) + [len(points)]

        for i in range(len(starts) - 1):

            start = starts[i]
            end = starts[i + 1]

            part = []

            for point in points[start:end]:

                x = float(point[0])
                y = float(point[1])

                if not (math.isfinite(x) and math.isfinite(y)):
                    raise ValueError("Invalid coordinate found.")

                # Remove consecutive duplicate vertices.
                if not part or (x != part[-1][0] or y != part[-1][1]):
                    part.append((x, y))

            if len(part) >= 2:
                all_parts.append(part)

    if not all_parts:
        raise ValueError("No usable polyline parts found.")

    return all_parts


def format_number(value):
    """Format coordinates without unnecessary decimal places."""

    if abs(value) < 0.0000005:
        value = 0.0

    return f"{value:.6f}".rstrip("0").rstrip(".") if value != 0 else "0"


def build_ansys_script(parts, sketch_name, units, origin):

    scale = 1000.0 if units == "mm" else 1.0
    safe_name = safe_js_name(sketch_name)

    lines = [
        "// Generated from ESRI Shapefile (EPSG:2056)",
        f"// Units: {units}",
        "",
        "var XYPlane = agb.GetXYPlane();",
        "agb.SetActivePlane(XYPlane);",
        "",
        f"var {safe_name} = XYPlane.newSketch();",
        f'{safe_name}.Name = "{sketch_name.replace(chr(34), chr(39))}";',
        "",
    ]

    total_vertices = sum(len(part) for part in parts)

    for index, part in enumerate(parts, start=1):

        spline_name = f"S{index}"

        lines.extend([
            f"// Line part {index}: {len(part)} fit points",
            f"var {spline_name} = {safe_name}.SplineBegin();",
            f"with ({spline_name})",
            "{",
            "    SplineFlexibility = agc.No;",
        ])

        for x, y in part:

            local_x = (x - origin[0]) * scale
            local_y = (y - origin[1]) * scale

            lines.append(
                f"    SplineXY({format_number(local_x)}, "
                f"{format_number(local_y)});"
            )

        lines.extend([
            "    SplineFitPtEnd();",
            "}",
            "",
        ])

    # Fix all splines.
    lines.append("// Fix all splines.")

    for index in range(1, len(parts) + 1):
        lines.append(f"XYPlane.FixedCon(S{index}, 1);")

    lines.extend([
        "",
        "XYPlane.EvalDimCons();",
        "agb.Regen();",
        "",
        f"// Summary: {len(parts)} splines, "
        f"{total_vertices} vertices.",
    ])

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n======================================")
    print(" SHAPEFILE TO ANSYS DESIGNMODELER")
    print("======================================\n")

    shp_path = INPUT_FOLDER / f"{SHAPEFILE_NAME}.shp"
    output_path = INPUT_FOLDER / OUTPUT_NAME

    # Check input files.
    validate_files(shp_path)

    # Check coordinate reference system.
    validate_crs(shp_path)

    print("Reading shapefile...")

    reader = shapefile.Reader(str(shp_path), encoding="utf-8")

    try:
        parts = extract_line_parts(reader)
    finally:
        reader.close()

    # Collect all coordinates.
    all_x = [x for part in parts for x, y in part]
    all_y = [y for part in parts for x, y in part]

    # Determine origin.
    if ORIGIN == "min":
        origin = (min(all_x), min(all_y))
        origin_description = "Minimum X/Y"
    else:
        origin = ORIGIN
        origin_description = "User-defined"

    # Generate ANSYS script.
    if UNITS not in ("mm", "m"):
        raise ValueError("UNITS must be either 'mm' or 'm'.")

    js = build_ansys_script(
        parts,
        SKETCH_NAME,
        UNITS,
        origin
    )

    output_path.write_text(js, encoding="utf-8")

    # Calculate geometry extent.
    scale = 1000.0 if UNITS == "mm" else 1.0

    width = (max(all_x) - min(all_x)) * scale
    height = (max(all_y) - min(all_y)) * scale

    total_vertices = sum(len(part) for part in parts)

    # Print summary.
    print("\nConversion completed successfully!")
    print("--------------------------------------")
    print(f"Input:       {shp_path.name}")
    print(f"Output:      {output_path.name}")
    print(f"CRS:         EPSG:2056")
    print(f"Line parts:  {len(parts)}")
    print(f"Vertices:    {total_vertices}")
    print(f"Units:       {UNITS}")
    print(f"Origin:      {origin[0]:.3f}, {origin[1]:.3f} m")
    print(f"Origin type: {origin_description}")
    print(f"Extent:      {width:.3f} x {height:.3f} {UNITS}")
    print("--------------------------------------")

    print("\nOpen ANSYS DesignModeler and run:")
    print(output_path)


if __name__ == "__main__":
    main()
