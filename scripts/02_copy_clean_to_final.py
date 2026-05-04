import pandas as pd
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EXCEL_PATH = BASE_DIR / "csv" / "02. Audio Dialogue Database.xlsx"
CLEAN_DIR = BASE_DIR / "02_CLEAN"
FINAL_DIR = BASE_DIR / "03_FINAL"

print("Using Excel:", EXCEL_PATH)
print("Using CLEAN folder:", CLEAN_DIR)
print("Using FINAL folder:", FINAL_DIR)

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

copied = 0
missing = []
skipped = []

for _, row in df.iterrows():
    language = clean(row["Language"])
    character = clean(row["Character"])
    line_type = short_line_type(row["Line_Type"])
    id_number = format_id(row["ID_Number"])
    variation = clean(row["Variation"]).upper()

    final_name = clean(row["File_Name"])

    if not final_name or final_name.lower() == "nan":
        skipped.append(f"Missing File_Name for ID {id_number}_{variation}_{character}_{line_type}_{language}")
        continue

    source_name = f"{id_number}_{variation}_{character}_{line_type}_{language}.wav"
    source_path = CLEAN_DIR / language / character / source_name

    final_folder = FINAL_DIR / language / character
    final_folder.mkdir(parents=True, exist_ok=True)

    final_path = final_folder / final_name

    if source_path.exists():
        shutil.copy2(source_path, final_path)
        copied += 1
        print(f"Copied: {source_name} -> {final_name}")
    else:
        missing.append(str(source_path))

print("\nDone.")
print(f"Total copied: {copied}")
print(f"Total missing: {len(missing)}")
print(f"Total skipped: {len(skipped)}")

if missing:
    missing_log = BASE_DIR / "csv" / "missing_files.txt"
    with open(missing_log, "w", encoding="utf-8") as f:
        for file in missing:
            f.write(file + "\n")
    print(f"Missing files saved to: {missing_log}")

if skipped:
    skipped_log = BASE_DIR / "csv" / "skipped_files.txt"
    with open(skipped_log, "w", encoding="utf-8") as f:
        for file in skipped:
            f.write(file + "\n")
    print(f"Skipped files saved to: {skipped_log}")