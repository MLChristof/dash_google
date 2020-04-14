import dash
import dash_core_components as dcc
import dash_html_components as html

dash_app = dash.Dash()
app = dash_app.server

dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        This is Dash running on Google App Engine.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [5, 4, 3], 'type': 'bar', 'name': 'Jelle'},
                {'x': [1, 2, 3], 'y': [6, 1, 2], 'type': 'bar', 'name': u'Christof'},
            ],
            'layout': {
                'title': 'Hoeveel broodjes zijn er gegeten?'
            }
        }
    )
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)