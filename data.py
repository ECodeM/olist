import os
import pandas as pd

class Olist:
    def get_data(self):
        '''
        This functions rreturns a python dict with the each csv file transformed to a dataframe.
        It's keys are "sellers", "orders", "product", etc.
        It's values are the each corresponding dataframe.
        '''
        csv_path = "/Users/manucunha/desktop/Portfolio/olist/data"

        # Creating a list with the csv file names
        file_names = os.listdir(csv_path)

        key_names = []

        for item in file_names:
            key_names.append(item.replace("olist_", "").replace(".csv", "").replace("_dataset", ""))

        # Creating a dict with the csv names as keys and their own dataframes as values
        data = {}

        for (x,y) in zip(key_names, file_names):
            data[x] = pd.read_csv(os.path.join(csv_path, y))

        return data
