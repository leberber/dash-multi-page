from dash import html
import dash_mantine_components as dmc


from pages.components import header

sidebar = html.Div(
    className='archive-sidebar sidebar-style',
    children=[

])
content = html.Div(
    
    className='archive-content',
    children=[
    header,
    dmc.Center(
        style={"height": 600, "width": "100%"},
        children=[
            dmc.Text(
                "Nothing is Archived",
                variant="gradient",
                gradient={"from": "#0CC0DF", "to": "#60C9DB", "deg": 45},
                style={"fontSize": 30},
            )
        ],
    )
])

layout = html.Div(
    id = 'archive',
    children=[
    sidebar,
    content
])