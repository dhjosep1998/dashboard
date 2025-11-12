from dash import Dash
import dash_bootstrap_components as dbc
#teste 1

app = Dash(__name__, 
           external_stylesheets=['assets/main.css', dbc.themes.FLATLY],
           suppress_callback_exceptions=True)
