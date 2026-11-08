from pathlib import Path

import pandas as pd


DATA_FOLDER = Path(__file__).resolve().parents[1] / "data" / "raw"

datasets = [
    ("S&P 500", "sp500.csv", "Date", "%Y-%m-%d"),
    ("VIX", "vix.csv", "DATE", "%m/%d/%Y"),
    ("EBP", "ebp.csv", "date", "%Y-%m-%d"),
]

for name, filename, date_column, date_format in datasets:
    data = pd.read_csv(DATA_FOLDER / filename)

    data[date_column] = pd.to_datetime(
        data[date_column],
        format=date_format,
    )

    print("\nDataset:", name)
    print("Observations:", len(data))
    print("First date:", data[date_column].min().date())
    print("Last date:", data[date_column].max().date())
    print("Duplicate dates:", data[date_column].duplicated().sum())
    print("Missing values:")
    print(data.isna().sum())