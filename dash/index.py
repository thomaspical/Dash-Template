#####################################################################
#######     Dash Plotly with Bootstrap Components           #########
#####################################################################

#Loading datas
import logging
import os
import pathlib
import yaml

import dash
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State 

import plotly.graph_objects as go
import plotly.express as px


from app import app, auth

from pages import blank_page

# Exposing server for gunicorn
server = app.server

# Reading environment file for configuration
CONFIGURATION_FILE = 'environment.yaml'
CONFIGURATION_SECTION = os.environ.get('MYAPP_ENV', 'local')

logging.info('Reading configuration file')
with open(CONFIGURATION_FILE, 'r') as file:
    config = yaml.safe_load(file)[CONFIGURATION_SECTION]

os.chdir(config['directory']['application'])


#Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Menu 1", href="/")),
        dbc.NavItem(dbc.NavLink("Menu 2", href="/somewhere")),   
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Menu 3", header=True),
                dbc.DropdownMenuItem("Menu 4", href="/where"),
            ],
            nav=True,
            in_navbar=True,
            label="Menu 0",
        ),
    ],
    brand="My Dashboard",
    brand_href="/",
    color="#384259",
    dark=True,
)

footer = dbc.Row(
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.NavLink("URL Link", href="#", style={'color':'rgba(0,0,0,.5)'}),
                    ],
                    className="mt-2",
                    md=7,
                ),
                dbc.Col([
                    dbc.NavbarSimple(
                        children=[
                            dbc.NavItem(dbc.NavLink("Legal notice", href="#")),
                        ],
                    )],
                    md=5,
                ),
            ])
        ],
    ),
    style={"background":"#f8f9fa"}
)

                
app.layout = (
        html.Div(children=[navbar,
                        dcc.Location(id="url", refresh=False), html.Div(id="page-content"),
                        footer
                ],
                style={"background":"white", "margin-top:":"0"}
        )
)



# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    return blank_page.create_layout(app)
  
#Favicon
@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(server.root_path, 'static'),
                                     'favicon.ico')

if __name__ == '__main__':

    port = config.get('port', 8050)
    debug = config.get('debug', False)

    app.run_server(
        host=config.get('host', '127.0.0.1'),
        debug=debug,
        port=port,
    )

