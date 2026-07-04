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
