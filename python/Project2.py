pip install dash plotly pandas

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 12]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash Example"),
    dcc.Graph(id='bar-chart'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': category, 'value': category}
            for category in data['Category']
        ],
        value=data['Category'][0]
    )
])

@app.callback(
    Output('bar-chart', 'figure'),
    Input('category-dropdown', 'value')
)
def update_bar_chart(selected_category):
    filtered_data = data[data['Category'] == selected_category]
    fig = px.bar(filtered_data, x='Category', y='Value', title=f'Bar Chart for Category {selected_category}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
