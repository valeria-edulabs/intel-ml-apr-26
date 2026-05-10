# Prophet Hands-On Exercise

## Goal
Build a production-style time series workflow using `data/s1_august_23.csv` and the future simulation file `data/s1_august_23_future.csv`.

The task is to predict whether the minimum flow in the next 10-minute interval will fall below a chosen threshold, then simulate hourly retraining as new data arrives.

## Data
- Primary file: `data/s1_august_23.csv`
- Future-simulation file: `data/s1_august_23_future.csv`
- The raw data covers August 1–31, 2023 up to 22:00.
- The data is sampled every few seconds.

## Problem definition
- Aggregate raw samples into fixed 10-minute intervals.
- Compute the minimum flow value for each interval.
- Define a target label for the next interval: whether the upcoming 10-minute minimum flow is below a threshold.
- Train models on historical 10-minute aggregates, and test on unseen later intervals.

## Suggested workflow
1. Load and inspect `data/s1_august_23.csv`.
2. Convert the timestamp column to datetime.
3. Resample or aggregate the raw data into 10-minute bins.
4. For each bin, store the minimum flow.
5. Create the prediction target using the next 10-minute interval’s minimum.
6. Split the data chronologically into 80% train and 20% test.

## Model development
- Use `ml_timeseries_basics/prophet.ipynb` for exploration and Prophet examples.
- The final code should be written in `.py` files, while the notebook may be used for analysis and experimentation.
- Fit multiple models or Prophet configurations and compare them.

## Prophet model options to explore
Try combinations of:
- `growth`: `linear`, `logistic`
- `changepoint_prior_scale`: `0.01`, `0.05`, `0.1`, `0.5`
- `seasonality_mode`: `additive`, `multiplicative`
- `seasonality_prior_scale`: `0.01`, `1.0`, `10.0`
- `yearly_seasonality`, `weekly_seasonality`, `daily_seasonality`
- Fourier order for seasonal components

## Evaluation and validation
- Use Prophet’s `cross_validation` and `performance_metrics` for model validation.
- Track error metrics such as `rmse`, `mae`, and `mape`.
- For a threshold-based label, also track classification metrics such as precision, recall, and accuracy.
- Ensure each retrained model has an acceptable validation score before using it to predict.
- Record:
  - parameter search configurations
  - validation scores for each configuration
  - the chosen best model and why it was selected

## Hourly retraining simulation
1. Implement a Python program that simulates reading new data hourly from `data/s1_august_23_future.csv`.
2. At each simulated hour:
   - append the new data to the historical dataset,
   - recompute 10-minute aggregated minimums,
   - retrain the model,
   - validate the retrained model,
   - make predictions for the next 10-minute horizon.
3. If validation fails, report the failure and do not use the model for production predictions.
4. The simulation should demonstrate how model performance changes as new data arrives.

## Questions to answer
1. How did you aggregate the raw data into 10-minute minimums?
2. What threshold did you choose for the low-flow alert, and why?
3. Which Prophet configuration gave the best validation performance?
4. How did you split the data into train and test sets?
5. How does the hourly retraining simulation work, and what did it show about model stability?

## Deliverables
- Python scripts that perform data preparation, training, parameter search, and retraining simulation.
- A notebook-based exploration using `ml_timeseries_basics/prophet.ipynb` for model experimentation.
- A summary of the best model configuration and validation results.
- A results table comparing the different parameter settings and their performance.
