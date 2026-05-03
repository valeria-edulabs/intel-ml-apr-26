# Prophet Hands-On Exercise

## Goal
Use the time series data from `data/s1_august_23.csv` to build and compare Prophet models. Apply different trend, seasonality, and changepoint settings from `ml_timeseries_basics/prophet.ipynb`, then determine which model performs best.

## Data
- File: `/Users/valeria/src/intel/intel-ml-apr-26/data/s1_august_23.csv`
- Load the dataset into a DataFrame and inspect the date column and target variable.
- Prepare the data for Prophet using `ds` and `y` columns.

## Suggested workflow
1. Load the CSV and inspect the data.
2. Convert the dataset into Prophet format:
   - `ds`: datetime column
   - `y`: target column
3. Visualize the series.
4. Fit at least three different Prophet configurations and evaluate them.

## Prophet model options to explore
Use the following configuration options in your experiments:

- `growth`: `linear`, `logistic`
- `changepoint_prior_scale`: try values such as `0.01`, `0.05`, `0.1`, `0.5`
- `seasonality_mode`: `additive`, `multiplicative`
- `seasonality_prior_scale`: try values such as `0.01`, `1.0`, `10.0`
- `yearly_seasonality`: enable/disable and vary the Fourier order
- `weekly_seasonality` / `daily_seasonality`: disable if data is monthly or daily with no strong weekly/daily signal

## Evaluation
- Use cross-validation and `performance_metrics` from Prophet diagnostics.
- Track at least one error metric such as `mape`, `rmse`, or `mae`.
- For each model configuration, record:
  - parameter values
  - cross-validation results
  - performance metrics

## Questions to answer
1. Which Prophet configuration gave the best performance for `s1_august_23.csv`?
2. Did `growth='logistic'` improve the fit compared to `growth='linear'`?
3. Which `changepoint_prior_scale` value gave the best balance between flexibility and stability?
4. Did `seasonality_mode='multiplicative'` or `additive` perform better for this dataset?
5. What is your selected final model and why?

## Deliverables
- A short summary of the best model configuration.
- A comparison table of the models you tested.
- A recommendation for the final Prophet settings based on the experiment.
