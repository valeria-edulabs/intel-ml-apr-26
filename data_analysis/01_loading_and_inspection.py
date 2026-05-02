import pandas as pd

import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_loading():
    # Loading the dataset
    # We use index_col=0 because the first column is an unnamed index
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    # Preview the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check data types and missing values
    print("\nDataset Info:")
    df.info()
    
    # Statistical summary of numeric columns
    print("\nStatistical Summary:")
    print(df.describe())
    
    # Checking unique tools and chambers
    print(f"\nUnique Tools: {df['tool'].unique()}")
    print(f"Unique Chambers: {df['chamber'].unique()}")

if __name__ == "__main__":
    demonstrate_loading()
