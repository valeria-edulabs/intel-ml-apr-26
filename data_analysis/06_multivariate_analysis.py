import pandas as pd
import os
import plotly.express as px

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_multivariate():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df['ts'] = pd.to_datetime(df['ts'])
    
    # Sampling the data to ensure the plot remains responsive
    df_sample = df.sample(1000).sort_values('ts')
    
    # Scatter plot comparing two sensors
    # Using 'color' to distinguish between chambers
    # Using 'hover_data' to show tool info on hover
    fig = px.scatter(
        df_sample,
        x='val3',
        y='val4',
        color='chamber',
        hover_data=['tool', 'ts'],
        title='Correlation: val3 vs val4 (Colored by Chamber)',
        template='plotly_dark'
    )
    
    fig.show()

if __name__ == "__main__":
    demonstrate_multivariate()
