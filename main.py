"""
CSE163 Final Project. Non Pronanun & Sirak Yohannes
May 28, 2023
This is the executable file that contains all the analysis
and research questions that we were trying to answer, it is the one
that reads the csv files.
"""
import pandas as pd
import question1 as q1


def main() -> None:
    game_sales = pd.read_csv('vgsales.csv')
    test = pd.read_csv('test.csv')
    q1.predict_in_2020(game_sales)
    q1.genre_trends(game_sales)


if __name__ == '__main__':
    main()