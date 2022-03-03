from dash import Dash, html, dcc
#import plotly.express as px
#import pandas as pd

import notebook_importing

import dashapp as ds

app = Dash(__name__)
app.layout = ds.layout

if __name__ == '__main__':
    app.run_server(debug=True)

