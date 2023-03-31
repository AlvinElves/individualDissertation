from Code.AIModel.AIModel import *
from Code.HandlingInteractions import *

import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn import tree
from yellowbrick.model_selection import ValidationCurve, LearningCurve
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score


class AIModelVis:
    """
    AIModelVis Class to be imported into GUI files. This class contains all the AI (RandomForestRegressor) Model Visualisation
    functions that can be called in the GUI file easily.
    """

    def __init__(self):
        """
        AIModelVis Class Constructor that calls the AIModel Class and Matplotlib Interaction Class and remove the matplotlib toolbar.
        """
        self.interact = HandlingInteractions()
        self.ai_model = AIModel()

        # Remove the matplotlib toolbar
        plt.rcParams['toolbar'] = 'None'

    def visualise_tree_result(self, ai_model, dataset, actual_dataset, variable, prediction_number, file_name, method):
        """
        A function that is used to visualise the predicted result for all the decision tree.
        :param ai_model: The AI Model that the user want to visualise
        :param dataset: The test dataset that is used to predict using the AI Model
        :param actual_dataset: Actual value from the test dataset
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param prediction_number: The row from the test dataset the user want to visualise
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the predicted result on all the decision tree using line graph and bar graph
        """
        # Get the predicted value for each tree
        tree_prediction = [decision_tree.predict(dataset) for decision_tree in ai_model.estimators_]
        result = [element[prediction_number] for element in tree_prediction]

        # Put the predicted value in a dataframe and get the average predicted value and the actual dataset value
        result_df = pd.DataFrame(result, columns=['Predicted Result'])
        mean = result_df['Predicted Result'].mean()
        actual_df = actual_dataset[prediction_number]

        if method != 'dataset':
            if variable == 'T':
                y_label = 'T (Temperature) '
            elif variable == 'AH':
                y_label = 'AH (Absolute Humidity) '
            else:
                y_label = 'RH (Relative Humidity) '

            # Create a figure and set the window title
            fig, ax = plt.subplots()
            fig.canvas.manager.set_window_title('All Decision Tree Prediction')

            # Allow panning and zooming using a mouse
            pan_handler = panhandler(fig, 1)
            self.interact.zoom_factory(ax, base_scale=1.2)

            # Plot the result using a bar chart and put the value of each bar
            visualise = result_df.plot(kind="bar", ax=ax, color='g', figsize=(12, 7))
            visualise.bar_label(ax.containers[0], fontsize=8)

            # Set the title, X and Y labels for the figure
            plt.minorticks_on()
            ax.set_xticklabels(ax.get_xticks(), rotation=0)
            ax.tick_params(axis='x', which='minor', bottom='off')
            ax.set_xlabel("Decision Tree #")
            ax.set_ylabel(y_label + " Feature Value")
            ax.set_title("Every Decision Tree Prediction VS Average Value VS Actual Value\nfor feature " + y_label)

            # Limit the X and Y axis
            plt.xlim([-0.5, 20.5])
            plt.ylim([min(result_df['Predicted Result']) - 2, max(result_df['Predicted Result']) + 2])

            # Plot the average and actual value using a horizontal dotted line
            ax.axhline(mean, linestyle='--', label='Average Result')
            ax.axhline(actual_df, linestyle='--', color='red', label='Actual Result')

            # Put the value of the line
            yticks = [*ax.get_yticks(), mean, actual_df]
            yticklabels = [*ax.get_yticklabels(), format(mean, ".2f"), format(actual_df, ".2f")]
            ax.set_yticks(yticks, labels=yticklabels)

            # Set the figure legend
            plt.legend()

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            plt.show()
        else:
            # Concat the result dataframe with the average and actual value
            mean = pd.DataFrame([mean], columns=['Average Value'])
            actual_df = pd.DataFrame([actual_df], columns=['Actual Value'])
            df = pd.concat([result_df, mean, actual_df], axis=1)
            return df

    def visualise_hyperparameter(self, ai_model, dataset, test_dataset, variable, param_name, file_name, method):
        """
        A function that is used to visualise the score for each hyperparameter value.
        :param ai_model: The AI Model that the user want to visualise
        :param dataset: The training dataset that is used to train the AI Model
        :param test_dataset: The test dataset that is used to test the AI Model
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param param_name: The hyperparameter that the user want to visualise
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the training score for the hyperparameter using either line graph or bar graph
        """
        if param_name == 'n_estimators':
            param_range = np.arange(1, 36)
            title = 'The Score of Model based on\nthe number of Decision Tree\nfor feature '
        elif param_name == 'max_depth':
            param_range = np.arange(5, 11)
            title = 'The Score of Model based on\nthe maximum depth of Decision Tree\nfor feature '
        elif param_name == 'max_features':
            param_range = [1.0, 'log2', 'sqrt']
            title = 'The Score of Model based on\nmaximum splitting features for\nfeature '
        elif param_name == 'criterion':
            param_range = ['squared_error', 'absolute_error', 'friedman_mse']
            title = 'The Score of Model based on\nthe method of the splitting\nfor feature '

        x = dataset.drop([variable], axis=1)
        y = dataset[variable]

        x_test = test_dataset.drop([variable], axis=1)
        y_test = test_dataset[variable]

        if variable == 'T':
            variable = 'T (Temperature)'
        elif variable == 'AH':
            variable = 'AH (Absolute Humidity)'
        else:
            variable = 'RH (Relative Humidity)'

        if method != 'dataset':
            # Create a figure and set the window title
            fig, ax = plt.subplots(figsize=(10, 5))
            fig.canvas.manager.set_window_title('Hyperparameter Tuning Visualisation')

            # Allow panning and zooming using a mouse
            pan_handler = panhandler(fig, 1)
            self.interact.zoom_factory(ax, base_scale=1.2)

            if param_name == 'n_estimators' or param_name == 'max_depth':
                # Create a validation curve using a line chart
                visualiser = ValidationCurve(ai_model, param_name=param_name, n_jobs=-1,
                                             param_range=param_range, cv=5, scoring="r2",
                                             title=title + variable)

                # Set the X and Y labels for the figure
                plt.xlabel(param_name)
                plt.ylabel("R2 Score (Scoring)")

                # Fit the dataset to the validation curve
                visualiser.fit(x, y)

                if method == 'save':
                    plt.savefig(file_name)

                visualiser.show()

            else:
                if param_name == 'max_features':
                    accuracy = []
                    cross_val = []

                    # Loop through all hyperparameter and set the model to each hyperparameter and output the accuracy and cross
                    # validation
                    for param in param_range:
                        params = {"max_features": param}
                        ai_model.set_params(**params)
                        ai_model.fit(x, y)
                        predicted = ai_model.predict(x_test)

                        accuracy.append(r2_score(y_test, predicted))
                        cross_val.append(np.average(cross_val_score(ai_model, x_test, y_test, cv=5)))

                    # Set the hyperparameter back to the initial hyperparameter
                    params = {"max_features": 1.0}
                    ai_model.set_params(**params)
                    ai_model.fit(x, y)

                    # Concatenate the hyper-parameters and the result
                    parameter = pd.DataFrame(param_range, columns=['Hyperparameter'])
                    accuracy_df = pd.DataFrame(accuracy, columns=['Training Score'])
                    cv_df = pd.DataFrame(cross_val, columns=['Cross Validation Score'])

                    result_df = pd.concat([accuracy_df, cv_df], axis=1)

                    result_df = pd.concat([parameter, result_df], axis=1)

                elif param_name == 'criterion':
                    accuracy = []
                    cross_val = []

                    # Loop through all hyperparameter and set the model to each hyperparameter and output the accuracy and cross
                    # validation
                    for param in param_range:
                        params = {"criterion": param}
                        ai_model.set_params(**params)
                        ai_model.fit(x, y)
                        predicted = ai_model.predict(x_test)

                        accuracy.append(r2_score(y_test, predicted))
                        cross_val.append(np.average(cross_val_score(ai_model, x_test, y_test, cv=5)))

                    # Set the hyperparameter back to the initial hyperparameter
                    if variable == 'AH':
                        params = {"criterion": 'squared_error'}
                    else:
                        params = {"criterion": 'friedman_mse'}

                    ai_model.set_params(**params)
                    ai_model.fit(x, y)

                    # Concatenate the hyper-parameters and the result
                    parameter = pd.DataFrame(param_range, columns=['Hyperparameter'])
                    accuracy_df = pd.DataFrame(accuracy, columns=['Training Score'])
                    cv_df = pd.DataFrame(cross_val, columns=['Cross Validation Score'])

                    result_df = pd.concat([accuracy_df, cv_df], axis=1)

                    result_df = pd.concat([parameter, result_df], axis=1)

                # Plot the hyperparameter result using a bar chart
                result_df.plot(x='Hyperparameter', kind='bar', stacked=False,
                               title=title + variable, ax=ax)

                # Limit Y axis and set the Y axis label
                plt.ylim(0, 1)
                plt.ylabel("R2 Score (Scoring)")
                plt.xticks(rotation=360)

                if method == 'save':
                    # Save the figure
                    plt.savefig(file_name)

                plt.show()

    def visualise_learning_rate(self, ai_model, dataset, variable, file_name, method):
        """
        A function that is used to visualise the learning curve based on the number of training data used.
        :param ai_model: The AI Model that the user want to visualise
        :param dataset: The dataset that is used to train the AI Model
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the learning curve of the AI Model using a line graph
        """
        x = dataset.drop([variable], axis=1)
        y = dataset[variable]

        if method != 'dataset':
            # Create a figure and set the window title
            fig, ax = plt.subplots(figsize=(10, 5))
            fig.canvas.manager.set_window_title('Learning Rate Visualisation')

            # Allow panning and zooming using a mouse
            pan_handler = panhandler(fig, 1)
            self.interact.zoom_factory(ax, base_scale=1.2)

            if variable == 'T':
                variable = 'T (Temperature)'
            elif variable == 'AH':
                variable = 'AH (Absolute Humidity)'
            else:
                variable = 'RH (Relative Humidity)'

            # Create a learning curve using a line chart
            visualiser = LearningCurve(ai_model, n_jobs=-1, cv=10, scoring="r2",
                                       title='Number of data Learning Curve\nfor feature ' + variable)

            # Set the X and Y labels for the figure
            plt.xlabel("Number of Data")
            plt.ylabel("R2 Score (Scoring)")

            # Fit the dataset to the learning curve
            visualiser.fit(x, y)

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            visualiser.show()
        else:
            # Concat the x and y dataset
            df = pd.concat([y, x], axis=1)
            return df

    def visualise_variable(self, method, column, variable, normaliser, file_name, guimethod):
        """
        A function that calls the normalised, outliers and feature correlation visualisation since we had to get the data one by one
        :param method: The type of visualisation the user chose, normalised, outliers or feature correlation
        :param column: The feature that the user want to visualise
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param normaliser: The normalisation scaler used to normalise the dataset
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param guimethod: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that the user had chose
        """
        # Get the AI model dataset and clean/preprocess it
        original_dataset = self.ai_model.model_dataset.copy()
        original_dataset[original_dataset == -200] = np.NaN
        original_dataset = original_dataset.dropna(subset=['T']).reset_index(drop=True)
        original_df = original_dataset.drop(['Date', 'Time', 'T', 'RH', 'AH'], axis=1)
        y_value = original_dataset[variable]

        # Do normalisation to the preprocessed dataset with the normaliser
        normalised_dataset = original_df.copy()
        features_list = list(normalised_dataset.columns)
        normalised_df = normaliser.transform(normalised_dataset)
        normalised_dataset = pd.DataFrame(normalised_df, columns=features_list)

        original_dataset = original_df.drop(['NMHC(GT)'], axis=1)
        normalised_dataset = normalised_dataset.drop(['NMHC(GT)'], axis=1)

        normalised = pd.concat([y_value, normalised_dataset], axis=1)

        # Deal with the outliers to the normalised dataset
        original_normalised_dataset = normalised.copy()
        outliers_dataset = self.ai_model.outliers('delete', original_normalised_dataset)

        # Deal with the null value to the outliers dataset
        feature_dataset, _ = self.ai_model.null_value('delete', outliers_dataset, pd.DataFrame())

        # Visualise the before and after based on the method chosen
        if method == 'normalised':
            df = self.visualise_normalised_data(original_dataset, normalised_dataset, column, variable, file_name,
                                                guimethod)
            return df

        elif method == 'outliers':
            df = self.visualise_outliers_data(original_normalised_dataset, outliers_dataset, column, variable,
                                              file_name, guimethod)
            return df

        elif method == 'feature':
            df = self.visualise_feature_correlation(feature_dataset, variable, file_name, guimethod)
            return df

    @staticmethod
    def visualise_feature_correlation(dataset, variable, file_name, method):
        """
        A function that is used to visualise the correlation relationship between the feature.
        :param dataset: The dataset used to generate the feature correlation
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the correlation between the features using a heatmap
        """
        # Correlation matrix for preprocessed data
        cor_df = dataset.copy()
        cor_df = cor_df.iloc[:, 1:10]
        corrMatt = cor_df.iloc[1:10, :].corr()
        if method != 'dataset':

            # Generate a mask for the upper triangle
            mask = np.zeros_like(corrMatt)
            mask[np.triu_indices_from(mask)] = True

            if variable == 'T':
                variable = 'T (Temperature)'
            elif variable == 'AH':
                variable = 'AH (Absolute Humidity)'
            else:
                variable = 'RH (Relative Humidity)'

            # Set up the matplotlib figure
            fig, ax = plt.subplots(figsize=(10, 8))
            plt.title('Feature Correlation between all features\nfor feature ' + variable)
            fig.canvas.manager.set_window_title('Correlation Visualisation')

            # Generate a custom diverging colormap
            cmap = sns.diverging_palette(260, 10, as_cmap=True)

            # Draw the heatmap with the mask and correct aspect ratio
            correlation_map = sns.heatmap(corrMatt, vmax=1.2, square=False, cmap=cmap, mask=mask, ax=ax, annot=True,
                                          fmt='.2g', linewidths=1)
            correlation_map.set_yticklabels(correlation_map.get_ymajorticklabels(), fontsize=7)
            correlation_map.set_xticklabels(correlation_map.get_xmajorticklabels(), fontsize=7)

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            plt.show()

        else:
            return corrMatt

    @staticmethod
    def visualise_outliers_data(original_dataset, outliers_dataset, column_name, variable, file_name, method):
        """
        A function that is used to visualise the difference between original and outliers data side by side.
        :param original_dataset: Original Dataset that is used for AI Model
        :param outliers_dataset: Outliers Dataset that removed the outliers from percentile
        :param column_name: The feature that the user want to visualise
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the before and after, original dataset and outliers dataset using a boxplot
        """
        # Combine the dataset to visualise more easily
        combined_visualise_dataset = pd.concat([original_dataset, outliers_dataset], axis=1)

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
            variable = 'T (Temperature)'

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
            variable = 'AH (Absolute Humidity)'

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
            variable = 'RH (Relative Humidity)'

        combined_visualise_dataset = combined_visualise_dataset[column_name]
        if method != 'dataset':
            # Plot the before and after outliers dataset using a box plot
            combined_visualise_dataset.plot(kind='box', subplots=True, layout=(1, 2), sharex=False, sharey=True,
                                            fontsize=12, figsize=(10, 6))

            #  Set the window title, plot title and Y labels for the figure
            plt.get_current_fig_manager().canvas.manager.set_window_title('Outliers Visualisation')
            plt.ylabel(column_name[0] + " VS " + column_name[1] + " Values")
            plt.title('Outliers Visualisation for\nfeature ' + variable)

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            plt.show()
        else:
            return combined_visualise_dataset

    def visualise_normalised_data(self, original_dataset, normalised_dataset, column_name, variable, file_name, method):
        """
        A function that is used to visualise the pattern of original and normalised data for the AI Model later.
        :param original_dataset: Original Dataset that is used for AI Model
        :param normalised_dataset: Normalised Dataset that has been normalised standard scalar
        :param column_name: The feature that the user want to visualise
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the before and after, original dataset and normalised dataset using a line graph
        """
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

        if variable == 'T':
            variable = 'T (Temperature)'
        elif variable == 'AH':
            variable = 'AH (Absolute Humidity)'
        else:
            variable = 'RH (Relative Humidity)'

        visualise = combined_normalised_dataset[column_name]
        visualise = visualise.dropna().reset_index(drop=True)

        if method != 'dataset':
            maximum = max(visualise[column_name[0]])
            minimum = min(visualise[column_name[1]])

            # Create a figure and set the window title
            fig, ax = plt.subplots(figsize=(12, 7))
            fig.canvas.manager.set_window_title('Normalisation Visualisation')

            # Allow panning and zooming using a mouse
            pan_handler = panhandler(fig, 1)
            self.interact.zoom_factory(ax, base_scale=1.2)

            # Creating axis limits and title
            plt.xlim([0, 100])
            plt.xlabel("Data Number")
            plt.ylabel(column_name[0] + " VS " + column_name[1] + " Values")
            plt.title('Normalised Visualisation for feature ' + variable)

            # Plot the before and after normalised dataset using a line chart
            visualise.plot(kind='line', fontsize=10, ax=ax, ylim=(minimum - 1, maximum))

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            plt.show()
        else:
            return visualise

    @staticmethod
    def visualise_feature_importance(AI_model, dataset, variable, file_name, method):
        """
        A function that is used to visualise the feature importance of the AI Model. This function shows the user how each of the
        independent variable affects the final outcome prediction, and which variable is important for it.
        :param AI_model: The AI Model that the user want to visualise
        :param dataset: The dataset that is used to train the AI Model
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the feature importance using a horizontal bar graph
        """

        if variable == 'T':
            variable = 'T (Temperature)'
        elif variable == 'AH':
            variable = 'AH (Absolute Humidity)'
        else:
            variable = 'RH (Relative Humidity)'

        if method != 'dataset':

            # Create a figure and set the window title
            fig, ax = plt.subplots(figsize=(12, 6))
            plt.title('Relative Importance between the features\nused for feature ' + variable)
            fig.canvas.manager.set_window_title('Relative Importance Visualisation')

            # Plot the feature importance using a horizontal bar chart
            feature_importance = pd.Series(AI_model.feature_importances_, index=dataset.columns)
            visualise = feature_importance.plot(kind='barh', ax=ax)

            # put the value of each bar
            visualise.bar_label(ax.containers[0], fontsize=8)

            # Creating axis limits and title
            plt.xlabel('Relative Importance')
            plt.xlim(0, max(feature_importance) + 0.1)

            if method == 'save':
                # Save the figure
                plt.savefig(file_name)

            plt.show()

    def visualise_actual_and_predicted(self, actual, predicted, variable, file_name, method):
        """
        A function that is used to visualise the actual vs predicted value of the AI Model. This function shows the user the difference
        between the actual test value and the predicted value from the AI Model. The function also show the percentage difference
        between the two.
        :param actual: Actual value from the test dataset
        :param predicted: Predicted value from the AI Model
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A plotly HTML figure that shows the actual vs predicted value using line graph and the percentage difference with
        bar graph
        """

        predicted = pd.DataFrame(predicted, columns=[variable])
        combined = pd.concat([actual, predicted], axis=1)

        column_name = [variable + " (Actual)"] + [variable + " (Predicted)"]
        combined.columns = column_name

        # Calculate the percentage difference between the actual and predicted value
        combined['Percentage'] = (abs(combined[variable + " (Actual)"] - combined[variable + " (Predicted)"]) /
                                  combined[variable + " (Actual)"]) * 100

        if method != 'dataset':

            # Create figure with secondary y-axis
            fig = make_subplots(specs=[[{"secondary_y": True}]])

            # Add the traces for the actual and predicted values using a line chart
            fig.add_trace(go.Scatter(x=combined.index, y=combined[variable + " (Actual)"], name="Actual Value"),
                          secondary_y=False)
            fig.add_trace(go.Scatter(x=combined.index, y=combined[variable + " (Predicted)"], name="Predicted Value"),
                          secondary_y=False)

            # Add the traces for the percentage difference between the two values using a bar chart
            fig.add_trace(
                go.Bar(x=combined.index, y=combined['Percentage'], name="Percentage Difference", marker_color='grey',
                       opacity=0.5),
                secondary_y=True)

            if variable == 'T':
                variable = 'T (Temperature)'
            elif variable == 'AH':
                variable = 'AH (Absolute Humidity)'
            else:
                variable = 'RH (Relative Humidity)'

            # Set the axis limit, axis label and the plot title
            fig.update_layout(xaxis_range=[-0.5, 50], yaxis_range=[0, combined[column_name].max() + 1],
                              yaxis2_range=[0, 200],
                              title="Actual vs Predicted for feature " + variable, hovermode='x unified')
            fig.update_xaxes(title_text="Prediction #", rangeslider_visible=True)
            fig.update_yaxes(title_text="Feature Value for feature " + variable, secondary_y=False)
            fig.update_yaxes(title_text="Difference between Actual and Predicted (%)", secondary_y=True)

            if method == 'save':
                # Save the figure
                fig.write_html(file_name)

            fig.show()

        else:
            return combined

    def check_decision(self, current_decision, number, decision):
        """
        A function that checks the decision of the tree
        :param current_decision: The current decision number for the node
        :param number: The node number
        :param decision: Decision of the node
        :return: A boolean that indicates the decision and the current decision number
        """
        if current_decision == number:
            if decision == 'True':
                decision = 'False'

                current_decision -= 1

            else:
                decision = 'True'

        return decision, current_decision

    def generate_tree(self, AI_model, dataset, tree_number, variable, file_name, method):
        """
        A function that is used to visualise the decision tree used for prediction.
        :param AI_model: The AI Model that the user want to visualise
        :param dataset: The dataset that is used to train the AI Model
        :param tree_number: The decision tree the user want to visualise
        :param variable: The dependent variable that the user want to predict with the AI Model
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A plotly HTML figure that shows the decision tree using a tree map
        """
        if method != 'dataset':
            if variable == 'T':
                variable = 'T (Temperature)'
            elif variable == 'AH':
                variable = 'AH (Absolute Humidity)'
            else:
                variable = 'RH (Relative Humidity)'

            # Get the text for list of node from the decision tree
            nodes = tree.plot_tree(AI_model.estimators_[tree_number], feature_names=dataset.columns, filled=True)
            plt.close()

            list_of_node = []
            current_decision = 0

            decisions = ['False', 'False', 'False', 'False', 'False', 'False']
            node_parents = []

            # Loop through all the node from the decision tree
            for i in range(len(nodes)):
                # Split the node into smaller element to put them in a list
                node_information = str(nodes[i]).split("'")[1]
                decision_information = node_information.split('\\n')

                # If the node is the leaf node, add empty string to the first element of the list
                if len(decision_information) == 3:
                    decision_information = [''] + decision_information

                # Split the list of element to contain the value instead of string and value
                criterion = decision_information[1].split('= ')[0]
                decision_information[1] = decision_information[1].split('= ')[1]
                decision_information[2] = decision_information[2].split('= ')[1]
                decision_information[3] = decision_information[3].split('= ')[1]

                # If the node is a leaf node
                if decision_information[0] == '':
                    # If the level of the decision tree is 0
                    if current_decision == 0:
                        decision_information = ['', ''] + decision_information + [current_decision]
                    else:
                        decision_information = [decisions[current_decision - 1], node_parents[current_decision - 1]] + \
                                               decision_information + [current_decision]

                        decision_information[2] = decision_information[0] + '<br>Value = ' + decision_information[5]

                    # Check the level of the decision tree
                    decisions[5], current_decision = self.check_decision(current_decision, 6, decisions[5])
                    decisions[4], current_decision = self.check_decision(current_decision, 5, decisions[4])
                    decisions[3], current_decision = self.check_decision(current_decision, 4, decisions[3])
                    decisions[2], current_decision = self.check_decision(current_decision, 3, decisions[2])
                    decisions[1], current_decision = self.check_decision(current_decision, 2, decisions[1])
                    decisions[0], current_decision = self.check_decision(current_decision, 1, decisions[0])

                else:  # If the node is not a leaf node
                    # If the level of the decision tree is 0
                    if current_decision == 0:
                        decision_information = ['', ''] + decision_information + [current_decision]
                        decision_information[2] = decision_information[2] + '?'

                        # If the list of node_parents is empty
                        if len(node_parents) == 0:
                            # Insert the parent node at position 0
                            node_parents.insert(0, decision_information[2])
                        else:
                            # Change the element value at position 0
                            node_parents[0] = decision_information[2]

                    else:
                        decision_information = [decisions[current_decision - 1], node_parents[current_decision - 1]] + \
                                               decision_information + [current_decision]

                        decision_information[2] = decision_information[0] + '<br>' + decision_information[2] + '?'

                        # If the list of node_parents is empty
                        if len(node_parents) == current_decision:
                            # Insert the parent node at position 'current_decision'
                            node_parents.insert(current_decision, decision_information[2])
                        else:
                            # Change the element value at position 'current_decision'
                            node_parents[current_decision] = decision_information[2]

                    current_decision += 1

                list_of_node.append(decision_information)

            # Create a dataframe with the node information
            node_df = pd.DataFrame(list_of_node, columns=['PreviousLeafDecision', 'Parents', 'Decision',
                                                          'Criterion', 'Samples', 'Value', 'Level'])

            frame0 = None
            frames = []

            # Loop through the level of the decision tree and create the treemap based on the level
            for i in range(0, node_df['Level'].max() + 1):
                treemap = go.Treemap(labels=node_df[node_df['Level'] <= i]['Decision'],
                                     parents=node_df[node_df['Level'] <= i]['Parents'], root_color="lightgrey")

                if frame0 is None:
                    frame0 = treemap

                frames.append(go.Frame(name=f"frame-{i}", data=treemap))

            # Create the slider that change the treemap frame based on the level of slider
            sliders = [
                dict(
                    steps=[
                        dict(
                            method="animate",
                            args=[
                                [f"frame-{i}"],
                                dict(mode="e", frame=dict(redraw=True), transition=dict(duration=200))],
                            label=f"{i}")
                        for i in range(0, node_df['Level'].max() + 1)
                    ],
                    transition=dict(duration=0),
                    x=0,
                    y=0,
                    currentvalue=dict(
                        font=dict(size=12), prefix="Level: ", visible=True, xanchor="center"
                    ),
                    len=1.0,
                    active=0,
                )
            ]

            # Create the layout of the figure
            layout = {"title": 'Decision Tree Number ' + str(tree_number + 1) + ' for feature ' + variable,
                      "sliders": sliders}

            # Create figure
            fig = go.Figure(data=frame0, layout=layout, frames=frames)

            # Update the figure hover text
            fig.update_traces(hovertext='<br>' + criterion + ' = ' + node_df.Criterion + '<br>Samples = ' +
                                        node_df.Samples + '<br>Value = ' + node_df.Value)

            if method == 'save':
                # Save the figure
                fig.write_html(file_name)

            fig.show()


if __name__ == '__main__':
    vis = AIModelVis()
