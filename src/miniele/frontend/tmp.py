import numpy as np
import plotly.graph_objects as go
from nicegui import ui

data = np.array([[0.62635324, 0.37618582],  
                 [0.66091037, 0.58762549],
                 [0.90949296, 0.16623247]])

fig = go.Figure(data=go.Heatmap(
                   z=data,
                   colorscale='Viridis'))

fig.update_layout(
    title='Heatmap',
    width=500,
    height=500,
    margin=dict(l=20, r=20, t=40, b=20)
)

@ui.page('/')
def main():
    ui.plotly(fig)

ui.run(port=8900)
