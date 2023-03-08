from Code.AIModel.AIModel import *
from Code.HandlingInteractions import *

import pandas as pd
import numpy as np
import seaborn as sns

from sklearn import tree
from PIL import Image
from yellowbrick.model_selection import ValidationCurve, LearningCurve


class AIModelVis:
    def __init__(self):
        self.interact = HandlingInteractions()
        self.ai_model = AIModel()

        path = self.create_Folder()

        # Remove the matplotlib toolbar
        plt.rcParams['toolbar'] = 'None'

        #self.visualise_variable('normalised', ['CO(GT) (Original)', 'CO(GT) (Processed)'], 'T', self.ai_model.T_normalise)

        #self.visualise_feature_importance(self.ai_model.T_model, self.ai_model.T_train.drop(['T'], axis=1))
        #self.visualise_actual_and_predicted(self.ai_model.T_actual, self.ai_model.T_prediction, 'T')

        #graph = self.generate_tree(path, self.ai_model.T_model, self.ai_model.T_train.drop(['T'], axis=1), 0)
        #self.show_Tree('graph', graph, path + "/" + 'tree.png')

        #self.visualise_hyperparameter(self.ai_model.T_model, self.ai_model.T_train, 'T', 'criterion')
        #self.visualise_learning_rate(self.ai_model.T_model, self.ai_model.T_train, 'T')

        #self.visualise_tree_result(self.ai_model.T_model, self.ai_model.T_test.drop(['T'], axis=1), 'T', 0)

    def visualise_tree_result(self, ai_model, dataset, variable, prediction_number):
        y_label = ''
        tree_prediction = [decision_tree.predict(dataset) for decision_tree in ai_model.estimators_]
        result = [element[prediction_number] for element in tree_prediction]

        result_df = pd.DataFrame(result, columns=['Predicted Result'])

        if variable == 'T':
            y_label = 'Temperature '
        elif variable == 'AH':
            y_label = 'Absolute Humidity '
        elif variable == 'RH':
            y_label = 'Relative Humidity '

        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title('All Tree Prediction')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        result_df.plot(kind="bar", ax=ax, color='g', figsize=(12, 7))

        plt.minorticks_on()
        ax.set_xticklabels(ax.get_xticks(), rotation=0)
        ax.tick_params(axis='x', which='minor', bottom='off')
        ax.set_xlabel("Decision Tree Number")
        ax.set_ylabel(y_label + " Value")
        ax.set_title("Decision Tree Prediction & Average Value")

        plt.xlim([0, 30])
        plt.ylim([min(result_df['Predicted Result']) - 2, max(result_df['Predicted Result']) + 2])

        mean = result_df['Predicted Result'].mean()
        ax.axhline(mean, linestyle='--', label='Average Result')
        #ax.axhline(mean + 1, linestyle='--', color='red', label='Predicted Result')

        plt.legend()

        plt.show()

    def visualise_hyperparameter(self, ai_model, dataset, variable, param_name):
        if param_name == 'n_estimators':
            param_range = np.arange(1, 36)
        elif param_name == 'max_depth':
            param_range = np.arange(5, 11)
        elif param_name == 'max_features':
            param_range = [1.0, 'log2', 'sqrt']
        elif param_name == 'criterion':
            param_range = ['poisson', 'squared_error', 'absolute_error', 'friedman_mse']

        fig, ax = plt.subplots(figsize=(10, 5))
        fig.canvas.manager.set_window_title('Hyperparameter Tuning Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        visualizer = ValidationCurve(ai_model, param_name=param_name, n_jobs=-1,
                                     param_range=param_range, cv=5, scoring="r2")

        x = dataset.drop([variable], axis=1)
        y = dataset[variable]

        plt.xlabel(param_name)
        plt.ylabel("R2 Score (Scoring)")

        visualizer.fit(x, y)

        visualizer.show()

    def visualise_learning_rate(self, ai_model, dataset, variable):
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.canvas.manager.set_window_title('Learning Rate Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        visualizer = LearningCurve(ai_model, n_jobs=-1, cv=10, scoring="r2")

        x = dataset.drop([variable], axis=1)
        y = dataset[variable]

        plt.xlabel("Number of Data")
        plt.ylabel("R2 Score (Scoring)")

        visualizer.fit(x, y)

        visualizer.show()

    def visualise_variable(self, method, column, variable, normaliser):
        original_dataset = self.ai_model.model_dataset.copy()
        original_dataset[original_dataset == -200] = np.NaN
        original_dataset = original_dataset.dropna(subset=['T']).reset_index(drop=True)
        original_df = original_dataset.drop(['Date', 'Time', 'T', 'RH', 'AH'], axis=1)
        y_value = original_dataset[variable]

        normalised_dataset = original_df.copy()
        features_list = list(normalised_dataset.columns)
        normalised_df = normaliser.transform(normalised_dataset)
        normalised_dataset = pd.DataFrame(normalised_df, columns=features_list)

        original_dataset = original_df.drop(['NMHC(GT)'], axis=1)
        normalised_dataset = normalised_dataset.drop(['NMHC(GT)'], axis=1)

        normalised = pd.concat([y_value, normalised_dataset], axis=1)

        original_normalised_dataset = normalised.copy()
        outliers_dataset = self.ai_model.outliers('delete', original_normalised_dataset)

        feature_dataset, _ = self.ai_model.null_value('delete', outliers_dataset, pd.DataFrame())

        if method == 'normalised':
            self.visualise_normalised_data(original_dataset, normalised_dataset, column)
        elif method == 'outliers':
            self.visualise_outliers_data(original_normalised_dataset, outliers_dataset, column, variable)
        elif method == 'feature':
            self.visualise_feature_correlation(feature_dataset)

    @staticmethod
    def visualise_feature_correlation(dataset):
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

    @staticmethod
    def visualise_outliers_data(original_dataset, normalised_dataset, column_name, variable):
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
        combined_normalised_dataset.columns = ['CO(GT) (Processed)', 'PT08.S1(CO) (Processed)',
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
        maximum = max(visualise[column_name[0]])
        minimum = min(visualise[column_name[1]])

        fig, ax = plt.subplots(figsize=(12, 7))
        fig.canvas.manager.set_window_title('Normalisation Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        # Creating axis limits and title
        plt.xlim([0, 100])
        plt.xlabel("Data Number")
        plt.ylabel(column_name[0] + " VS " + column_name[1] + " Values")

        visualise.plot(kind='line', fontsize=10, ax=ax, ylim=(minimum - 1, maximum))
        plt.show()

    @staticmethod
    def visualise_feature_importance(AI_model, dataset):
        plt.figure().set_figwidth(10)
        plt.title('Relative Importance between the features used')
        plt.get_current_fig_manager().canvas.manager.set_window_title('Relative Importance Visualisation')

        feature_importance = pd.Series(AI_model.feature_importances_, index=dataset.columns)
        feature_importance.plot(kind='barh')

        plt.xlabel('Relative Importance')
        plt.show()

    def visualise_actual_and_predicted(self, actual, predicted, variable):

        predicted = pd.DataFrame(predicted, columns=[variable])
        combined = pd.concat([actual, predicted], axis=1)

        column_name = [variable + " (Actual)"] + [variable + " (Predicted)"]
        combined.columns = column_name

        fig, ax = plt.subplots(figsize=(12, 7))
        fig.canvas.manager.set_window_title('Prediction Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        # Creating axis limits and title
        plt.xlim([0, 50])
        plt.xlabel("Prediction Number")
        plt.ylabel(variable + " Values")

        plt.title("Actual vs Predicted " + variable + " variable")

        combined.plot(kind='line', fontsize=10, ax=ax)
        plt.show()

    @staticmethod
    def generate_tree(path, AI_model, dataset, tree_number):
        fig, ax = plt.subplots(figsize=(12, 6), dpi=800)
        fig.canvas.manager.set_window_title('Tree ' + str(tree_number + 1) + ' Estimator Visualisation')

        tree.plot_tree(AI_model.estimators_[tree_number], feature_names=dataset.columns, filled=True)
        plt.savefig(path + "/" + 'tree')
        return plt

    @staticmethod
    def show_Tree(method, graph, image):
        if method == 'image':
            # Read image
            img = Image.open(image)

            # Output Images
            img.show()
        elif method == 'graph':
            graph.show()

    @staticmethod
    def create_Folder():
        new_directory = "Visualisation"  # New folder name
        current_path = os.path.dirname(os.path.dirname(os.getcwd()))  # Get current file path
        path = os.path.join(current_path, new_directory)

        # Create new folder
        if not os.path.exists(path):
            os.mkdir(path)

        return path


if __name__ == '__main__':
    vis = AIModelVis()
