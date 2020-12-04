import os

import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State 

from app import app

txt_notice=[
        html.H5("1. Random text"),
        html.P([
            "Blank template",
            html.Br(),
            html.U("Owner:")," You",
        ]),
]

def create_layout(app):
    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("H2 title"),
                            html.Div(txt_notice),
                        ],
                        style={"text-align":"justify"},
                        xl=12,
                        
                    ),
                ],
                justify="center",
            ),
        ],
        className="mt-4",
    )
                   
    return body