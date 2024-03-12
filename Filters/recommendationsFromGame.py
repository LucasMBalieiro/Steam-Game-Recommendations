import os
import pandas as pd

def create_recommend(): 

    current_directory = os.path.dirname(os.path.abspath(__file__))

    game_path = os.path.join(current_directory, 'games.csv')
    recommend_path = os.path.join(current_directory, 'recommendations.csv')

    game = pd.read_csv(game_path)
    recommend = pd.read_csv(recommend_path, nrows=100000)

    recommend = recommend.drop(['review_id'], axis=1)


    reduced_recommendations = recommend[recommend['app_id'].isin(game['app_id'])]



    reduced_recommendations.to_csv('red_recommendations.csv', index= False)


create_recommend()