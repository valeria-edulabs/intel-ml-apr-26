import pandas as pd
import plotly.express as px

# Load demo pressure data for the lithography machine
csv_path = "data/litho_sensor_data.csv"
df = pd.read_csv(csv_path, parse_dates=["Timestamp"])

# Use a demo machine identifier for the plot
demo_tool = "LITHO_01"
df_demo = df[df["Tool_ID"] == demo_tool].copy()

df_demo = df_demo.sort_values("Timestamp")

fig = px.line(
    df_demo,
    x="Timestamp",
    y="Pressure_PSI",
    title=f"Demo Pressure on Machine {demo_tool}",
    labels={"Pressure_PSI": "Pressure (PSI)", "Timestamp": "Time"},
    markers=True,
)

print(f"Loaded {len(df_demo)} records for {demo_tool}")
print("Showing demo pressure plot...")
fig.show()
