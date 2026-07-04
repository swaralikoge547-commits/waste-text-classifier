# Contributing guidelines

Thank you for improving the waste-text-classifier project.

## Adding data

- Edit `data/examples.csv`.
- Always keep columns: item_name, description, category, disposal_guideline, source, notes.
- Use labels: wet, dry, recyclable, hazardous, e-waste.
- Keep `item_name` short (1–3 words, lowercase where possible).
- Write `description` as natural language, how a user would type.
- Fill `disposal_guideline` with clear, 1–2 line instructions.
- Use `source` = synthetic / real_user / faq.

Before committing:

- Run `scripts/validate_schema.py` (locally or in Colab).
- Check that category counts and examples look reasonable.

## Code and notebooks

- Keep notebooks small and focused (week-based or topic-based).
- Document any major changes in the README.
