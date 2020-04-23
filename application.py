# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import datagathering
import dash_bootstrap_components as dbc

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__)
application=app.server
app.scripts.config.serve_locally = False
app.title ="CoVID-19 Tracker"
app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})
#app.css.append_css({"external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"})

# All the actual data

@app.callback(
    [Output(component_id='graph', component_property='figure'),
     Output('piechart', 'figure'), ],
    [Input(component_id='input', component_property='value')]
)
def getDatapoints(countrycode):
    ccountry = countrycode
    casedict = datagathering.getDeathnewapi(ccountry)
    pielabels, pievalues = datagathering.pieDetails(ccountry)
    dates = list(casedict.keys())
    confirmed = list(casedict.values())
    figure = {
        'data': [
            {'x': dates, 'y': confirmed, 'type': 'bar',
             'name': 'Confirmed Cases'},
        ],
        'layout': {
            'title': 'Confirmed Covid-19 Cases : '+str(ccountry).upper()
        }
    }
    colors = ['rgb(55, 83, 109)', 'indianred', 'green']
    piefig = go.Figure(data=[go.Pie(labels=pielabels, values=pievalues, hole=.5, textinfo='label+value',
                                    hoverinfo='percent', marker=dict(colors=colors))],
                                    layout= {'title': 'Total Cases: '+str(ccountry).upper()})
    #piefig=go.Pie(labels=pielabels, values=pievalues, hole=.5,textinfo='value',hoverinfo='label+value')
    # ret=[figure,piefig]
    return figure, piefig

jumbotron = dbc.Jumbotron(
    [
        html.H1("Covid-19 Tracker WorldWide", className="display-3"),
        html.Hr(className="my-3"),
        #html.P(
            #"This Dashboard uses data from openAPIs to tell you about the pandemic of Covid-19"
        #),
        #html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ]
)

app.layout = html.Div(children=[

    html.Div(
        [
            html.H1(children=jumbotron),
        ], className="twelve columns"),

    html.Div(
        [
            html.Div(children='''
        All Data is being pulled from Johns Hopkins University Database
    '''),
        ], className="twelve columns"),

    html.Div(
        [

        ], className="twelve columns"),


    html.Div(
        [

    html.Div([html.Label('Choose Your Country:'),
              dcc.Dropdown(
        id="input",
        options=[
            {'label': u'USA', 'value': 'united-states'},
            {'label': 'Canada', 'value': 'canada'},
            {'label': 'India', 'value': 'india'},
            {'label': 'United Kingdom', 'value': 'united-kingdom'},
            {'label': 'Spain', 'value': 'spain'},
            {'label': 'Italy', 'value': 'italy'},
            {'label': 'Germany', 'value': 'germany'},
            {'label': 'Belgium', 'value': 'belgium'},
            {'label': 'Netherlands', 'value': 'netherlands'},
            {'label': 'France', 'value': 'france'},
            {'label': 'Mexico', 'value': 'mexico'},
            {'label': 'China - Mainland', 'value': 'china'},
            {'label': 'Japan', 'value': 'japan'},

        ],
        value='united-states'
    )], className="two columns"),
    ], className="twelve columns"),

    html.Div(
        [

            html.Div([
                dcc.Graph(
                    id='graph'
                )], className="six columns"),

            html.Div([
                dcc.Graph(
                    id='piechart'
                )], className="six columns"),

        ]),


])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
