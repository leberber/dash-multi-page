from dash import html
import dash_mantine_components as dmc
from pages.components import header


layout = html.Div(
    id = 'home',
    children = [
    header,
    dmc.Center(
        style={"height": 600, "width": "100%"},
        children=[
            dmc.Text(
                "This is the Home page",
                variant="gradient",
                gradient={"from": "#0CC0DF", "to": "#60C9DB", "deg": 45},
                style={"fontSize": 30},
            )
        ],
    )
])