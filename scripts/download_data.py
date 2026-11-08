from pathlib import Path

import pandas as pd
import requests


# Create the folder containing the downloaded datasets.
DATA_FOLDER = Path("data/raw")
DATA_FOLDER.mkdir(parents=True, exist_ok=True)

# Include December 1989 to calculate the first return of January 1990.
start_date = pd.Timestamp("1989-12-01", tz="UTC")
end_date = pd.Timestamp("2026-01-01", tz="UTC")

url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC"

parameters = {
    "period1": int(start_date.timestamp()),
    "period2": int(end_date.timestamp()),
    "interval": "1d",
}

response = requests.get(
    url,
    params=parameters,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30,
)
response.raise_for_status()

# Extract daily dates and closing levels from Yahoo Finance.
result = response.json()["chart"]["result"][0]

sp500 = pd.DataFrame({
    "Date": pd.to_datetime(
        result["timestamp"], unit="s", utc=True
    ).strftime("%Y-%m-%d"),
    "Close": result["indicators"]["quote"][0]["close"],
})

sp500 = sp500.sort_values("Date")
sp500.to_csv(DATA_FOLDER / "sp500.csv", index=False)

print("S&P 500 data saved.")
print("Number of observations:", len(sp500))
print(sp500.head())
print(sp500.tail())

# Download the VIX and Excess Bond Premium datasets.
sources = {
    "vix.csv": (
        "https://cdn-api.cboe.com/api/global/us_indices/"
        "daily_prices/VIX_History.csv"
    ),
    "ebp.csv": (
        "https://www.federalreserve.gov/econres/"
        "notes/feds-notes/ebp_csv.csv"
    ),
}

for filename, source_url in sources.items():
    response = requests.get(
        source_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()

    file_path = DATA_FOLDER / filename
    file_path.write_bytes(response.content)

    dataset = pd.read_csv(file_path)

    print("\nDataset:", filename)
    print("Number of observations:", len(dataset))
    print(dataset.head(2))
    print(dataset.tail(2))