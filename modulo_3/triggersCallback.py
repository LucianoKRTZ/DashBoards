from dash import Dash, dcc, html, callback_context # callback_context possibilita obter a info de qual botao foi clicado
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Button('btn1', id='btn1'),
    html.Button('btn2', id='btn2'),
    html.Button('btn3', id='btn3'),
    html.Div(id='containerExemplo'),
])

@app.callback(
    Output('containerExemplo','children'),
    Input('btn1','n_clicks'),
    Input('btn2','n_clicks'),
    Input('btn3','n_clicks'),
)
def display(btn1,btn2,btn3):
 #   import pdb
 #   pdb.set_trace()
    id_triggered = callback_context.triggered[0]['prop_id'].split('.')[0] # Obtem o ID do botao clicado, pode-se usar essa variavel para validacoes de processos futuros
    return id_triggered

if __name__ == '__main__':
    app.run_server(debug=True)