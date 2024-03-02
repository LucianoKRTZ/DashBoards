import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__) # Instaciacao obrigatoria


app.layout = html.Div(
    children=[
        html.Label("Dropdown"),
        dcc.Dropdown(
            id="dp-1",
            options=[
                {'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'Santa Catarina', 'value':'SC'},
                {'label':'Parana', 'value':'PR'}
                ],
            value="RS", style={"margin-bottom":"25px"}

        ),
        html.Label("Checklist"),
        dcc.Checklist(
            id="cl-1",
            options=[
                {'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'Santa Catarina', 'value':'SC'},
                {'label':'Parana', 'value':'PR'}
                ],
            value=["RS"], style={"margin-bottom":"25px"}

        ),
        
        html.Label("Input"),
        dcc.Input(value='SP',type='text'),


        html.Label("Slider"),
        dcc.Slider(
            min=0,
            max=9,
            marks={i:'Label {}'.format(i) if(i==1) else str(i) for i in range(1,6)}, # 'dicionario' do Slider
            value=5, #Valor de inicio
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)