from Code.HistoricalData.HistoricalData import *

# Feature Selection
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

from verstack.stratified_continuous_split import scsplit

# AI Model
from sklearn.ensemble import RandomForestRegressor


class AIModel:
    def __init__(self):
        self.historical_data = HistoricalData()

        dataset = self.historical_data.original_dataset.copy()
        self.T_dataset = dataset.copy()
        self.AH_dataset = dataset.copy()
        self.RH_dataset = dataset.copy()
        self.model_dataset = dataset.copy()

        #self.T_normalise, self.T_scaling, self.T_train, self.T_test = self.train_test_data(self.T_dataset, 'T', 'delete', 'delete', 'lasso')
        #self.AH_normalise, self.AH_train, self.AH_test = self.train_test_data(self.AH_dataset, 'AH', 'delete', 'delete', 'none')
        #self.RH_normalise, self.RH_scaling, self.RH_train, self.RH_test = self.train_test_data(self.RH_dataset, 'RH', 'none', 'delete', 'lasso')

        # self.T_model = RandomForestRegressor(n_estimators=396, max_features=1.0, criterion='friedman_mse', max_depth=6,
        #                                     random_state=5, n_jobs=5)
        #self.T_model.fit(self.T_train.drop(['T'], axis=1), self.T_train['T'])

        #self.T_prediction = self.T_model.predict(self.T_test.drop(['T'], axis=1))

        #self.AH_model = RandomForestRegressor(n_estimators=487, max_features=1.0, criterion='squared_error', max_depth=6,
        #                                      random_state=5, n_jobs=5)
        #self.AH_model.fit(self.AH_train.drop(['AH'], axis=1), self.AH_train['AH'])
        #self.AH_prediction = self.AH_model.predict(self.AH_test.drop(['AH'], axis=1))

        #self.RH_model = RandomForestRegressor(n_estimators=265, max_features=1.0, criterion='friedman_mse', max_depth=6,
        #                                      random_state=5, n_jobs=5)
        #self.RH_model.fit(self.RH_train.drop(['RH'], axis=1), self.RH_train['RH'])
        #self.RH_prediction = self.RH_model.predict(self.RH_test.drop(['RH'], axis=1))

        #self.T_actual = self.T_test['T']
        #self.AH_actual = AH_test['AH']
        #self.RH_actual = RH_test['RH']

    def train_test_data(self, dataset, variable, outlier_method, null_method, scaling_method):
        normalise, train, test = self.data_preprocessing(dataset, variable)
        train, test = self.null_value(null_method, self.outliers(outlier_method, train), test)
        if scaling_method == 'lasso':
            scaling_model, train, test = self.feature_scaling(scaling_method, variable, train, test)
            return normalise, scaling_model, train, test
        elif scaling_method == 'none':
            train, test = self.feature_scaling(scaling_method, variable, train, test)
            return normalise, train, test

    @staticmethod
    def data_preprocessing(dataset, variable):
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
        q1 = dataset.quantile(0.25)
        q3 = dataset.quantile(0.75)
        iqr = q3 - q1
        factor = 1.5

        if method == 'none':
            return dataset

        elif method == 'delete':
            dataset = dataset[
                ~((dataset < (q1 - factor * iqr)) | (dataset > (q3 + factor * iqr))).any(axis=1)].reset_index(drop=True)
            return dataset

        else:
            print("No Outliers method found")

    # Method to deal with null values, data imputation
    @staticmethod
    def null_value(method, train_dataset, test_dataset):
        if method == "delete":
            train_dataset = train_dataset.dropna(axis=0, how='any').reset_index(drop=True)
            test_dataset = test_dataset.dropna(axis=0, how='any').reset_index(drop=True)

            return train_dataset, test_dataset
        else:
            print("No Imputation method found")

    # Feature Scaling Method
    @staticmethod
    def feature_scaling(method, variable, train_dataset, test_dataset):
        if method == 'none':
            return train_dataset, test_dataset

        elif method == 'lasso':
            features_name = []
            X_train = train_dataset.drop([variable], axis=1)
            features_list = list(X_train.columns)
            y_train = train_dataset[variable]

            X_test = test_dataset.drop([variable], axis=1)
            y_test = test_dataset[variable]

            # Lasso Model
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

            return scaling_model, train_dataset, test_dataset

        else:
            print("No Feature Scaling method found")


if __name__ == '__main__':
    model = AIModel()
