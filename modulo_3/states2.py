from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='inp1',type='text', value='deschamps'),
    dcc.Input(id='inp2',type='text', value='contabilidade'),
    html.Button(id='submitBtnState', children='submit'),
    html.Div(id='numberOut'),
])



@app.callback(
    Output('numberOut','children'),
    Input('submitBtnState','n_clicks'),
    State('inp1','value'), # os valores s serao atuallizados quando o cliente clicar no btn
    State('inp2','value'),
)
def updateValues(n_clicks,inp1, inp2):
    return u'inp 1 is "{}" and inp 2 is "{}".'.format(inp1,inp2)

if __name__ == '__main__':
    app.run_server(debug=True)
