import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from plotly.subplots import make_subplots



def predict_in_2020(df):
    df = df[df['Year'] < 2015]
    df = df[['Global_Sales', 'NA_Sales', 'EU_Sales', 'Year', 'Genre']]
    agg_functions = {'Global_Sales': 'sum', 'NA_Sales': 'sum', 'EU_Sales': 'sum'}
    df = df.groupby(['Year', 'Genre']).aggregate(agg_functions).reset_index()

    model = LinearRegression()
    model.fit(df[['Year']], df['Global_Sales'])

    sales_2020 = model.predict([[2020]])
    actual_sales_2020 = 140.4

    fig = px.scatter(df, x='Year', y='Global_Sales', opacity=0.65,
                     trendline='ols', trendline_color_override='green',
                     labels={
                         'Global_Sales' : 'Sales in Millions',
                     },
                     title="Are Video Game Sales Affected by the Pandemic?")
    fig.add_scatter(x=[2020], y=[sales_2020[0]], mode='markers', name='Predicted Sales in 2020')
    fig.add_scatter(x=[2020], y=[actual_sales_2020], mode='markers', name='Actual Sales in 2020')
    fig.update_traces(marker=dict(size=8))
    fig.write_image("images/predict_2020.png")

def genre_trends(df):
    df = df[['Genre', 'Year', 'Global_Sales']]
    data_2000 = df[df['Year'] == 2000]
    data_2010 = df[df['Year'] == 2010]
    data_2005 = df[df['Year'] == 2005]
    data_2015 = df[df['Year'] == 2015]
    labels = df['Genre']
    values_2000 = data_2000['Global_Sales']
    values_2010 = data_2010['Global_Sales']
    values_2005 = data_2005['Global_Sales']
    values_2015 = data_2015['Global_Sales']
    specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
    fig = make_subplots(rows=2, cols=2, vertical_spacing=0.1, horizontal_spacing=0.1,
                        specs=specs, subplot_titles=['2000', '2005', '2010', '2015'])
    fig.add_trace(go.Pie(labels=labels, values=values_2000, scalegroup='one'), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=values_2010, scalegroup='one'), 2, 1)
    fig.add_trace(go.Pie(labels=labels, values=values_2005, scalegroup='one'), 1, 2)
    fig.add_trace(go.Pie(labels=labels, values=values_2015, scalegroup='one'), 2, 2)
    fig.update_layout(title="Distribution of Video Game Genres between 2000 and 2015 \
                      <br><sup>The size of the charts represents the relative volume of sales</sup>")

    fig.write_image("images/genre_trends.png")


def main() -> None:
    game_sales = pd.read_csv('vgsales.csv')
    predict_in_2020(game_sales)
    genre_trends(game_sales)

if __name__ == '__main__':
    main()
