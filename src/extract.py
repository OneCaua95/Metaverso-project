import pandas as pd

file = 'data\Twitch_game_data.csv'

class Extractor:

    def get_data(self):
    
        data = pd.read_csv(file, encoding='latin-1')

        return data



#TESTE



