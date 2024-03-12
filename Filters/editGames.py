import os
import pandas as pd

def editGames():

    #read do arquivo
    current_directory = os.path.dirname(os.path.abspath(__file__))
    game_path = os.path.join(current_directory, 'CSVs/games.csv')
    game = pd.read_csv(game_path)

    #tem que converter true pra True e false pra False... é serio...
    colunas = ['win', 'mac', 'linux', 'steam_deck']
    for col in colunas:
        game[col] = game[col].replace({'true':1, 'false':0})

    game[colunas] = game[colunas].astype(int)

    game.to_csv(game_path, index=False)


editGames()