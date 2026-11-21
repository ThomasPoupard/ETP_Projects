from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsField
)
from qgis.PyQt.QtCore import QVariant

# --------------------------------------------------
# 1. Retrieve input layers
# --------------------------------------------------

project = QgsProject.instance()

temp_layer = project.mapLayersByName("Temperaturmessnetz")[0]
lhg_layer = project.mapLayersByName("lhg_UBST")[0]

# --------------------------------------------------
# 2. Define coordinate reference systems
# --------------------------------------------------

# LV95 (CH1903+)
crs_lv95 = QgsCoordinateReferenceSystem("EPSG:2056")

# Transform both layers to LV95
transform_temp = QgsCoordinateTransform(
    temp_layer.crs(),
    crs_lv95,
    project
)

transform_lhg = QgsCoordinateTransform(
    lhg_layer.crs(),
    crs_lv95,
    project
)

# --------------------------------------------------
# 3. Filter lhg_UBST
# --------------------------------------------------

lhg_features = []

for feature in lhg_layer.getFeatures():

    if feature["lhg_code"] == "lhg_fluss":

        geom = QgsGeometry(feature.geometry())

        geom.transform(transform_lhg)

        lhg_features.append(geom)

print(f"Filtered LHG features: {len(lhg_features)}")

# --------------------------------------------------
# 4. Create output layer
# --------------------------------------------------

output_layer = QgsVectorLayer(
    "Point?crs=EPSG:2056",
    "Temperaturmessnetz_LHG_Matches",
    "memory"
)

provider = output_layer.dataProvider()

# Add attributes from Temperaturmessnetz
provider.addAttributes([
    QgsField("NR", QVariant.String),
    QgsField("Name", QVariant.String)
])

output_layer.updateFields()

# --------------------------------------------------
# 5. Find matching points (< 10 metres)
# --------------------------------------------------

tolerance = 10.0

new_features = []

for temp_feature in temp_layer.getFeatures():

    temp_geom = QgsGeometry(temp_feature.geometry())
    temp_geom.transform(transform_temp)

    for lhg_geom in lhg_features:

        distance = temp_geom.distance(lhg_geom)

        if distance < tolerance:

            new_feature = QgsFeature(output_layer.fields())

            new_feature.setGeometry(temp_geom)

            new_feature.setAttributes([
                temp_feature["NR"],
                temp_feature["Name"]
            ])

            new_features.append(new_feature)

            # Stop after the first match
            break

# Add features to output layer
provider.addFeatures(new_features)
output_layer.updateExtents()

# --------------------------------------------------
# 6. Add output layer to QGIS project
# --------------------------------------------------

project.addMapLayer(output_layer)

print(f"Created {len(new_features)} matching points.")
print("Output layer added to QGIS project.")
