import pandas as pd
import os
import plotly.express as px

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_advanced_plotly():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df['ts'] = pd.to_datetime(df['ts'])
    
    # Filter for a few tools for better visualization
    selected_tools = df['tool'].unique()[:4]
    df_filtered = df[df['tool'].isin(selected_tools)].sort_values('ts')
    
    # Faceting: Create subplots automatically using 'facet_col'
    fig = px.line(
        df_filtered,
        x='ts',
        y='val3',
        facet_col='tool',
        color='chamber',
        title='Sensor val3 across different Tools (Faceted View)',
        labels={'ts': 'Time', 'val3': 'Sensor Value'}
    )
    
    # Adding a Range Slider for easy navigation of time series
    fig.update_xaxes(rangeslider_visible=True)
    
    # Improving layout
    fig.update_layout(height=500, showlegend=True)
    
    fig.show()

if __name__ == "__main__":
    demonstrate_advanced_plotly()
