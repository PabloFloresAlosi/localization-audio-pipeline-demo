import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FINAL_DIR = BASE_DIR / "03_FINAL"
WWISE_READY_DIR = BASE_DIR / "04_WWISE_READY"

LANGUAGE_MAP = {
    "EN": "English(US)",
    "ES": "Spanish(Spain)",
}

copied = 0
skipped = []
errors = []

print("Using FINAL folder:", FINAL_DIR)
print("Creating WWISE READY folder:", WWISE_READY_DIR)

for language_code, wwise_language in LANGUAGE_MAP.items():
    language_folder = FINAL_DIR / language_code

    if not language_folder.exists():
        skipped.append(f"Missing language folder: {language_folder}")
        continue

    for wav_path in language_folder.rglob("*.wav"):
        original_name = wav_path.name

        # Expected format:
        # VO_EN_MA_Greeting_Q_001_A.wav
        parts = original_name.replace(".wav", "").split("_")

        if len(parts) < 7:
            errors.append(f"Unexpected filename format: {wav_path}")
            continue

        prefix = parts[0]          # VO
        file_language = parts[1]   # EN / ES
        character = parts[2]       # MA / FA / SYS

        if file_language != language_code:
            errors.append(
                f"Language mismatch: folder={language_code}, file={file_language}, path={wav_path}"
            )
            continue

        # Remove language from filename:
        # VO_EN_MA_Greeting_Q_001_A.wav
        # becomes:
        # VO_MA_Greeting_Q_001_A.wav
        new_parts = [prefix] + parts[2:]
        new_name = "_".join(new_parts) + ".wav"

        destination_folder = WWISE_READY_DIR / wwise_language / character
        destination_folder.mkdir(parents=True, exist_ok=True)

        destination_path = destination_folder / new_name

        shutil.copy2(wav_path, destination_path)
        copied += 1

        print(f"Copied: {original_name} -> {wwise_language}/{character}/{new_name}")

print("\nDone.")
print(f"Total copied: {copied}")
print(f"Total skipped: {len(skipped)}")
print(f"Total errors: {len(errors)}")

if skipped:
    skipped_log = BASE_DIR / "csv" / "wwise_ready_skipped.txt"
    with open(skipped_log, "w", encoding="utf-8") as f:
        for item in skipped:
            f.write(item + "\n")
    print(f"Skipped log saved to: {skipped_log}")

if errors:
    errors_log = BASE_DIR / "csv" / "wwise_ready_errors.txt"
    with open(errors_log, "w", encoding="utf-8") as f:
        for item in errors:
            f.write(item + "\n")
    print(f"Errors log saved to: {errors_log}")