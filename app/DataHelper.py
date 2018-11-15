import pandas as pd

DATA_PATH = './ressources/dataset_annonces.csv'


class DataHelper:

    def __init__(self, data_path=DATA_PATH):
        # reading csv file
        self.data_path = data_path
        self.pd = pd
        self.readData()
        pass

    def readData(self):
        self.df = self.pd.read_csv(self.data_path, nrows=2)

    def getDataFrame(self):
        return self.df

    def getDatas(self):
        return self.df

    def getData(self, id):
        return self.df.loc[[id]]

dataHelper = DataHelper()