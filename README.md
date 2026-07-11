# waste-text-classifier
Text-based classifier for household waste (wet, dry, recyclable, hazardous, e-waste) with disposal guidance.


## Data

- Schema: `docs/schema.md`
- Sample dataset: `data/examples.csv`

Labels used: wet, dry, recyclable, hazardous, e-waste.

## How to run (Colab)

1. Open the notebook from GitHub (e.g. `waste_text_classifier_week1.ipynb`).
2. In the browser address bar, replace `github.com` with `githubtocolab.com` and press Enter. This opens the notebook in Google Colab.
3. In Colab, add a cell:

   ```python
   import pandas as pd

   url = "https://raw.githubusercontent.com/swaralikoge547-commits/waste-text-classifier/main/data/examples.csv"
   df = pd.read_csv(url)
   print(df.head())
   print(df['category'].value_counts())
   ```
## Baseline text classifier

- Model: TF-IDF (1–2 grams) + LogisticRegression (scikit-learn).
- Input: description field from `data/examples.csv`.
- Output: category label (wet, dry, recyclable, hazardous, e-waste) and disposal guideline lookup.
- Metrics: see `waste_text_classifier_week2.ipynb` for classification report and confusion matrix.
## Results

- Dataset size: 70+ examples
- Labels: wet, dry, recyclable, hazardous, e-waste
- Model: TF-IDF + Logistic Regression
- Strong labels: wet, dry, e-waste
- Moderate labels: recyclable
- Weakest label: hazardous
- Outcome: A working baseline waste text classifier with disposal guidance.
## Project summary

This project classifies household waste text into wet, dry, recyclable, hazardous, and e-waste categories. It also returns a disposal guideline for the predicted item.

The project includes:
- a defined schema,
- a curated dataset,
- validation checks,
- a rule-based baseline,
- a TF-IDF + Logistic Regression model,
- and sample predictions.
