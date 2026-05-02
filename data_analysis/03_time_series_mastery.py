import pandas as pd

import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_time_series():
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    # Converting the 'ts' column to actual datetime objects
    # This is critical for time-based operations
    df['ts'] = pd.to_datetime(df['ts'])
    
    # Setting the timestamp as the index
    # This enables powerful time-based slicing and resampling
    df = df.set_index('ts').sort_index()
    
    print("DataFrame with DateTime Index:")
    print(df.head())
    
    # 2. Time-Based Slicing (Specific Ranges)
    # Slicing for a specific 4-hour window
    start_time = df.index[0]
    end_time = start_time + pd.Timedelta(hours=4)
    print(f"\nData from {start_time} to {end_time}:")
    print(df.loc[start_time:end_time].head())

    # 3. Rolling Windows (Smoothing)
    # Calculating a 5-sample moving average to reduce sensor noise
    df['val3_smoothed'] = df['val3'].rolling(window=5).mean()
    print("\nOriginal vs Smoothed val3 (First 10 rows):")
    print(df[['val3', 'val3_smoothed']].head(10))

    # 4. Extracting Time Components
    # Useful for finding patterns based on the time of day
    df['hour'] = df.index.hour
    print("\nAverage val3 by Hour of Day:")
    print(df.groupby('hour')['val3'].mean().head())

    # 5. Advanced Resampling
    # Calculating Min, Max, and Mean in one go
    hourly_stats = df['val3'].resample('h').agg(['min', 'max', 'mean'])
    
    print("\nHourly Statistics (Min, Max, Mean):")
    print(hourly_stats.head())

    # 6. Time Shifting
    # Calculating the difference between current and previous reading
    df['val3_diff'] = df['val3'].diff()
    print("\nDifference from previous reading (val3_diff):")
    print(df['val3_diff'].head())

    # 7. Fuzzy Joining with merge_asof (Recipe/Event Correlation)
    # Creating a dummy 'Recipe Log' to demonstrate joining non-matching timestamps
    event_logs = pd.DataFrame({
        'ts': pd.to_datetime([df.index[0], df.index[1000], df.index[5000]]),
        'recipe_id': ['RECIPE_A', 'RECIPE_B', 'RECIPE_C']
    }).sort_values('ts')

    # Merging sensor data with the recipe log
    # This finds the 'last known recipe' for every sensor reading
    df_reset = df.reset_index() # merge_asof requires the join key to be a column
    merged_df = pd.merge_asof(df_reset, event_logs, on='ts', direction='backward')
    
    print("\nFuzzy Join Result (Sensor + Recipe ID):")
    print(merged_df[['ts', 'val3', 'recipe_id']].head(15))


def demo_asof_with_sample_csvs():
    demo1_path = os.path.join(SCRIPT_DIR, "..", "data", "demo_sensor1.csv")
    demo2_path = os.path.join(SCRIPT_DIR, "..", "data", "demo_sensor2.csv")

    sensor1 = pd.read_csv(demo1_path, parse_dates=["ts"]).sort_values("ts")
    sensor2 = pd.read_csv(demo2_path, parse_dates=["ts"]).sort_values("ts")

    print("\nDemo sensor1 readings:")
    print(sensor1)
    print("\nDemo sensor2 readings:")
    print(sensor2)

    # merge_asof finds the closest prior sensor1 value for each sensor2 timestamp.
    asof_joined = pd.merge_asof(
        sensor2,
        sensor1,
        on='ts',
        direction='backward'
    )

    print("\nmerge_asof(sensor2, sensor1, on='ts', direction='backward'):")
    print(asof_joined)

    # Use a tolerance to require the prior value to be within 10 seconds.
    asof_with_tolerance = pd.merge_asof(
        sensor2,
        sensor1,
        on='ts',
        direction='backward',
        tolerance=pd.Timedelta('10s')
    )

    print("\nmerge_asof with 10-second tolerance:")
    print(asof_with_tolerance)

    # The Series.asof method gives the last valid value before each query timestamp.
    sensor1_series = sensor1.set_index('ts')['sensor1']
    sensor2 = sensor2.copy()
    sensor2['sensor1_asof'] = sensor1_series.asof(sensor2['ts']).values

    print("\nSeries.asof(sensor2['ts']) result:")
    print(sensor2)


if __name__ == "__main__":
    demonstrate_time_series()
    demo_asof_with_sample_csvs()
