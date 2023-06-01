"""
CSE163 Final Project
Authors: Non Pronanun & Sirak Yohannes
Date: May 23, 2023

Description:
This file contains the implementation of research question 1 for the CSE163 Final Project. The goal of the project is to investigate how the COVID-19 pandemic has impacted video game sales and the market share of different video game genres.

Methods:
- predict_in_2020(df): Predicts the number of video game sales in 2020 and compares it with the actual sales. Generates a scatter plot.
- genre_trends(df): Plots the sales statistics of video game genres between 2000 and 2015 using pie charts.

Imports:
- pandas
- matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_covid_impact_on_video_game_sales_and_popularity_by_genre(df):
    """
    This method takes in a dataframe and analyzes the impact of the COVID-19 pandemic on video game sales
    and popularity by genre. It identifies the top 10 games based on global sales and creates a bar chart
    to visualize their sales figures.

    Parameters:
        - df (pandas.DataFrame): The input dataframe containing video game data.

    Returns:
        None
    """
    top_games = df.nlargest(10, 'Global_Sales')

    plt.figure(figsize=(10, 6))
    plt.bar(top_games['Name'], top_games['Global_Sales'], color='blue')

    plt.xlabel('Game')
    plt.ylabel('Global Sales (in millions)')
    plt.title('Top 10 Games by Global Sales')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def get_most_popular_video_game_genres(df):
    """
    This method takes in a dataframe and analyzes the popularity of specific video game genres over time.
    It groups the data by genre and year, calculates the sum of global sales for each genre, and creates
    a line plot to visualize the sales trends.

    Parameters:
        - df (pandas.DataFrame): The input dataframe containing video game data.

    Returns:
        None
    """
    genre_sales = df.groupby(['Genre', 'Year'])['Global_Sales'].sum().reset_index()

    pivot_genre_sales = genre_sales.pivot(index='Year', columns='Genre', values='Global_Sales')

    selected_genres = ['Action', 'Sports', 'Role-Playing', 'Shooter']

    selected_genre_sales = pivot_genre_sales[selected_genres]

    plt.figure(figsize=(10, 6))
    for genre in selected_genres:
        plt.plot(selected_genre_sales.index, selected_genre_sales[genre], label=genre)
    plt.xlabel('Year')
    plt.ylabel('Global Sales (in millions)')
    plt.title('Popularity of Specific Video Game Genres Over Time')

    plt.legend()

    plt.tight_layout()
    plt.show()
