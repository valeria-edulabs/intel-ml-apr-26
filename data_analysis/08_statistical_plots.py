import pandas as pd
import os
import plotly.express as px

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_stats_plots():
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    # Histogram: Understanding the distribution of sensor values
    # This helps identify if the process follows a Normal Distribution
    fig_hist = px.histogram(
        df, 
        x='val3', 
        color='chamber', 
        nbins=50,
        title='Distribution of Sensor val3 by Chamber',
        marginal='box' # Adds a box plot on top for outlier detection
    )
    fig_hist.show()
    
    # Box Plot: Comparing variability across tools
    # Critical for Identifying which tool might need maintenance
    fig_box = px.box(
        df, 
        x='tool', 
        y='val4', 
        title='Sensor val4 Variability per Tool',
        points='outliers' # Show outliers explicitly
    )
    fig_box.show()

if __name__ == "__main__":
    demonstrate_stats_plots()
