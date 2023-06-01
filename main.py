"""
CSE163 Final Project. Non Pronanun & Sirak Yohannes
May 28, 2023
This is the executable file that contains all the analysis
and research questions that we were trying to answer, it is the one
that reads the csv files.
"""
import pandas as pd
import question1 as q1
import question2 as q2
from cse163_utils import assert_equals


def main() -> None:
    game_sales = pd.read_csv('vgsales.csv')
    test = pd.read_csv('test.csv')
    q1.predict_in_2020(game_sales)
    q1.genre_trends(game_sales)
    q2.get_most_popular_video_game_genres(game_sales)
    q2.get_covid_impact_on_video_game_sales_and_popularity_by_genre(game_sales)
    assert_equals({'Shooter': 3, 'Sports': 1, 'Role-Playing': 1}, q1._file_test(test, 2015))
    assert_equals({'Role-Playing': 1}, q1._file_test(test, 2000))


if __name__ == '__main__':
    main()