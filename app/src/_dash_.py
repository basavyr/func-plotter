

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

import data_fourier


app = Dash(__name__)


df = data_fourier.df

fig1 = px.scatter(df, x=df.t, y=df.ud, labels={'x': 't', 'ud': 'ud(t)'})
fig2 = px.line(df, x=df.t, y=df.ud, labels={'x': 't', 'ud': 'ud(t)'})


app.layout = html.Div([
    html.Div(children='Please select the value of \gamma'),
    html.Br(),
    dcc.Dropdown(data_fourier.gamma, 'gamma',
                 id='dropdown-gamma', placeholder='gamma'),
    html.Div(children='Please select the value of $\omega_0$'),
    html.Br(),
    dcc.Dropdown(data_fourier.omega0,  id='dropdown-omega',
                 placeholder='omega'),
    html.Div(children=data_fourier.HEADER),
    html.Br(),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run(debug=True)
