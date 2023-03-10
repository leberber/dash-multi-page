


from dash import Dash, page_container, html, dcc
import dash_mantine_components as dmc


app = Dash(__name__, use_pages=True,  suppress_callback_exceptions=True)


def page_link (pageHref, hoverIngoText):
    return dcc.Link([
                 dmc.HoverCard(
                     transition="fade",
                     position='right-start',
                     children=[
                        dmc.HoverCardTarget(dmc.Image(src=f"/assets/svg/{pageHref}.svg", width=30)),
                        dmc.HoverCardDropdown(dmc.Text(hoverIngoText, color = 'black', size="sm")),
                    ],
                ), 
            ], 
            href=f"/{pageHref.replace('home', '')}",  
            className='pages-sidebar-links hovered-link'
        )




app.layout = html.Div([
        html.Div([
            page_link('home', 'This is the home page'),
            page_link('analytics', 'This is the analythics page'),
            page_link('archive', 'This is the archive page'),
            dmc.Image(src="/assets/svg/plotly.svg",  className='plotly-logo hovered-link', width=35),
                  
                ], 
       
                id = 'dash-page-navigation-bar'
        ),
        
        html.Div([
            page_container
            ],
            id = 'dash-page-container'
            
        )
	
    ], 
    id = 'dash-app-layout'
                      
)
# dmc.Anchor("Link1", href="/"), mdi:analytics #dash-page-container, dash-app-layout

if __name__ == '__main__':
	app.run_server(
     port=8070,  debug = True #, host = '0.0.0.0',  dev_tools_ui=False, dev_tools_props_check=False
    )