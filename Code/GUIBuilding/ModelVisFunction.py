import tkinter as tk
from Code.AIModel.AIModelVis import *


class ModelVisFunction:
    def __init__(self):
        self.aiModelVis = AIModelVis()
        self.aiModel = self.aiModelVis.ai_model

        self.model_text = ''
        self.visualisation_text = ''
        self.choose_variable_text = ''
        self.choose_model_text = ''

        self.visualise_variable = ['CO(GT)', 'PT08.S1(CO)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)',
                                   'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)']
        self.hyperparameter = ['Number Of Trees', 'Max Depth Of Tree', 'Max Features',
                               'Splitting Method']

    def visualise(self, right_inside_frame, model_label, visualisation_label, variable_label, model_choose_label,
                  listbox, button1,
                  button2, button3, entry, method):
        listbox_index, features, checked_passed, file_name, file_passed = self.check_filename(right_inside_frame,
                                                                                              listbox, entry,
                                                                                              method)

        # Show a message in the GUI
        if checked_passed and file_passed:
            if method == 'visualise':
                label = tk.Label(right_inside_frame, text='Loading, Please wait', foreground='green',
                                 bg='lightskyblue')
            else:
                label = tk.Label(right_inside_frame, text='Saving the File', foreground='green',
                                 bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())

        # If the user chose all the variables
        if checked_passed:
            if self.model_text == 'T Variable':
                model_variable = 'T'
                scalar = self.aiModel.T_normalise
                all_df = self.aiModel.T_train
                train_df = self.aiModel.T_train.drop(['T'], axis=1)
                test_df = self.aiModel.T_test.drop(['T'], axis=1)
                actual_df = self.aiModel.T_actual
                predicted_df = self.aiModel.T_prediction
                aiModel = self.aiModel.T_model

            elif self.model_text == 'AH Variable':
                model_variable = 'AH'
                scalar = self.aiModel.AH_normalise
                all_df = self.aiModel.AH_train
                train_df = self.aiModel.AH_train.drop(['AH'], axis=1)
                test_df = self.aiModel.AH_test.drop(['AH'], axis=1)
                actual_df = self.aiModel.AH_actual
                predicted_df = self.aiModel.AH_prediction
                aiModel = self.aiModel.AH_model

            else:
                model_variable = 'RH'
                scalar = self.aiModel.RH_normalise
                all_df = self.aiModel.RH_train
                train_df = self.aiModel.RH_train.drop(['RH'], axis=1)
                test_df = self.aiModel.RH_test.drop(['RH'], axis=1)
                actual_df = self.aiModel.RH_actual
                predicted_df = self.aiModel.RH_prediction
                aiModel = self.aiModel.RH_model

            if self.visualisation_text == 'Normalised Data' or self.visualisation_text == 'Outliers Data':
                original_features = features[0] + ' (Original)'
                processed_features = features[0] + ' (Processed)'
                features_used = [original_features, processed_features]

            if self.visualisation_text == 'Normalised Data':
                self.aiModelVis.visualise_variable('normalised', features_used, model_variable, scalar)

            elif self.visualisation_text == 'Outliers Data':
                self.aiModelVis.visualise_variable('outliers', features_used, model_variable, scalar)

            elif self.visualisation_text == 'Feature Correlation':
                self.aiModelVis.visualise_variable('feature', None, model_variable, scalar)

            elif self.visualisation_text == 'Feature Importance':
                self.aiModelVis.visualise_feature_importance(aiModel, train_df, model_variable)

            elif self.visualisation_text == 'Learning Curve':
                self.aiModelVis.visualise_learning_rate(aiModel, all_df, model_variable)

            elif self.visualisation_text == 'Hyperparameter Tuning':
                print(self.visualisation_text)

            elif self.visualisation_text == 'Decision Tree':
                print(self.visualisation_text)

            elif self.visualisation_text == 'Actual VS Predicted':
                self.aiModelVis.visualise_actual_and_predicted(actual_df, predicted_df, model_variable)

            elif self.visualisation_text == 'All Decision\nTree Prediction':
                self.aiModelVis.visualise_tree_result(aiModel, test_df, actual_df, model_variable, listbox_index[0])

            self.clear(model_label, visualisation_label, variable_label, model_choose_label, listbox, button1,
                       button2, button3)

    def check_filename(self, right_inside_frame, listbox, entry, method):
        listbox_index, features, checked_passed = self.check_visualise(right_inside_frame, listbox)
        file_name = entry.get()
        file_passed = False

        if checked_passed and (method == 'dataset' or method == 'save'):
            if file_name == '':
                label = tk.Label(right_inside_frame, text='Please Enter a\nFilename to Save', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=9, column=1)
                label.after(3000, lambda: label.destroy())
                file_passed = False

            else:
                file_passed = True

        elif method == 'visualise':
            file_passed = True

        return listbox_index, features, checked_passed, file_name, file_passed

    def check_visualise(self, right_inside_frame, listbox):
        listbox_index, variables = self.get_listbox(listbox)
        if self.visualisation_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())
            checked = False

        elif self.model_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\nAI Model to Visualise', foreground='red',
                             bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())
            checked = False

        elif self.visualisation_text == 'Normalised Data' or self.visualisation_text == 'Outliers Data' or \
                self.visualisation_text == 'Hyperparameter Tuning' or self.visualisation_text == 'Decision Tree' or \
                self.visualisation_text == 'All Decision\nTree Prediction':
            if not variables:
                label = tk.Label(right_inside_frame, text='Please Choose the\nItem(s) from listbox\nto Visualise',
                                 foreground='red',
                                 bg='lightskyblue')
                label.grid(row=9, column=1)
                label.after(3000, lambda: label.destroy())
                checked = False
            else:
                checked = True

        else:
            checked = True

        return listbox_index, variables, checked

    def get_listbox(self, listbox):
        items = []
        index = listbox.curselection()
        for i in index:
            result = listbox.get(i)
            if result == 'T (Temperature)':
                result = 'T'
            elif result == 'AH (Absolute Humidity)':
                result = 'AH'
            elif result == 'RH (Relative Humidity)':
                result = 'RH'

            items.append(result)

        return index, items

    def choose_method(self, method, visualisation_label, variable_label, model_label, listbox, button1, button2,
                      button3):
        listbox.delete(0, 'end')
        if method == 'normalised':
            self.visualisation_text = 'Normalised Data'
            self.choose_variable_text = 'Choose the Feature(s)'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            if self.model_text == 'T Variable':
                view_variable = ['T (Temperature)'] + self.visualise_variable

            elif self.model_text == 'AH Variable':
                view_variable = ['AH (Absolute Humidity)'] + self.visualise_variable

            elif self.model_text == 'RH Variable':
                view_variable = ['RH (Relative Humidity)'] + self.visualise_variable
            else:
                view_variable = self.visualise_variable

            for item in view_variable:
                listbox.insert('end', item)
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'outliers':
            self.visualisation_text = 'Outliers Data'
            self.choose_variable_text = 'Choose the Feature(s)'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for item in self.visualise_variable:
                listbox.insert('end', item)
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'feature':
            self.visualisation_text = 'Feature Correlation'
            self.choose_variable_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'feature_importance':
            self.visualisation_text = 'Feature Importance'
            self.choose_variable_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'learning':
            self.visualisation_text = 'Learning Curve'
            self.choose_variable_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'hyperparameter':
            self.visualisation_text = 'Hyperparameter Tuning'
            self.choose_variable_text = 'Choose the\nHyperparameter'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for item in self.hyperparameter:
                listbox.insert('end', item)
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'tree':
            self.visualisation_text = 'Decision Tree'
            self.choose_variable_text = 'Choose the\nDecision Tree #'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for i in range(0, 51):
                listbox.insert('end', "test" + str(i))
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'predicted':
            self.visualisation_text = 'Actual VS Predicted'
            self.choose_variable_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'all_tree':
            self.visualisation_text = 'All Decision\nTree Prediction'
            self.choose_variable_text = 'Choose the\nData Row #'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for i in range(0, 51):
                listbox.insert('end', "Data Row " + str(i))

            self.choose_model_text = 'Choose the AI Model'

        visualisation_label.config(text=self.visualisation_text)
        variable_label.config(text=self.choose_variable_text)
        model_label.config(text=self.choose_model_text)
        button1.config(text='T Variable\n(TEMPERATURE)', state='normal', bd=2)
        button2.config(text='AH Variable\n(ABSOLUTE HUMIDITY)', state='normal', bd=2)
        button3.config(text='RH Variable\n(RELATIVE HUMIDITY)', state='normal', bd=2)

    def choose_model(self, model_var, model_label, listbox):
        if model_var == 't':
            self.model_text = 'T Variable'
            if self.visualisation_text == 'Normalised Data':
                view_variable = ['T (Temperature)'] + self.visualise_variable
                listbox.delete(0, 'end')
                for item in view_variable:
                    listbox.insert('end', item)

        elif model_var == 'ah':
            self.model_text = 'AH Variable'
            if self.visualisation_text == 'Normalised Data':
                view_variable = ['AH (Absolute Humidity)'] + self.visualise_variable
                listbox.delete(0, 'end')
                for item in view_variable:
                    listbox.insert('end', item)

        elif model_var == 'rh':
            self.model_text = 'RH Variable'
            if self.visualisation_text == 'Normalised Data':
                view_variable = ['RH (Relative Humidity)'] + self.visualise_variable
                listbox.delete(0, 'end')
                for item in view_variable:
                    listbox.insert('end', item)

        model_label.config(text=self.model_text)

    def clear(self, model_label, visualisation_label, variable_label, model_choose_label, listbox, button1,
              button2, button3):
        self.visualisation_text = ''
        self.model_text = ''
        self.choose_variable_text = ''
        self.choose_model_text = ''
        model_label.config(text=self.model_text)
        visualisation_label.config(text=self.visualisation_text)
        variable_label.config(text=self.choose_variable_text)
        model_choose_label.config(text=self.choose_model_text)

        listbox.delete(0, 'end')
        listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
        button1.config(text='', state='disabled', bd=0)
        button2.config(text='', state='disabled', bd=0)
        button3.config(text='', state='disabled', bd=0)
