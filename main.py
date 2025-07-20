import dash
from dash import dcc, html
import plotly.express as px
import requests
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__)

# Fetch data for a given country
def get_country_data(country):
    url = f'https://disease.sh/v3/covid-19/countries/{country}'
    response = requests.get(url)
    return response.json()

# Layout for the dashboard
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[
            {'label': 'USA', 'value': 'USA'},
            {'label': 'India', 'value': 'India'},
            {'label': 'Brazil', 'value': 'Brazil'},
            {'label': 'Russia', 'value': 'Russia'}
        ],
        value='USA',
        style={'width': '50%'}
    ),
    dcc.Graph(id='covid-graph')
])

k = 4


# Callback to update the graph based on the selected country
@app.callback(
    dash.dependencies.Output('covid-graph', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    data = get_country_data(selected_country)
    country_data = {
        'Category': ['Cases', 'Deaths', 'Recovered'],
        'Count': [data['cases'], data['deaths'], data['recovered']]
    }
    df_plot = pd.DataFrame(country_data)
    
    # Plotly bar chart
    fig = px.bar(df_plot, x='Category', y='Count', title=f"COVID-19 Overview in {selected_country}")
    return fig

if __name__ == '__main__':
    app.run(debug=False, port = 8051)

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(debug=False)