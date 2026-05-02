import pandas as pd

import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_cleaning():
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    # Checking for missing values
    print("Missing values per column:")
    print(df.isnull().sum())
    
    # Strategy 1: Dropping rows with missing sensor data
    # Good if the missingness is rare
    df_dropped = df.dropna(subset=['val3', 'val4'])
    print(f"\nShape after dropping NaNs: {df_dropped.shape}")
    
    # Strategy 2: Filling missing values (Imputation)
    # Using Forward Fill (ffill) is common in sensor data where the state 
    # is assumed to remain constant until the next reading.
    df_filled = df.sort_values('ts').ffill()
    
    print("\nMissing values after forward fill:")
    print(df_filled.isnull().sum())
    
    # Strategy 3: Linear Interpolation
    # Instead of a 'step' change (ffill), this creates a smooth transition
    # between the last known and next known values.
    df_interpolated = df.sort_values('ts').interpolate(method='linear')
    print("\nMissing values after linear interpolation:")
    print(df_interpolated.isnull().sum())

    # Strategy 4: Group-Specific Imputation (Advanced)
    # Filling missing values with the mean of the SAME tool/chamber
    # This is much more accurate than using a global average.
    df['val5'] = df.groupby(['tool', 'chamber'])['val5'].transform(lambda x: x.fillna(x.mean()))
    print("\nRemaining nulls in val5 after Group-Specific Fill:")
    print(df['val5'].isnull().sum())

    # Strategy 5: Filling with a Constant (Zero or Global Mean)

if __name__ == "__main__":
    demonstrate_cleaning()
