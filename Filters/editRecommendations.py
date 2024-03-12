import os
import pandas as pd

def edit_recommend(): 

    current_directory = os.path.dirname(os.path.abspath(__file__))
    recommend_path = os.path.join(current_directory, 'CSVs/red_recommendations.csv')

    recommend = pd.read_csv(recommend_path)

    recommend['is_recommended'] = recommend['is_recommended'].replace({True:1, False:0})


    recommend.to_csv(recommend_path, index= False)


edit_recommend()