from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PROJECT_FOLDER = Path(__file__).resolve().parents[1]
DATA_FOLDER = PROJECT_FOLDER / "data" / "raw"
FIGURE_FOLDER = PROJECT_FOLDER / "figures"
FIGURE_FOLDER.mkdir(parents=True, exist_ok=True)

# Load the credit indicator and select the study period.
ebp = pd.read_csv(DATA_FOLDER / "ebp.csv", parse_dates=["date"])
ebp = ebp.set_index("date").sort_index()
ebp = ebp.loc["1990-01-01":"2025-12-31"]

# Plot the Excess Bond Premium.
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(ebp.index, ebp["ebp"])
ax.axhline(0, color="grey", linewidth=0.8)

ax.set_title("Excess Bond Premium — 1990–2025")
ax.set_xlabel("Year")
ax.set_ylabel("Percentage points")

fig.tight_layout()
fig.savefig(FIGURE_FOLDER / "ebp.png", dpi=150)
plt.close(fig)

print("Figure saved: figures/ebp.png")

# Load the VIX and select the study period.
vix = pd.read_csv(DATA_FOLDER / "vix.csv")
vix["DATE"] = pd.to_datetime(vix["DATE"], format="%m/%d/%Y")
vix = vix.set_index("DATE").sort_index()
vix = vix.loc["1990-01-01":"2025-12-31"]

# Plot daily VIX closing values.
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(vix.index, vix["CLOSE"])
ax.set_title("VIX — 1990–2025")
ax.set_xlabel("Year")
ax.set_ylabel("Annualised implied volatility (%)")

fig.tight_layout()
fig.savefig(FIGURE_FOLDER / "vix.png", dpi=150)
plt.close(fig)

print("Figure saved: figures/vix.png")


# Calculate daily S&P 500 returns before selecting the study period.
sp500 = pd.read_csv(DATA_FOLDER / "sp500.csv", parse_dates=["Date"])
sp500 = sp500.set_index("Date").sort_index()

sp500["daily_return"] = sp500["Close"].pct_change(fill_method=None)
sp500 = sp500.loc["1990-01-01":"2025-12-31"]

# Calculate annualised realised volatility for each calendar month.
monthly_volatility = (
    sp500["daily_return"].resample("ME").std(ddof=1)
    * (252 ** 0.5)
    * 100
)

# Plot monthly realised volatility.
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(monthly_volatility.index, monthly_volatility)
ax.set_title("S&P 500 Monthly Realised Volatility — 1990–2025")
ax.set_xlabel("Year")
ax.set_ylabel("Annualised realised volatility (%)")

fig.tight_layout()
fig.savefig(
    FIGURE_FOLDER / "sp500_realised_volatility.png",
    dpi=150,
)
plt.close(fig)

print("Figure saved: figures/sp500_realised_volatility.png")
print("Number of months:", len(monthly_volatility))
print("Missing monthly volatility values:", monthly_volatility.isna().sum())