import pandas as pd

game = pd.read_csv(".../CSVs/games.csv")
recommend = pd.read_csv(".../CSVs/recommendations.csv")

recommend = recommend.drop(['review_id'], axis=1)


reduced_recommendations = recommend[recommend['app_id'].isin(game['app_id'])]

reduced_recommendations.to_csv('red_recommendations.csv', index= False)