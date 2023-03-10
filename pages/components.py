from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
header = html.Div(
    className='header-component',
    children=[
        dmc.Group(
        position = 'right',
        children=[
            dmc.Button(
                "Connect to Database",
                variant="subtle",
                leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                className='header-item hovered'
            ),
            dmc.Button(
                "Load Data",
                variant="subtle",
                rightIcon=DashIconify(icon="ri:loader-4-line"),
                className='header-item hovered'
            ),
            dmc.Button(
                "Settings",
                color='dark',
                variant="outline",
                leftIcon=DashIconify(icon="fluent:settings-32-regular"),
                className='header-item hovered'
            ),
        ])
]
)