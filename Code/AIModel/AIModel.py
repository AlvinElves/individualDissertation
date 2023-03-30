from Code.HistoricalData.HistoricalData import *

# Feature Selection
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

from verstack.stratified_continuous_split import scsplit

# AI Model
from sklearn.ensemble import RandomForestRegressor


class AIModel:
    """
    AIModel Class to be imported into GUI files. This class contains all the AI (RandomForestRegressor) Model functions that can
    be called for prediction and model visualise in the GUI file easily.
    """
    def __init__(self):
        """
        AIModel Class Constructor that calls the Historical Data Class and creates the all the AI Model and training, testing dataset.
        """
        self.historical_data = HistoricalData()

        dataset = self.historical_data.original_dataset.copy()

        self.T_dataset = dataset.copy()
        self.AH_dataset = dataset.copy()
        self.RH_dataset = dataset.copy()
        self.model_dataset = dataset.copy()

        # Get the training and testing dataset
        self.T_normalise, self.T_scaling, self.T_features, self.T_train, self.T_test = self.train_test_data(self.T_dataset, 'T', 'delete', 'delete', 'lasso')
        self.AH_normalise, self.AH_train, self.AH_test = self.train_test_data(self.AH_dataset, 'AH', 'delete', 'delete', 'none')
        self.RH_normalise, self.RH_scaling, self.RH_features, self.RH_train, self.RH_test = self.train_test_data(self.RH_dataset, 'RH', 'none', 'delete', 'lasso')

        # Create the AI Model for all dependent features
        self.T_model = RandomForestRegressor(n_estimators=20, max_features=1.0, criterion='friedman_mse', max_depth=6,
                                             random_state=5, n_jobs=5)
        self.T_model.fit(self.T_train.drop(['T'], axis=1), self.T_train['T'])

        self.AH_model = RandomForestRegressor(n_estimators=20, max_features=1.0, criterion='squared_error', max_depth=6,
                                              random_state=5, n_jobs=5)
        self.AH_model.fit(self.AH_train.drop(['AH'], axis=1), self.AH_train['AH'])

        self.RH_model = RandomForestRegressor(n_estimators=20, max_features=1.0, criterion='friedman_mse', max_depth=6,
                                              random_state=5, n_jobs=5)
        self.RH_model.fit(self.RH_train.drop(['RH'], axis=1), self.RH_train['RH'])

        # Predict the testing dataset
        self.T_prediction = self.T_model.predict(self.T_test.drop(['T'], axis=1))
        self.AH_prediction = self.AH_model.predict(self.AH_test.drop(['AH'], axis=1))
        self.RH_prediction = self.RH_model.predict(self.RH_test.drop(['RH'], axis=1))

        # Get the actual result from testing dataset
        self.T_actual = self.T_test['T']
        self.AH_actual = self.AH_test['AH']
        self.RH_actual = self.RH_test['RH']

    def train_test_data(self, dataset, variable, outlier_method, null_method, scaling_method):
        """
        A function that is used to split the dataset into training and testing data.
        :param dataset: The dataset that is used for the AI Model
        :param variable: The dependent variable that want to be split for the AI Model
        :param outlier_method: The method that deals with outlier which has been chosen in the AIModelComparison file
        :param null_method: The method that deals with null value which has been chosen in the AIModelComparison file
        :param scaling_method: The method that does feature scaling which has been chosen in the AIModelComparison file
        :return: A normaliser that is used during normalisation and scaling model which is used for feature scaling, in addition to
        training and testing dataset that has been split
        """
        # Data preprocess and feature scaling the dataset
        normalise, train, test = self.data_preprocessing(dataset, variable)
        train, test = self.null_value(null_method, self.outliers(outlier_method, train), test)
        if scaling_method == 'lasso':
            scaling_model, features_name, train, test = self.feature_scaling(scaling_method, variable, train, test)
            return normalise, scaling_model, features_name, train, test
        elif scaling_method == 'none':
            train, test = self.feature_scaling(scaling_method, variable, train, test)
            return normalise, train, test

    @staticmethod
    def data_preprocessing(dataset, variable):
        """
        A function that is used to drop the unwanted column and do normalisation on the dataset
        :param dataset: The dataset that is used for the AI Model
        :param variable: The dependent variable that want to be split for the AI Model
        :return: A normaliser that is used during normalisation, in addition to training and testing dataset that has been split
        """
        # Change the value with -200 (Null value) to nan value and drop the dependent ones
        dataset[dataset == -200] = np.NaN
        dataset = dataset.dropna(subset=['T']).reset_index(drop=True)

        # Split the dataframe to X and Y variables
        X = dataset.drop(['Date', 'Time', 'T', 'RH', 'AH'], axis=1)
        Y = dataset[variable]

        # Split the data into train, test (80%, 20%)
        Xs_train, Xs_test, y_train, y_test = scsplit(X, Y, stratify=Y, test_size=0.2, random_state=5, continuous=True)
        Xs_train.reset_index(inplace=True, drop=True)
        y_train.reset_index(inplace=True, drop=True)
        Xs_test.reset_index(inplace=True, drop=True)
        y_test.reset_index(inplace=True, drop=True)

        # Normalise the training dataset
        features_list = list(Xs_train.columns)
        scaler = StandardScaler()
        scaler.fit(Xs_train)

        Xs_train_norm = scaler.transform(Xs_train)
        Xs_train = pd.DataFrame(Xs_train_norm, columns=features_list)
        train_dataset = pd.concat([y_train, Xs_train], axis=1)

        # Use the settings for training dataset to normalise testing dataset too
        Xs_test_norm = scaler.transform(Xs_test)
        Xs_test = pd.DataFrame(Xs_test_norm, columns=features_list)
        test_dataset = pd.concat([y_test, Xs_test], axis=1)

        train_df = train_dataset.drop(['NMHC(GT)'], axis=1)
        test_df = test_dataset.drop(['NMHC(GT)'], axis=1)

        return scaler, train_df, test_df

    # Method to deal with outliers
    @staticmethod
    def outliers(method, dataset):
        """
        A function that is used to deal with the outliers value on the dataset
        :param method: The method that deals with outlier which has been chosen by AIModelComparison file
        :param dataset: The dataset that is used for the AI Model
        :return: A dataset that is from the function parameter, which the outliers value has been dealt with based on the method chosen
        """
        # Get the quantile of the dataset
        q1 = dataset.quantile(0.25)
        q3 = dataset.quantile(0.75)
        iqr = q3 - q1
        factor = 1.5

        if method == 'none':
            return dataset

        elif method == 'delete':
            # Drop the dataset that is bigger than the upper quantile or smaller than the lower quantile
            dataset = dataset[
                ~((dataset < (q1 - factor * iqr)) | (dataset > (q3 + factor * iqr))).any(axis=1)].reset_index(drop=True)
            return dataset

        else:
            print("No Outliers method found")

    # Method to deal with null values, data imputation
    @staticmethod
    def null_value(method, train_dataset, test_dataset):
        """
        A function that is used to deal with the null value on the training and testing dataset
        :param method: The method that deals with null value which has been chosen by AIModelComparison file
        :param train_dataset: The training dataset that is used to train the AI Model
        :param test_dataset: The testing dataset that is used to test the AI Model
        :return: A training and testing dataset that are from the function parameter, which the null value has been dealt with
        based on the method chosen
        """
        if method == "delete":
            # Drop the rows with null value
            train_dataset = train_dataset.dropna(axis=0, how='any').reset_index(drop=True)
            test_dataset = test_dataset.dropna(axis=0, how='any').reset_index(drop=True)

            return train_dataset, test_dataset
        else:
            print("No Imputation method found")

    # Feature Scaling Method
    @staticmethod
    def feature_scaling(method, variable, train_dataset, test_dataset):
        """
        A function that does feature scaling on the training and testing dataset
        :param method: The method that does feature scaling which has been chosen in the AIModelComparison file
        :param variable: The dependent variable that want to be split for the AI Model
        :param train_dataset: The training dataset that is used to train the AI Model
        :param test_dataset: The testing dataset that is used to test the AI Model
        :return: A scaling model which is used for feature scaling, in addition to training and testing dataset that have been dealt
        with based on the method chosen
        """
        if method == 'none':
            return train_dataset, test_dataset

        elif method == 'lasso':
            features_name = []
            X_train = train_dataset.drop([variable], axis=1)
            features_list = list(X_train.columns)
            y_train = train_dataset[variable]

            X_test = test_dataset.drop([variable], axis=1)
            y_test = test_dataset[variable]

            # Lasso Model that scales the features for training and testing dataset
            lasso = linear_model.Lasso(max_iter=50, random_state=5, alpha=0.1).fit(X_train, y_train.values)
            scaling_model = SelectFromModel(lasso, prefit=True)
            features_output = scaling_model.get_support(indices=True)
            train_dataset = scaling_model.transform(X_train)

            # Use setting from training set
            test_dataset = scaling_model.transform(X_test)

            for i in features_output:
                features_name.append(features_list[i])

            X_train = pd.DataFrame(train_dataset, columns=features_name)
            X_test = pd.DataFrame(test_dataset, columns=features_name)

            train_dataset = pd.concat([y_train, X_train], axis=1)
            test_dataset = pd.concat([y_test, X_test], axis=1)

            return scaling_model, features_name, train_dataset, test_dataset

        else:
            print("No Feature Scaling method found")


if __name__ == '__main__':
    model = AIModel()
