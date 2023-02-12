import pandas as pd
import numpy as np
import seaborn as sns

# Feature Selection
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt


class AIModelVis:
    def __init__(self):
        self.dataset = pd.DataFrame()
        self.get_data_from_excel()

        original_dataset = self.dataset.copy()
        original_dataset = original_dataset.drop(['Date', 'Time', 'T', 'RH', 'AH', 'NMHC(GT)'], axis=1)
        normalised_dataset = self.data_preprocessing('T')

        original_normalised_dataset = normalised_dataset.copy()
        outliers_dataset = self.outliers('delete', self.data_preprocessing('T'))

        feature_dataset = self.null_value('delete', self.outliers('delete', self.data_preprocessing('T')))

        #self.visualise_normalised_data(original_dataset, normalised_dataset, ['CO(GT) (Original)', 'CO(GT) (Processed)'])
        #self.visualise_outliers_data(original_normalised_dataset, outliers_dataset, ['T (Original)', 'T (Processed)'])
        self.visualise_feature_correlation(feature_dataset)

    def visualise_feature_correlation(self, dataset):
        # Correlation matrix for preprocessed data
        cor_df = dataset.copy()
        cor_df = cor_df.iloc[:, 1:10]
        corrMatt = cor_df.iloc[1:10, :].corr()

        # Generate a mask for the upper triangle
        mask = np.zeros_like(corrMatt)
        mask[np.triu_indices_from(mask)] = True

        # Set up the matplotlib figure
        fig, ax = plt.subplots(figsize=(20, 12))
        plt.title('Feature Correlation')

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(260, 10, as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        correlation_map = sns.heatmap(corrMatt, vmax=1.2, square=False, cmap=cmap, mask=mask, ax=ax, annot=True, fmt='.2g', linewidths=1)
        correlation_map.set_yticklabels(correlation_map.get_ymajorticklabels(), fontsize=7)

        plt.show()

    def visualise_outliers_data(self, original_dataset, normalised_dataset, column_name):
        # Combine the dataset to visualise more easily
        combined_visualise_dataset = pd.concat([original_dataset, normalised_dataset], axis=1)

        # Rename the dataset
        combined_visualise_dataset.columns = ['T (Original)', 'CO(GT) (Original)', 'PT08.S1(CO) (Original)',
                                              'C6H6(GT) (Original)', 'PT08.S2(NMHC) (Original)', 'NOx(GT) (Original)',
                                              'PT08.S3(NOx) (Original)', 'NO2(GT) (Original)', 'PT08.S4(NO2) (Original)',
                                              'PT08.S5(O3) (Original)', 'T (Processed)', 'CO(GT) (Processed)',
                                              'PT08.S1(CO) (Processed)', 'C6H6(GT) (Processed)', 'PT08.S2(NMHC) (Processed)',
                                              'NOx(GT) (Processed)', 'PT08.S3(NOx) (Processed)', 'NO2(GT) (Processed)',
                                              'PT08.S4(NO2) (Processed)', 'PT08.S5(O3) (Processed)']

        combined_visualise_dataset = combined_visualise_dataset[column_name]

        combined_visualise_dataset.plot(kind='box', subplots=True, layout=(1, 2), sharex=False, sharey=False,
                                        fontsize=12, figsize=(10, 10))
        plt.show()

    def visualise_normalised_data(self, original_dataset, normalised_dataset, column_name):
        # Combine the dataset to visualise more easily
        combined_normalised_dataset = pd.concat([normalised_dataset, original_dataset], axis=1)

        # Rename the dataset
        combined_normalised_dataset.columns = ['T', 'CO(GT) (Processed)', 'PT08.S1(CO) (Processed)',
                                               'C6H6(GT) (Processed)',
                                               'PT08.S2(NMHC) (Processed)', 'NOx(GT) (Processed)',
                                               'PT08.S3(NOx) (Processed)',
                                               'NO2(GT) (Processed)', 'PT08.S4(NO2) (Processed)',
                                               'PT08.S5(O3) (Processed)',
                                               'CO(GT) (Original)', 'PT08.S1(CO) (Original)', 'C6H6(GT) (Original)',
                                               'PT08.S2(NMHC) (Original)', 'NOx(GT) (Original)',
                                               'PT08.S3(NOx) (Original)',
                                               'NO2(GT) (Original)', 'PT08.S4(NO2) (Original)',
                                               'PT08.S5(O3) (Original)']
        # Rearrange the columns
        combined_normalised_dataset = combined_normalised_dataset[
            ['CO(GT) (Original)', 'CO(GT) (Processed)', 'PT08.S1(CO) (Original)', 'PT08.S1(CO) (Processed)',
             'C6H6(GT) (Original)', 'C6H6(GT) (Processed)', 'PT08.S2(NMHC) (Original)', 'PT08.S2(NMHC) (Processed)',
             'NOx(GT) (Original)', 'NOx(GT) (Processed)', 'PT08.S3(NOx) (Original)', 'PT08.S3(NOx) (Processed)',
             'NO2(GT) (Original)', 'NO2(GT) (Processed)', 'PT08.S4(NO2) (Original)', 'PT08.S4(NO2) (Processed)',
             'PT08.S5(O3) (Original)', 'PT08.S5(O3) (Processed)']]

        visualise = combined_normalised_dataset[column_name]
        visualise = visualise.dropna().reset_index(drop=True)
        visualise = visualise.head(400)
        maximum = max(visualise['CO(GT) (Original)'])
        minimum = min(visualise['CO(GT) (Processed)'])
        visualise.plot(kind='line', fontsize=10, figsize=(30, 10), xlim=(-5, 400), ylim=(minimum - 1, maximum))
        plt.show()

    def get_data_from_excel(self):
        self.dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")

        self.dataset[self.dataset == -200] = np.NaN
        self.dataset = self.dataset.dropna(subset=['RH']).reset_index(drop=True)

    def data_preprocessing(self, variable):
        # Split the dataframe to X and Y variables
        X = self.dataset.drop(['Date', 'Time', 'T', 'RH', 'AH'], axis=1)
        Y = self.dataset[variable]

        # Normalise the dataset based on the training dataset from comparison
        features_list = list(X.columns)
        scaler = StandardScaler()
        scaler.fit(X)
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

    # Method to deal with null values, data imputation
    @staticmethod
    def null_value(method, dataset):
        if method == "delete":
            dataset = dataset.dropna(axis=0, how='any').reset_index(drop=True)
            return dataset
        else:
            print("No Imputation method found")

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
            lasso = linear_model.Lasso(max_iter=50, random_state=5, alpha=0.2).fit(X_df.values, y_df.values)
            lasso_model = SelectFromModel(lasso, prefit=True)
            features_output = lasso_model.get_support(indices=True)
            X_df = lasso_model.transform(X_df.values)

            for i in features_output:
                features_name.append(features_list[i])

            X_df = pd.DataFrame(X_df, columns=features_name)

            dataset = pd.concat([y_df, X_df], axis=1)

            return dataset

        else:
            print("No Feature Scaling method found")


if __name__ == '__main__':
    vis = AIModelVis()
