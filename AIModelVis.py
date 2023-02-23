from AIModel import *

import pandas as pd
import numpy as np
import seaborn as sns

from HandlingInteractions import *
from sklearn import tree
from PIL import Image


class AIModelVis:
    def __init__(self):
        self.interact = HandlingInteractions()
        self.ai_model = AIModel()

        path = self.create_Folder()

        # self.visualise_variable('feature', ['CO(GT) (Original)', 'CO(GT) (Processed)'], 'RH')

        self.visualise_feature_importance(self.ai_model.T_model, self.ai_model.T_dataset.drop(['T'], axis=1))

        # graph = self.generate_tree(path, self.ai_model.T_model, self.ai_model.T_dataset.drop(['T'], axis=1), 0)
        # self.show_Tree('graph', graph, path + "/" + 'tree.png')

    def visualise_variable(self, method, column, variable):
        original_dataset = self.ai_model.dataset.drop(['Date', 'Time', 'T', 'RH', 'AH', 'NMHC(GT)'], axis=1)
        normalised_dataset = self.ai_model.data_preprocessing(variable)

        original_normalised_dataset = normalised_dataset.copy()
        outliers_dataset = self.ai_model.outliers('delete', self.ai_model.data_preprocessing(variable))

        feature_dataset = self.ai_model.null_value('delete', self.ai_model.outliers('delete',
                                                                                    self.ai_model.data_preprocessing(
                                                                                        variable)))

        if method == 'normalised':
            self.visualise_normalised_data(original_dataset, normalised_dataset, column)
        elif method == 'outliers':
            self.visualise_outliers_data(original_normalised_dataset, outliers_dataset, column, variable)
        elif method == 'feature':
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
        fig, ax = plt.subplots(figsize=(10, 8))
        plt.title('Feature Correlation between all features')
        fig.canvas.manager.set_window_title('Correlation Visualisation')

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(260, 10, as_cmap=True)

        # Draw the heatmap with the mask and correct aspect ratio
        correlation_map = sns.heatmap(corrMatt, vmax=1.2, square=False, cmap=cmap, mask=mask, ax=ax, annot=True,
                                      fmt='.2g', linewidths=1)
        correlation_map.set_yticklabels(correlation_map.get_ymajorticklabels(), fontsize=7)
        correlation_map.set_xticklabels(correlation_map.get_xmajorticklabels(), fontsize=7)

        plt.show()

    def visualise_outliers_data(self, original_dataset, normalised_dataset, column_name, variable):
        # Combine the dataset to visualise more easily
        combined_visualise_dataset = pd.concat([original_dataset, normalised_dataset], axis=1)

        # Rename the dataset
        if variable == 'T':
            combined_visualise_dataset.columns = ['T (Original)', 'CO(GT) (Original)', 'PT08.S1(CO) (Original)',
                                                  'C6H6(GT) (Original)', 'PT08.S2(NMHC) (Original)',
                                                  'NOx(GT) (Original)',
                                                  'PT08.S3(NOx) (Original)', 'NO2(GT) (Original)',
                                                  'PT08.S4(NO2) (Original)',
                                                  'PT08.S5(O3) (Original)', 'T (Processed)', 'CO(GT) (Processed)',
                                                  'PT08.S1(CO) (Processed)', 'C6H6(GT) (Processed)',
                                                  'PT08.S2(NMHC) (Processed)',
                                                  'NOx(GT) (Processed)', 'PT08.S3(NOx) (Processed)',
                                                  'NO2(GT) (Processed)',
                                                  'PT08.S4(NO2) (Processed)', 'PT08.S5(O3) (Processed)']
        elif variable == 'AH':
            combined_visualise_dataset.columns = ['AH (Original)', 'CO(GT) (Original)', 'PT08.S1(CO) (Original)',
                                                  'C6H6(GT) (Original)', 'PT08.S2(NMHC) (Original)',
                                                  'NOx(GT) (Original)',
                                                  'PT08.S3(NOx) (Original)', 'NO2(GT) (Original)',
                                                  'PT08.S4(NO2) (Original)',
                                                  'PT08.S5(O3) (Original)', 'AH (Processed)', 'CO(GT) (Processed)',
                                                  'PT08.S1(CO) (Processed)', 'C6H6(GT) (Processed)',
                                                  'PT08.S2(NMHC) (Processed)',
                                                  'NOx(GT) (Processed)', 'PT08.S3(NOx) (Processed)',
                                                  'NO2(GT) (Processed)',
                                                  'PT08.S4(NO2) (Processed)', 'PT08.S5(O3) (Processed)']
        elif variable == 'RH':
            combined_visualise_dataset.columns = ['RH (Original)', 'CO(GT) (Original)', 'PT08.S1(CO) (Original)',
                                                  'C6H6(GT) (Original)', 'PT08.S2(NMHC) (Original)',
                                                  'NOx(GT) (Original)',
                                                  'PT08.S3(NOx) (Original)', 'NO2(GT) (Original)',
                                                  'PT08.S4(NO2) (Original)',
                                                  'PT08.S5(O3) (Original)', 'RH (Processed)', 'CO(GT) (Processed)',
                                                  'PT08.S1(CO) (Processed)', 'C6H6(GT) (Processed)',
                                                  'PT08.S2(NMHC) (Processed)',
                                                  'NOx(GT) (Processed)', 'PT08.S3(NOx) (Processed)',
                                                  'NO2(GT) (Processed)',
                                                  'PT08.S4(NO2) (Processed)', 'PT08.S5(O3) (Processed)']

        # Rename the dataset

        combined_visualise_dataset = combined_visualise_dataset[column_name]

        combined_visualise_dataset.plot(kind='box', subplots=True, layout=(1, 2), sharex=False, sharey=False,
                                        fontsize=12, figsize=(10, 6))

        plt.get_current_fig_manager().canvas.manager.set_window_title('Outliers Visualisation')
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
        maximum = max(visualise[column_name[0]])
        minimum = min(visualise[column_name[1]])

        fig, ax = plt.subplots(figsize=(12, 7))
        fig.canvas.manager.set_window_title('Normalisation Visualisation')

        visualise.plot(kind='line', fontsize=10, ax=ax, xlim=(-5, 400), ylim=(minimum - 1, maximum))
        plt.show()

    def visualise_feature_importance(self, AI_model, dataset):
        plt.figure().set_figwidth(10)
        plt.title('Relative Importance between the features used')
        plt.get_current_fig_manager().canvas.manager.set_window_title('Relative Importance Visualisation')

        feature_importance = pd.Series(AI_model.feature_importances_, index=dataset.columns)
        feature_importance.plot(kind='barh')

        plt.xlabel('Relative Importance')
        plt.show()

    def generate_tree(self, path, AI_model, dataset, tree_number):
        fig = plt.subplots(figsize=(12, 6), dpi=800)

        tree.plot_tree(AI_model.estimators_[tree_number], feature_names=dataset.columns, filled=True)
        plt.savefig(path + "/" + 'tree')
        return plt

    def show_Tree(self, method, graph, image):
        if method == 'image':
            # Read image
            img = Image.open(image)

            # Output Images
            img.show()
        elif method == 'graph':
            graph.show()

    def create_Folder(self):
        new_directory = "Visualisation"  # New folder name
        current_path = os.getcwd()  # Get current file path
        path = os.path.join(current_path, new_directory)

        # Create new folder
        if not os.path.exists(path):
            os.mkdir(path)

        return path


if __name__ == '__main__':
    vis = AIModelVis()
