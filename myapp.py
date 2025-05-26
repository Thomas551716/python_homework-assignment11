from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as data

app = Dash(__name__)
server = app.server  # For deployment

df = data.gapminder()
countries = df['country'].drop_duplicates().sort_values()

app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'
    ),
    dcc.Graph(id='gdp-growth')
])

@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap',
                  title=f'GDP Per Capita Over Time: {selected_country}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

