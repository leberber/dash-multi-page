from dash import html
import dash_mantine_components as dmc
from pages.components import header

sidebar = html.Div(
    className='analytics-sidebar sidebar-style',
    children=[
        dmc.Button(
        "Show Graph",
        id = 'show-graph',
        variant="subtle",
        color="grape",
        className='hovered'
    ),

])
content = html.Div(
    
    className='analytics-content',
    children=[
    header,
    html.Div(id = 'graph-container', style = {'padding':'15%'})
])

layout = html.Div(
    id = 'analytics',
    children=[
    sidebar,
    content
])