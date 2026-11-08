# Credit Markets and S&P 500 Volatility

**Nikola Samardzic — Advanced Data Analytics — HEC Lausanne, 2026**

## Research Question

Does credit-market information improve one-month-ahead forecasts of S&P 500 realised volatility beyond past volatility and the VIX?

## Project Overview

This project examines whether information from the corporate bond market improves forecasts of US equity-market risk.

Credit-market conditions may contain information about future equity volatility that is not fully captured by past volatility or the VIX.

The objective is to assess this additional predictive value by comparing forecasts with and without a credit-market indicator. Finding no improvement would also provide an answer to the research question.

## Data

The study covers January 1990 to December 2025 and uses three publicly accessible sources:

| Source | Dataset | Frequency | Role |
|---|---|---|---|
| Yahoo Finance | S&P 500 index closing levels (`^GSPC`) | Daily | Construction of realised volatility |
| Cboe | VIX closing values | Daily | Implied-volatility indicator |
| Federal Reserve Board | Excess Bond Premium (EBP) | Monthly | Credit-market indicator |

Daily S&P 500 returns are calculated from consecutive closing levels using:

`daily_return = close_today / close_previous_trading_day - 1`

The final trading-day close of December 1989 is also collected to calculate the first daily return of January 1990.

The S&P 500 series is a price index: the calculated returns exclude reinvested dividends.

Using the S&P 500 aligns the equity-market universe with the index underlying the VIX.

### Sources

- [Yahoo Finance — S&P 500 Historical Data](https://finance.yahoo.com/quote/%5EGSPC/history/)
- [Cboe — VIX Historical Data](https://www.cboe.com/tradable-products/vix/vix-historical-data)
- [Federal Reserve Board — Excess Bond Premium](https://www.federalreserve.gov/econres/notes/feds-notes/updating-the-recession-risk-and-the-excess-bond-premium-20161006.html)

## Prediction Target

The prediction target is realised S&P 500 volatility during the following calendar month.

Monthly realised volatility is calculated as the sample standard deviation of daily returns within each month, annualised by multiplying by the square root of 252.

Forecasts are formed at each month-end to predict volatility during the next month. Predictor alignment accounts for publication timing, subject to the historical-data limitations discussed below.

## Methodology

### Predictor Sets

Three sets of predictors are compared:

1. **Past volatility:** realised volatility during the most recently completed month.
2. **Past volatility and VIX:** the first predictor set plus the final VIX closing value of the month.
3. **Past volatility, VIX and credit:** the second predictor set plus the EBP, lagged to account for its publication timing.

Comparisons use the same forecast months so that differences in accuracy reflect the information added.

### Models

- **Persistence benchmark:** next month's volatility is forecast to equal the most recently observed monthly volatility.
- **Linear regression:** an interpretable model for assessing the contribution of each predictor set.
- **Small feedforward neural network:** a model for investigating whether nonlinear relationships improve forecast accuracy.

### Evaluation

Training, validation and test periods follow chronological order.

Model settings and preprocessing are determined using the training and validation periods. The test period is reserved for the final evaluation.

Any preprocessing parameters, including scaling parameters, are estimated using training data only.

Forecast accuracy is assessed using:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

The central comparison is whether adding the EBP reduces forecast errors relative to a model using past volatility and the VIX.

## Limitations

The EBP is a monthly estimate published with a delay and subject to historical revisions. Lagging the series addresses publication timing but does not reconstruct the values originally available to investors at each historical date.

The analysis therefore evaluates predictive relationships using revised historical data rather than providing a fully real-time forecasting simulation.

The relatively small number of monthly observations limits the complexity of the models, particularly the neural network. Relationships between credit conditions and equity volatility may also change over time.

The VIX reflects option-implied volatility over approximately 30 days, whereas the prediction target measures realised volatility over the next calendar month. Their horizons are similar but do not match exactly.

The analysis assesses predictive performance and does not establish a causal relationship between credit conditions and equity volatility.

## Working Environment

The project uses Python and Jupyter notebooks in GitHub Codespaces.

Data sources, preparation steps, modelling choices and evaluation procedures are documented alongside the code.
