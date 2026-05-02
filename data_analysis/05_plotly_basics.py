import pandas as pd
import os
import plotly.express as px

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the dataset relative to this script
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sensors_sample.csv")

def demonstrate_plotly_basics():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df['ts'] = pd.to_datetime(df['ts'])
    
    # Filter for one tool to keep the plot clean
    target_tool = df['tool'].iloc[0]
    df_tool = df[df['tool'] == target_tool].sort_values('ts')
    
    # Basic Line Plot
    # This shows how a sensor value changes over time
    fig = px.line(
        df_tool, 
        x='ts', 
        y='val3', 
        title=f'Sensor val3 Trend for Tool {target_tool}',
        labels={'ts': 'Timestamp', 'val3': 'Sensor Reading'}
    )
    
    # Adding interactive features
    fig.update_traces(mode='lines+markers')
    
    # Show the plot (this will open in a browser)
    fig.show()

if __name__ == "__main__":
    demonstrate_plotly_basics()
