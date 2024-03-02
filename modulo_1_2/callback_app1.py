import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Altere o valor abaixo para ver o callback em acao!"),
    html.Div(["Entrada",
        dcc.Input(id='myInp', value="val_Ini", type="text")]),
    html.Br(),
    html.Div(id="myOut")
])



@app.callback(
    Output(component_id="myOut", component_property="children"), #saida
    [Input(component_id="myInp", component_property="value")], #saida
    []  #State
    
)
def updateOutputDiv(value):
    return "Saida: {}".format(value)

if __name__ == "__main__":
    app.run_server(debug=True)