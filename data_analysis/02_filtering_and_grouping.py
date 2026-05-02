import pandas as pd

import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_filtering_grouping():
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    # 2. Filtering by Sensor Thresholds (Anomaly Detection)
    # Finding instances where val3 is above 5.5 (potential outlier/issue)
    anomalies = df[df['val3'] > 5.5]
    print(f"\nDetected {len(anomalies)} anomalies in sensor val3 (> 5.5):")
    print(anomalies.head())

    # 3. Complex Filtering (Logical Operators)
    # Finding data for Chamber 1 OR Chamber 5, excluding Tool 11
    complex_filter = df[((df['chamber'] == 1) | (df['chamber'] == 5)) & (df['tool'] != 11)]
    print(f"\nFiltered Data (Chambers 1 or 5, excluding Tool 11):")
    print(complex_filter.head())

    # 4. Grouping for Benchmarking
    # Calculating the average sensor values per tool
    tool_performance = df.groupby('tool')[['val3', 'val4']].mean()
    print("\nAverage Sensor Values per Tool (Top 5):")
    print(tool_performance.sort_values('val3', ascending=False).head())

    # 5. Pivot Tables (Powerful Cross-tabulation)
    # Comparing val3 averages across Tools (rows) and Chambers (columns)
    pivot = df.pivot_table(values='val3', index='tool', columns='chamber', aggfunc='mean')
    print("\nPivot Table: Mean val3 per Tool and Chamber:")
    print(pivot.head())

    # 6. Multi-level Aggregation
    chamber_stats = df.groupby(['tool', 'chamber'])['val3'].agg(['mean', 'std', 'count'])
    
    print("\nStatistics by Tool and Chamber (val3):")
    print(chamber_stats.head(10))

if __name__ == "__main__":
    demonstrate_filtering_grouping()
