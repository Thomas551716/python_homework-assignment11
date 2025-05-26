import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load dataset
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

# Clean 'strength'
df['strength'] = df['strength'].str.replace('[^\d.]', '', regex=True).astype(float)

# Scatter plot
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title='Wind Strength vs Frequency')
fig.write_html('wind.html')
fig.show()