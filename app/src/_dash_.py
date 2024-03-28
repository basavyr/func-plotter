

from dash import Dash, html, dcc,  Input, Output, callback
import plotly.express as px
import pandas as pd
import numpy as np

import data_fourier


app = Dash(__name__)


gamma_step = 0.1
gamma_values = data_fourier.generate_gamma_values(0, 5, gamma_step)
omega_step = 5
omega_values = data_fourier.generate_omega_values(0, 100, omega_step)

app.layout = html.Div([
    html.Div(id="gamma-value"),
    html.Br(),
    dcc.Slider(min=gamma_values[0], max=gamma_values[-1], step=gamma_step, value=gamma_values[0], id='gamma-slider',
               tooltip={"placement": "bottom", "always_visible": False}),
    html.Div(id="omega-value"),
    html.Br(),
    dcc.Slider(min=omega_values[0], max=omega_values[-1], step=omega_step, value=omega_values[0], id='omega-slider',
               tooltip={"placement": "bottom", "always_visible": False}),
    html.Br(),
    html.Div(children=data_fourier.HEADER),
    html.Br(),
    dcc.Graph(id='graph-ud')
])


@callback(Output('gamma-value', 'children'),
          Input('gamma-slider', 'value'))
def set_gamma(value):
    return f'Select the value of gamma. Current value: {value}$'


@callback(Output('omega-value', 'children'),
          Input('omega-slider', 'value'))
def set_omega(value):
    return f'Select the value of omega. Current value: {value}$'


@callback(
    Output('graph-ud', 'figure'),
    Input('gamma-slider', 'value'),
    Input('omega-slider', 'value'))
def update_ud(gamma, omega):
    df = data_fourier.generate_ud_df(gamma, omega)

    fig = px.line(df, x=df.t, y=df.ud, labels={'x': 't', 'ud': 'ud(t)'})
    fig2 = px.scatter(df, x=df.t, y=df.ud, labels={'x': 't', 'ud': 'ud(t)'})

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run(debug=True)
