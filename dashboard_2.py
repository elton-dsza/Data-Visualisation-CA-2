import dash
from dash import html


dashboard_2_layout = html.Div([
    html.Link(rel='stylesheet', href='/assets/style.css'),
    html.Main(id='main', children=[
        html.A('Dashboard 1', className='link_2', href='/dashboard_1'),
        html.A('Dashboard 2', className='link_2', href='/dashboard_2'),
        html.A('About', className='link_2', href='/'),
        html.Iframe(src='/assets/d4.html', width='100%', height='600'),
        html.Iframe(src='/assets/d5.html', width='100%', height='600'),
        html.Iframe(src='/assets/d6.html', width='100%', height='600'),

    ])
])

