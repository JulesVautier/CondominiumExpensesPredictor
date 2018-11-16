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
        self.reIndex()
        self.hasTrainingSet = False
        self.isTrained = False
        self.trainResults = False
        pass

    def readData(self):
        print('read_data')
        self.df = self.pd.read_csv(self.data_path, nrows=100)

    def reIndex(self):
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

    def trainAll(self):
        self.createTrainSet()
        self.cleanDataSet()
        self.train()
        return "200"

    def createTrainSet(self):
        self.X = self.df[self.df.columns[:-1]]
        self.y = self.df[self.df.columns[-1]]

        print("\nFeature matrix:\n", self.X.head())
        print("\nResponse vector:\n", self.y.head())
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.4,
                                                                                random_state=1)

        # printing the shapes of the new X objects
        print(self.X_train.shape)
        print(self.X_test.shape)

        # printing the shapes of the new y objects
        print(self.y_train.shape)
        print(self.y_test.shape)
        self.hasTrainingSet = True
        self.isTrained = False
        return "200"

    def cleanDataSet(self):
        if self.hasTrainingSet is False:
            self.createTrainSet()
        from sklearn.preprocessing import Imputer
        # Create our imputer to replace missing values with the mean e.g.
        imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imp = imp.fit(self.X_train)
        self.X_train = imp.transform(self.X_train)
        imp = imp.fit(self.X_test)
        self.X_test = imp.transform(self.X_test)
        return "200"

    def train(self):
        if self.hasTrainingSet is False:
            self.createTrainSet()

        X_train = self.X_train
        X_test = self.X_test
        y_train = self.y_train
        y_test = self.y_test

        # training the model on training set
        from sklearn.neighbors import KNeighborsClassifier
        # TODO pourquoi KNN ? Je ne connais pas les différents models et leur spécificitées

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train, y_train)
        print(X_train, y_train)
        print(X_train.shape, y_train.shape)

        # # making predictions on the testing set
        y_pred = knn.predict(X_test)

        # comparing actual response values (y_test) with predicted response values (y_pred)
        from sklearn import metrics
        print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))

        # making prediction for out of sample data
        sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
        preds = knn.predict(sample)
        # self.pred_species = [iris.target_names[p] for p in preds]
        # print("Predictions:", pred_species)

        # saving the model
        from sklearn.externals import joblib
        joblib.dump(knn, './ressources/condimonium_knn.pkl')
        self.isTrained = True
        #TODO
        self.trainResults = "ok"
        return self.trainResults, "200"

    def isTrainedfct(self):
        if self.isTrained is False:
            return "False", "200"
        else:
            return self.isTrained, self.trainResults, "200"

    def getTrainResult(self):
        if self.isTrained is False:
            return "Not trained.", "401"
        else:
            return self.trainResults, "200"

    def predict(self, data):
        #TODO
        return "200"


dataHelper = DataHelper()
