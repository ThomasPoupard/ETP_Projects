import pandas as pd
from importlib import Path

input_file_path = Path(__file__).parent / 'Data' / 'swissprtr-daten-2007-2024.xlsx'
output_file_path = Path(__file__).parent / 'QGIS' / 'polluting_facilities.csv'

pollutants_to_keep = [
    "Chloride (als Gesamt-Cl)",
    "Fluoride (als Gesamt-F)",
    "Gesamtphosphor",
]

df = pd.read_excel(input_file_path, sheet_name=0, header=0, skiprows=[1, 2, 3])

filtered_df = df[
    (df["Source type"] == "Punktquelle") &
    (df["Medium"] == "Wasser") &
    (df["Year"] == 2024) &
    (df["Pollutant_name"].isin(pollutants_to_keep))
]

# Group by facility and combine pollutant names
facility_columns = [
    "Year",
    "Facility",
    "Facility ID",
    "North coordinate (CH1903+)",
    "East coordinate (CH1903+)"
]

pollutants_df = (
    filtered_df.groupby(facility_columns)["Pollutant_name"]
    .apply(lambda x: "/".join(sorted(x.dropna().unique())))
    .reset_index(name="Pollutants")
)

pollutants_df.to_csv(output_file_path, index=False, encoding="utf-8")

print(f"Number of facilities extracted: {len(pollutants_df)}")
print(f"Output saved to: {output_file_path}")
