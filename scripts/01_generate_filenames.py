import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "csv" / "02. Audio Dialogue Database.xlsx"

df = pd.read_excel(EXCEL_PATH)
df.columns = df.columns.str.strip()

def clean(value):
    return str(value).strip()

def format_id(value):
    return str(int(float(value))).zfill(3)

def short_line_type(value):
    value = clean(value)
    if value.lower().startswith("q"):
        return "Q"
    if value.lower().startswith("r"):
        return "R"
    return value

# Ensure column exists
if "File_Name" not in df.columns:
    df["File_Name"] = ""

# Force string type
df["File_Name"] = df["File_Name"].astype(str)

# Generate filenames
for index, row in df.iterrows():
    language = clean(row["Language"])
    character = clean(row["Character"])
    category = clean(row["Category"])
    line_type = short_line_type(row["Line_Type"])
    id_number = format_id(row["ID_Number"])
    variation = clean(row["Variation"]).upper()

    file_name = f"VO_{language}_{character}_{category}_{line_type}_{id_number}_{variation}.wav"

    df.at[index, "File_Name"] = file_name

df.to_excel(EXCEL_PATH, index=False)

print("Done. File_Name column updated.")
print(f"Updated file: {EXCEL_PATH}")