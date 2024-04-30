import dash
from dash import html, dcc
from dash.dependencies import Input, Output

from home import home_layout
from dashboard_1 import dashboard_1_layout
from dashboard_2 import dashboard_2_layout

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/home':
        return home_layout
    elif pathname == '/dashboard_1':
        return dashboard_1_layout
    elif pathname == '/dashboard_2':
        return dashboard_2_layout
    else:
        return html.Div([
            html.H3('404 - Page not found')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
