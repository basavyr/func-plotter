

from dash import Dash, html, dcc,  Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

import data_fourier


app = Dash(__name__)


gamma_step = 0.1
omega_step = 5

gamma_values = data_fourier.generate_gamma_values(0, 5, gamma_step)
omega_values = data_fourier.generate_omega_values(0, 100, omega_step)

app.layout = html.Div([
    html.Div(id="gamma-value"),
    html.Br(),
    dcc.Slider(min=gamma_values[0], max=gamma_values[-1], step=gamma_step, value=gamma_values[int(len(gamma_values)/2)], id='gamma-slider',
               tooltip={"placement": "bottom", "always_visible": False}),
    html.Div(id="omega-value"),
    html.Br(),
    dcc.Slider(min=omega_values[0], max=omega_values[-1], step=omega_step, value=omega_values[int(len(omega_values)/2)], id='omega-slider',
               tooltip={"placement": "bottom", "always_visible": False}),
    html.Br(),
    html.Div(children=data_fourier.HEADER),
    html.Br(),
    dcc.Graph(id='graph-ud')
])


@callback(Output('gamma-value', 'children'),
          Input('gamma-slider', 'value'))
def set_gamma(value):
    return f'Select the value of ɣ. Current value: ɣ={value}'


@callback(Output('omega-value', 'children'),
          Input('omega-slider', 'value'))
def set_omega(value):
    return f'Select the value of ω. Current value: ω={value}'


@callback(
    Output('graph-ud', 'figure'),
    Input('gamma-slider', 'value'),
    Input('omega-slider', 'value'))
def update_ud_plot(gamma, omega):
    df_line = data_fourier.generate_ud_df(1500, gamma, omega).th
    df_scatter = data_fourier.generate_ud_df(100, gamma, omega).exp

    # line_plot = px.line(df_line, x=df_line.t, y=df_line.ud,
    #                     color_discrete_sequence=['black'])
    # scatter_plot = px.scatter(
    #     df_scatter, x=df_scatter.t, y=df_scatter.ud, color_discrete_sequence=['red'])

    # go_fig = go.Figure(data=line_plot.data + scatter_plot.data)

    # go_fig.update_layout(transition_duration=500,
    #                      title="Under-damped oscillator",
    #                      xaxis_title="t",
    #                      yaxis_title="ud(t)",
    #                      legend_title="Under-damped oscillator"
    #                      )

    # return go_fig

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_scatter.t, y=df_scatter.ud,
        name="Name of Trace 1"
    ))
    fig.add_trace(go.Line(
        x=df_line.t, y=df_line.ud,
        name="Name of Trace 1"
    ))

    fig.update_layout(
        title="Plot Title",
        xaxis_title="X Axis Title",
        yaxis_title="Y Axis Title",
        legend_title="Legend Title"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
