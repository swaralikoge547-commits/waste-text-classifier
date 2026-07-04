import sys
import pandas as pd

ALLOWED_CATEGORIES = {"wet", "dry", "recyclable", "hazardous", "e-waste"}
REQUIRED_COLUMNS = ["item_name", "description", "category", "disposal_guideline", "source", "notes"]

def main():
    path = "data/examples.csv"
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"ERROR: Could not read {path}: {e}")
        sys.exit(1)

    # Check columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"ERROR: Missing columns: {missing}")
        sys.exit(1)

    # Check categories
    bad_cat = df[~df["category"].isin(ALLOWED_CATEGORIES)]
    if not bad_cat.empty:
        print("ERROR: Invalid category values:")
        print(bad_cat[["item_name", "category"]])
        sys.exit(1)

    # Check item_name word count (1–3 words)
    def word_count_ok(name: str) -> bool:
        if not isinstance(name, str):
            return False
        words = name.strip().split()
        return 1 <= len(words) <= 3

    bad_name = df[~df["item_name"].apply(word_count_ok)]
    if not bad_name.empty:
        print("WARNING: item_name with word count outside 1–3:")
        print(bad_name[["item_name"]])

    # Check disposal_guideline not empty
    empty_guideline = df[df["disposal_guideline"].isna() | (df["disposal_guideline"].astype(str).str.strip() == "")]
    if not empty_guideline.empty:
        print("ERROR: Empty disposal_guideline for rows:")
        print(empty_guideline[["item_name", "description"]])
        sys.exit(1)

    # Summary
    print("OK: examples.csv passed basic validation.")
    print("Category counts:")
    print(df["category"].value_counts())

if __name__ == "__main__":
    main()
