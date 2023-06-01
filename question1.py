"""
CSE163 Final Project. Non Pronanun & Sirak Yohannes
May 23, 2023
This file is responsible for research question 1, it contains the
algorithms behind each of the research questions -- to find how the
COVID19 pandemic affected video game sales and the market share of each
video game genres.
"""
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from plotly.subplots import make_subplots


"""
This method takes in a dataframe, it filters out the dataframes for
the number of sales and genres, then it will predict the number of
sales in 2020 and put that against the actual number of sales in 2020.
"""
def predict_in_2020(df):
    df = df[df['Year'] < 2015]
    df = df[['Global_Sales', 'NA_Sales', 'EU_Sales', 'Year', 'Genre']]
    agg_functions = {'Global_Sales': 'sum', 'NA_Sales': 'sum',
                     'EU_Sales': 'sum'}
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
    fig.add_scatter(x=[2020], y=[sales_2020[0]], mode='markers',
                    name='Predicted Sales in 2020')
    fig.add_scatter(x=[2020], y=[actual_sales_2020], mode='markers',
                    name='Actual Sales in 2020')
    fig.update_traces(marker=dict(size=8))
    fig.write_image("images/predict_2020.png")


"""
This method takes in the video game dataframe and it will plot the
statistics of sales by genre of video games between 2000 and 2015,
by 5 year intervals. The size of each of the pie charts are also
dependant on the number of sales in that year (smaller=less, etc.)
"""
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
    specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'},
                                                        {'type': 'domain'}]]
    fig = make_subplots(rows=2, cols=2, vertical_spacing=0.1,
                        horizontal_spacing=0.1, specs=specs,
                        subplot_titles=['2000', '2005', '2010', '2015'])
    fig.add_trace(go.Pie(labels=labels, values=values_2000,
                         scalegroup='one'), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=values_2010,
                         scalegroup='one'), 2, 1)
    fig.add_trace(go.Pie(labels=labels, values=values_2005,
                         scalegroup='one'), 1, 2)
    fig.add_trace(go.Pie(labels=labels, values=values_2015,
                         scalegroup='one'), 2, 2)
    fig.update_layout(title="Distribution of Video Game Genres (2000-2015)")
    fig.write_image("images/genre_trends.png")


def _file_test(df, year):
    df = df[df['Year'] == year]
    genres = df['Genre'].value_counts().to_dict()
    return genres



