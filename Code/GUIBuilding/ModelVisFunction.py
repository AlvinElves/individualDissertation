import tkinter as tk
from Code.AIModel.AIModelVis import *


class ModelVisFunction:
    def __init__(self):
        self.aiModelVis = AIModelVis()

        self.model_text = ''
        self.visualisation_text = ''
        self.choose_variable_text = ''
        self.choose_model_text = ''

        self.visualise_variable = ['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)',
                                   'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)']
        self.hyperparameter = ['Number Of Trees', 'Max Depth Of Tree', 'Max Features',
                               'Splitting Method']

    def visualise(self, right_inside_frame, method):
        if self.visualisation_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())
        elif self.model_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\nAI Model to Visualise', foreground='red',
                             bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())
        else:
            label = tk.Label(right_inside_frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
            label.grid(row=9, column=1)
            label.after(3000, lambda: label.destroy())

    def choose_method(self, method, visualisation_label, variable_label, model_label, listbox, button1, button2, button3):
        listbox.delete(0, 'end')
        if method == 'normalised':
            self.visualisation_text = 'Normalised Data'
            self.choose_variable_text = 'Choose the Feature(s)'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for item in self.visualise_variable:
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
            self.choose_variable_text = 'Choose the Tree'
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for i in range(0, 51):
                listbox.insert('end', "test" + str(i))
            self.choose_model_text = 'Choose the AI Model'

        elif method == 'predicted':
            self.visualisation_text = 'Actual VS Predicted'
            self.choose_variable_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            self.choose_model_text = 'Choose the AI Model'

        visualisation_label.config(text=self.visualisation_text)
        variable_label.config(text=self.choose_variable_text)
        model_label.config(text=self.choose_model_text)
        button1.config(text='T Variable\n(TEMPERATURE)', state='normal', bd=2)
        button2.config(text='AH Variable\n(ABSOLUTE HUMIDITY)', state='normal', bd=2)
        button3.config(text='RH Variable\n(RELATIVE HUMIDITY)', state='normal', bd=2)

    def choose_model(self, model_var, model_label):
        if model_var == 't':
            self.model_text = 'T Variable'
        elif model_var == 'ah':
            self.model_text = 'AH Variable'
        elif model_var == 'rh':
            self.model_text = 'RH Variable'

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

