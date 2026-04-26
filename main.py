import pandas as pd
import plotly.express as px

print("pandas version:", pd.__version__)

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 1, 3]})
print(df)

fig = px.line(df, x="x", y="y", title="Plotly test")
print("plotly figure created:", fig is not None)

fig.show()
