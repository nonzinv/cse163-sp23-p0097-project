"""
CSE163 Final Project. Non Pronanun & Sirak Yohannes
May 23, 2023
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')
top_games = df.nlargest(10, 'Global_Sales')

plt.figure(figsize=(10, 6))
plt.bar(top_games['Name'], top_games['Global_Sales'], color='blue')

plt.xlabel('Game')
plt.ylabel('Global Sales (in millions)')
plt.title('Top 10 Games by Global Sales')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# problem 2


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')

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
