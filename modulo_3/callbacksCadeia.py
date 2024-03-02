from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

allOptions = {
    'USA':['NY','SF','OR'],
    'Canada':['MN','TR','OT']
}

app.layout = html.Div([
    dcc.RadioItems(list(allOptions.keys()), 'USA', id='countries'),
    html.Hr(),
    dcc.RadioItems(id='cities'),                
    html.Hr(),

    html.Div(
        id='selectedValues'
    )
])





@app.callback(
    Output('cities','options'),
    Input('countries','value')
)
def setCities(selectedCountrie):
    return [{'label': i,'value':i} for i in allOptions[selectedCountrie]]


@app.callback(
    Output('cities','value'),
    Input('cities','options'),
)
def setCities(availableOptions):
    return availableOptions[0]['value']


@app.callback(
    Output('selectedValues','children'),
    Input('countries','value'),
    Input('cities','value'),
)
def setDisplayValues(selectedCountry, selectedCity):
    return u'{} is a city in {}'.format(selectedCity,selectedCountry)



if __name__ == '__main__':
    app.run_server(debug=True)


