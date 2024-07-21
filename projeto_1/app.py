import dash, plotly.express as px, pandas as pd
from dash import html, dcc


app = dash.Dash(__name__)

df = pd.DataFrame({
    "FRUTAS":["MAÇÃS","PÊRAS","LARANJAS"],
    "QTD":[2,6,7],
    "CIDADE":["BLUMENAU","INDAIAL","POMERODE"]
})

fig = px.bar(df,x="FRUTAS", y="QTD", color="CIDADE") #Transformando o DF em uma FIG


app.layout = html.Div(id="main_div",style={"color":"RED"},
    children=[
        html.H1("Hello dash", id="titulo"),
        html.Div("Dash: Um framework web pra .py"),
        dcc.Graph(id="main_graph", figure=fig)
    ],
)

if __name__ == "__main__":
    app.run_server(debug= True)