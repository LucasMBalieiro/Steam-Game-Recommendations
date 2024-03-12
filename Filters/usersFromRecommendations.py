import os
import pandas as pd

def create_users(): 

    current_directory = os.path.dirname(os.path.abspath(__file__))

    recommend_path = os.path.join(current_directory, 'red_recommendations.csv')
    users_path = os.path.join(current_directory, 'users.csv')

    users = pd.read_csv(users_path)
    recommend = pd.read_csv(recommend_path)


    reduced_users = users[users['user_id'].isin(recommend['user_id'])]


    reduced_users.to_csv('red_users.csv', index= False)


create_users()