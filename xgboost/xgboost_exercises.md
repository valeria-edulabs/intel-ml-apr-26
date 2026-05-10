# XGBoost Hands-On Exercise

This exercise continues the XGBoost demo in `xgboost_demo.ipynb`.

## Objectives

1. Identify the least important feature from the trained XGBoost model.
2. Remove that feature and rerun the cross-validation experiment.
3. Create new features, for example:
   - a boolean `is_summer` flag
   - a `is_peak_month` flag
   - a `month_norm` or `month_quarter` encoding
4. Tune XGBoost hyperparameters and compare results.
5. For each experiment, run time-series cross-validation and record the CV RMSE.
6. Select the best configuration and evaluate it on the holdout test set.

## Exercise steps

### 1. Baseline review

- Open `xgboost_demo.ipynb` and note the baseline feature list.
- Run the notebook through the feature engineering and CV sections.
- Save the baseline CV RMSE and final test RMSE.

### 2. Remove the least important feature

- Use the feature importance output from the final model.
- Identify the feature with the smallest importance score.
- Remove it from `feature_columns`.
- Re-run the cross-validation block using `TimeSeriesSplit`.
- Record the new CV RMSE.

### 3. Add a boolean seasonality feature

- Create a new feature in the notebook, for example:
  - `df["is_summer"] = df.index.month.isin([6, 7, 8]).astype(int)`
  - `df["is_peak_month"] = df.index.month.isin([12, 1, 7]).astype(int)`
- Add that feature to `feature_columns` and rerun CV.
- Compare the RMSE result with the baseline.


### 4. Hyperparameter experiments

Try changing XGBoost hyperparameters and compare CV performance.

Suggested parameters:

- `n_estimators`: 100, 200, 300
- `learning_rate`: 0.01, 0.05, 0.1
- `max_depth`: 3, 4, 6
- `subsample`: 0.8, 1.0
- `colsample_bytree`: 0.6, 0.8, 1.0

For each combination:
- train with CV
- capture CV RMSE
- keep the best configuration

### 5. Compare experiments

- Create a simple table of experiments with:
  - feature set description
  - hyperparameters
  - CV RMSE
  - test RMSE (for the selected best model)

Example table:

| Experiment | Features | Params | CV RMSE | Test RMSE |
|---|---|---|---|---|
| Baseline | baseline features | default xgboost | 15.4 | 16.2 |
| Drop least important | removed `lag_2` | default xgboost | 15.5 | - |
| Add is_summer | baseline + `is_summer` | default xgboost | 15.1 | - |
| Best model | best feature set | tuned params | 14.8 | 15.0 |

### 6. Final evaluation

- Retrain the best model on the full training set.
- Evaluate it on `X_test` / `y_test`.
- Report the final test RMSE and compare to the baseline.

## Notes

- Keep the target shift fixed: the model should always predict the next month.
- Use the same holdout split (last 12 months) for a fair comparison.
- Focus on simple, explainable feature changes.

Good luck! The goal is to learn how feature engineering and hyperparameter tuning affect time-series model performance. 