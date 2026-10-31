# Proposal — draft for review

Does credit-market information improve one-month-ahead forecasts of US equity-market volatility beyond past volatility and the VIX?

I plan to study 1990–2025 using three datasets that have already been downloaded: the Federal Reserve's monthly Excess Bond Premium, Cboe's daily VIX, and daily US equity-market returns from Kenneth French's Data Library. I will construct monthly realised volatility from daily returns and use the following month's volatility as the prediction target.

I will compare forecasts based on past volatility, forecasts adding the VIX, and forecasts additionally including the credit indicator. Linear regression will provide an interpretable baseline, with a small feedforward neural network used to investigate whether nonlinear relationships improve predictions. Performance will be assessed using chronological training, validation and test periods, with MAE and RMSE calculated on the same forecast months.

The exercise will use revised historical data, account for publication lags, and discuss the resulting limitations for real-time forecasting. The objective is to assess the credit indicator's incremental predictive value; finding no improvement would also answer the research question.
