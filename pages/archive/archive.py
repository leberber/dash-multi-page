from dash import register_page, callback, html,  Input, Output
import dash_mantine_components as dmc
import plotly.graph_objects as go


register_page(__name__, path='/archive')

from pages.archive.layout import layout

layout = layout