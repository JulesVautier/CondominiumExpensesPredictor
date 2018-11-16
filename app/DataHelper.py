import pandas as pd

DATA_PATH = './ressources/dataset_annonces.csv'


def check(func):
    def wrapper(self, id):
        try:
            self.df.loc[id]
        except:
            return 401
        return func(self, id)

    return wrapper


class DataHelper:

    def __init__(self, data_path=DATA_PATH):
        # reading csv file
        self.data_path = data_path
        self.pd = pd
        self.readData()
        self.cleanData()
        pass

    def readData(self):
        print('read_data')
        self.df = self.pd.read_csv(self.data_path, nrows=100)

    def cleanData(self):
        # self.df.drop(['ID'], inplace=True, axis=1)
        self.df['ID'] = self.df.index

    def toJson(self, data):
        return data.to_json()

    def getDataFrame(self):
        return self.df

    def getDatas(self, limite_one, limite_two):
        return self.toJson(self.df.loc[limite_one:limite_two])

    @check
    def getData(self, id):
        return self.toJson(self.df.loc[id])

    @check
    def deleteData(self, id):
        self.df.drop(id, inplace=True)
        return 200

    def postData(self, data):
        series = self.pd.Series(data)
        try:
            self.df.append(series, ignore_index=True)
            return "201"
        except:
            return "501"

dataHelper = DataHelper()
