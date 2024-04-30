
from dash import html, dcc, callback_context


home_layout = html.Div([
    html.Link(rel='stylesheet', href='/assets/style.css'),
    html.Main(id='main', children=[
        html.H1(className='data-viz-header', children='Data Visualization CA2'),
        html.P(className='author-header', children=[
            'Elton Grivith D\'Souza | D00264329',
            html.P(children=[
                html.A('Dashboard 1',className='link', href='/dashboard_1'),
                html.A('Dashboard 2',className='link', href='/dashboard_2'),
                html.A('About',className='link', href='/')
            ])
        ])
    ])
])
