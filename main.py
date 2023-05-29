import pandas as pd
import question1 as q1


def main() -> None:
    game_sales = pd.read_csv('vgsales.csv')
    test = pd.read_csv('test.csv')
    q1.predict_in_2020(game_sales)
    q1.genre_trends(game_sales)
    q1.predict_in_2020(test)
    q1.genre_trends(test)


if __name__ == '__main__':
    main()