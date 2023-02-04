import pandas as pd
import numpy as np

# Feature Selection
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

# AI Models
from sklearn.ensemble import RandomForestRegressor


class AIModel:
    def __init__(self):
        self.dataset = None
        self.get_data_from_excel()
        T_dataset = self.feature_scaling('lasso', self.null_value('delete', self.outliers('delete', self.data_preprocessing('T'))), 'T')
        AH_dataset = self.feature_scaling('lasso', self.null_value('delete', self.outliers('delete', self.data_preprocessing('AH'))), 'AH')
        RH_dataset = self.feature_scaling('lasso', self.null_value('delete', self.outliers('none', self.data_preprocessing('RH'))), 'RH')

        self.T_model = RandomForestRegressor(n_estimators=242, max_features='log2', criterion='friedman_mse',
                                             random_state=5, n_jobs=5)
        self.T_model.fit(T_dataset.drop(['T'], axis=1), T_dataset['T'])

        self.RH_model = RandomForestRegressor(n_estimators=487, max_features='auto', criterion='friedman_mse',
                                              random_state=5, n_jobs=5)
        self.RH_model.fit(RH_dataset.drop(['RH'], axis=1), RH_dataset['RH'])

    def get_data_from_excel(self):
        self.dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")

        self.dataset[self.dataset == -200] = np.NaN
        self.dataset = self.dataset.dropna(subset=['RH']).reset_index(drop=True)

    def data_preprocessing(self, variable):
        # Split the dataframe to X and Y variables
        X = self.dataset.drop(['Date', 'Time', 'T', 'RH', 'AH'], axis=1)
        Y = self.dataset[variable]

        normalise_train = pd.read_excel("CleanedDataset/TrainingData.xlsx")

        # Normalise the dataset based on the training dataset from comparison
        features_list = list(normalise_train.columns)
        scaler = StandardScaler()
        scaler.fit(normalise_train)
        X_norm = scaler.transform(X)

        X_norm = pd.DataFrame(X_norm, columns=features_list)

        # Drop the column that has too much null value
        X_norm = X_norm.drop(['NMHC(GT)'], axis=1)

        dataset = pd.concat([Y, X_norm], axis=1)

        return dataset

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

    # Method to deal with null values
    @staticmethod
    def null_value(method, dataset):
        if method == "delete":
            dataset = dataset.dropna(axis=0, how='any').reset_index(drop=True)
            return dataset
        else:
            print("No Outliers method found")

    # Feature Scaling Method
    @staticmethod
    def feature_scaling(method, dataset, variable):
        if method == 'none':
            return dataset

        elif method == 'lasso':
            features_name = []
            X_df = dataset.drop([variable], axis=1)
            features_list = list(X_df.columns)
            y_df = dataset[variable]

            # Lasso Model
            lasso = linear_model.Lasso(max_iter=50, random_state=5, alpha=0.1).fit(X_df.values, y_df.values)
            lasso_model = SelectFromModel(lasso, prefit=True)
            features_output = lasso_model.get_support(indices=True)
            X_df = lasso_model.transform(X_df.values)

            for i in features_output:
                features_name.append(features_list[i])

            X_df = pd.DataFrame(X_df, columns=features_name)

            dataset = pd.concat([y_df, X_df], axis=1)

            return dataset


if __name__ == '__main__':
    model = AIModel()
