import dash, plotly.express as px, pandas as pd
from dash import dcc, html


app = dash.Dash(__name__)


app.layout = html.Div([
        html.Label("Dropdown"),
        dcc.Dropdown(
            id="drop_1",
            options=[{'label':'Rio Grande do Sul', 'value':'RS'}, {'label':'São Paulo', 'value':'SP'}, {'label':'Paraná', 'value':'PR'}],
            value='RS',
            style={"margin-bottom":"25px"},
        ),
        html.Label("Checklist", style={"margin-top":"25px"}),
        dcc.Checklist(
            id="check_1",
            options=[{'label':'Rio Grande do Sul', 'value':'RS'}, {'label':'São Paulo', 'value':'SP'}, {'label':'Paraná', 'value':'PR'}],
            value=['RS'],
            style={"margin-bottom":"25px"},
        ),
        html.Label("Input", style={"margin-top":"25px"}),
        dcc.Input(
            id="inp_1",
            type="text",
            style={"margin-bottom":"25px"},
        ),
        html.Label("Slider", style={"margin-top":"25px"}),
        dcc.Slider(
            id="slider_1",
            min=0,
            max=9,
            marks={i:'Label {}'.format(i) if i == 1 else str(i) for i in range(1,6)},
            value=5,
        ),
])

if __name__ == "__main__":
    app.run_server(debug=True)