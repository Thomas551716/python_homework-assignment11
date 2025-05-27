from dash import Dash, dcc, html, Input, Output

import plotly.express as px

import pandas as pd



# Sample dataset (replace this with your actual CSV if needed)

df = pd.DataFrame({

    "Category": ["A", "B", "C", "D"],

    "Value": [100, 200, 300, 400]

})



# Create Dash app

app = Dash(__name__)

server = app.server  # This is important for Render!



# Layout

app.layout = html.Div([

    html.H1("Simple Dash App"),

    dcc.Dropdown(

        id='category-dropdown',

        options=[{'label': cat, 'value': cat} for cat in df["Category"]],

        value='A'

    ),

    dcc.Graph(id='bar-plot')

])



# Callback to update graph

@app.callback(

    Output('bar-plot', 'figure'),

    Input('category-dropdown', 'value')

)

def update_graph(selected_category):

    filtered_df = df[df["Category"] == selected_category]

    fig = px.bar(filtered_df, x="Category", y="Value", title=f"Category {selected_category}")

    return fig



# Run locally (for testing)

if __name__ == '__main__':

    app.run_server(debug=True)

