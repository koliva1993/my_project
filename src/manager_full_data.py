import pandas as pd

class ManagerFullData:

    def read_csv(self):
        df= pd.read_csv('..\data\data.csv')
        print(df)

