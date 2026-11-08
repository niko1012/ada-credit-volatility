# Project Proposal

Does credit-market information improve one-month-ahead forecasts of S&P 500 realised volatility beyond past volatility and the VIX?

I will study January 1990–December 2025 using daily S&P 500 closing levels from Yahoo Finance, daily VIX observations from Cboe, and the Federal Reserve's monthly Excess Bond Premium (EBP). I have downloaded the datasets, performed initial quality checks and produced descriptive plots.

The prediction target will be the following calendar month's annualised realised volatility, calculated from daily S&P 500 returns.

I will compare three predictor sets: past realised volatility; past volatility and the VIX; and those variables plus the EBP. Linear regression will provide an interpretable baseline, while a small feedforward neural network will investigate nonlinear relationships. A persistence forecast will provide a simple benchmark.

Performance will be evaluated using chronological training, validation and test periods, with MAE and RMSE calculated on identical forecast months.

The analysis will account for the EBP's publication lag and discuss the limitations of revised historical data. The objective is to assess the credit indicator's incremental predictive value. Finding no improvement would also answer the research question.