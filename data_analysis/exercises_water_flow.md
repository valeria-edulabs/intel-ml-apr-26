# Exercise: Water Flow Analysis (S1 & S2)

In this exercise, you will act as a Data Engineer at Intel responsible for monitoring water flow in a fabrication facility. You have been provided with two separate sensor datasets (S1 and S2) that track flow rates at different points in the system.

Your goal is to clean, merge, and analyze this data to understand the system's behavior and identify potential issues.

> [!TIP]
> Use **GitHub Copilot** to help you write the code. Try typing a comment describing what you want to do, and let Copilot suggest the implementation.

---

## 0. Setup & Data Loading

The prepared August 2023 datasets are already available in the repository under `data/`:
- **Sensor S1**: `data/s1_august_23.csv`
- **Sensor S2**: `data/s2_august_23.csv`

**Task:**
1. Use `pd.read_csv()` to load `data/s1_august_23.csv` and `data/s2_august_23.csv`.
2. Load them into two DataFrames: `df_s1` and `df_s2`.

---

## 1. Data Exploration

Before diving into analysis, you need to understand the structure of your data.

**Tasks:**
- Display the first 5 rows of both DataFrames.
- Check the data types of each column. Are the timestamps recognized as dates?
- Use `.describe()` to see the statistical summary of the flow rates.
- Check for missing values in both datasets.

---

## 2. Data Cleaning

Sensor data is often "noisy" or has gaps.

**Tasks:**
- Convert the timestamp columns to proper `datetime` objects.
- Sort both DataFrames by the timestamp.
- Handle any missing values (NaNs). Should you drop them or interpolate?
- Remove any duplicate timestamps if they exist.

---

## 3. Data Optimization

The August datasets are already prepared, so you can skip the filtering step and use the provided files directly.

**Tasks:**
- Confirm that `df_s1` and `df_s2` contain only August 2023 data.
- If you want, save cleaned versions back to CSV, but this is optional.
- Continue using these two DataFrames for the rest of the exercise.

---

## 4. Merging with `merge_asof`

The sensors S1 and S2 might not take samples at the exact same millisecond. To compare them, we need to align them using a "nearest" time match.

**Task:**
- Use `pd.merge_asof()` to merge the August datasets.
- Ensure you merge in a way that aligns S2 readings to the closest S1 timestamp.
- Name the final merged DataFrame `df_merged`.

---

## 5. Analysis Questions

Answer the following questions using **Pandas** for calculations and **Plotly** for visualizations.

1. **Visual Comparison**: Create a line chart showing both S1 and S2 flow rates over the entire period. Do they seem to follow the same pattern?
2. **Correlation**: What is the Pearson correlation coefficient between S1 and S2? Does a change in S1 immediately reflect in S2?
3. **Flow Ratio**: Create a new column `flow_ratio` (S1 / S2). Plot this ratio over time. Are there periods where the ratio deviates significantly from 1.0?
4. **Hourly Patterns**: What is the average flow rate for each hour of the day? Visualize this using a bar chart.
5. **Weekly Trends**: Is the water flow higher on weekdays compared to weekends? Use a box plot to compare.
6. **Anomaly Detection**: Define an "anomaly" as any flow rate 3 standard deviations above the mean. Identify these points and mark them on a scatter plot.
7. **Rolling Averages**: Calculate a 1-hour rolling average for both sensors to smooth out the noise. Plot the original vs. smoothed data.
8. **Sampling Consistency**: Calculate the time difference between consecutive readings. Is the sampling frequency consistent (e.g., every 5 seconds), or are there gaps?
9. **Daily Volume**: Calculate the total "volume" of water passed each day (hint: sum the flow rates per day).
10. **Interactive Heatmap**: Create a density heatmap showing the flow rate distribution by "Hour of Day" (Y-axis) vs. "Day of Week" (X-axis).

---

## Expected Outcome
By the end of this exercise, you should have a Jupyter Notebook that tells a story: from raw, messy sensor data to clear, actionable insights about the facility's water usage.
