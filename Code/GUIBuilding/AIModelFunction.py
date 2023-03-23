import tkinter as tk
from tkinter import filedialog

from Code.AIModel.AIModel import *


class AIModelFunction:
    """
    AIModelFunction Class to be imported into AIModelWidget files. This class contains the tkinter widgets functions..
    """
    def __init__(self):
        """
        AIModelFunction Class Constructor that calls the AIModel Class and creates the list and variables used for the page.
        """
        self.aiModel = AIModel()

        self.input_column = ['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)',
                             'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)']

        self.input_independent_type = ''
        self.input_dependent_type = ''
        self.result = ''
        self.file_inputted = ''

        self.t_variable = tk.IntVar()
        self.ah_variable = tk.IntVar()
        self.rh_variable = tk.IntVar()

        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
        self.input3 = tk.StringVar()
        self.input4 = tk.StringVar()
        self.input5 = tk.StringVar()
        self.input6 = tk.StringVar()
        self.input7 = tk.StringVar()
        self.input8 = tk.StringVar()
        self.input9 = tk.StringVar()
        self.input10 = tk.StringVar()

        self.view_options = 'initial'
        self.prediction_options = False

    def button_config(self, method, t_Button, ah_Button, rh_Button):
        """
        A function that show or hide the buttons when called
        :param method: To either disable or enable the buttons
        :param t_Button: The button for dependent variable T
        :param ah_Button: The button for dependent variable AH
        :param rh_Button: The button for dependent variable RH
        :return: Show or hide the buttons
        """

        t_Button.deselect()
        ah_Button.deselect()
        rh_Button.deselect()

        if method == 'disabled':
            t_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            ah_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            rh_Button.config(text='', state='disabled', bd=0, indicatoron=False)

        elif method == 'normal':
            t_Button.config(text='T Variable\n(TEMPERATURE)', state='normal', bd=2, indicatoron=True)
            ah_Button.config(text='AH Variable\n(ABSOLUTE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)
            rh_Button.config(text='RH Variable\n(RELATIVE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)

    def change_input(self, method, frame, input_func, canvas, independent_label, dependent_label, result_label, file_entry,
                     entry_input, label_input, file_input, result, t_Button, ah_Button, rh_Button):
        """
        A function that changes the user's view when being clicked
        :param method: The user's input chosen from the input buttons
        :param frame: The frame of the tkinter widgets
        :param input_func: The function to create the tkinter widgets
        :param canvas: The canvas created for the frame
        :param independent_label: The heading for the independent variable
        :param dependent_label: The heading for the dependent variable
        :param result_label: The heading for the result
        :param file_entry: The entry for the name of the file that want to be saved
        :param entry_input: The list of input entry for single point prediction
        :param label_input: The list of label for single point prediction
        :param file_input: The list of widgets like buttons, label etc, for file prediction
        :param result: The list of widgets like treeview for the prediction result
        :param t_Button: The button for dependent variable T
        :param ah_Button: The button for dependent variable AH
        :param rh_Button: The button for dependent variable RH
        :return: Change the user's view based on the button the user clicks
        """
        if self.view_options == 'initial':
            canvas.destroy()

        elif self.view_options == 'single':
            self.single_destroy(entry_input, label_input)

        elif self.view_options == 'file':
            self.file_destroy(file_input)

        self.button_config('normal', t_Button, ah_Button, rh_Button)

        if self.prediction_options is True:
            result_label.config(text='')
            self.result_destroy(result)
            self.prediction_options = False

        if method == 'single':
            self.view_options = 'single'
            frame.config(pady=1)

            independent_label.config(text='ENTER THE INDEPENDENT FEATURES FOR SINGLE POINT INPUT')
            dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')

            file_entry.delete(0, 'end')

        elif method == 'file':
            self.view_options = 'file'
            frame.config(pady=3)

            independent_label.config(text='UPLOAD A FILE WITH INDEPENDENT FEATURES FOR FILE INPUT')
            dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')
            file_entry.delete(0, 'end')

    def check_save_file(self, frame, entry):
        """
        A function that checks the filename inputted by the user
        :param frame: The frame that puts the tkinter widgets
        :param entry: The file entry for the user to enter the filename
        :return: A boolean that checks the name of file and the file name string
        """
        file_name = entry.get()
        if file_name == '':
            label = tk.Label(frame, text='Please Enter a\nFilename to Save', foreground='red',
                             bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())
            file_passed = False
        else:
            file_passed = True

        return file_passed, file_name

    def save_file(self, frame, entry):
        """
        A function that saves the prediction to the user's computer
        :param frame: The frame that puts the tkinter widgets
        :param entry: The file entry for the user to enter the filename
        :return: An Excel file that has the predicted result
        """
        file_passed, file_name = self.check_save_file(frame, entry)

        if file_passed:
            if self.prediction_options is False:
                label = tk.Label(frame, text='Please Do the\nPrediction First', foreground='red', bg='lightskyblue')
                label.grid(row=13, column=2)
                label.after(3000, lambda: label.destroy())

            else:
                try:
                    path = self.aiModel.historical_data.create_folder('SavedPrediction')
                    self.result_df.to_excel(path + '/' + file_name + '.xlsx', index=False)
                    label = tk.Label(frame, text='Saving the\nPrediction', foreground='green',
                                     bg='lightskyblue')
                    label.grid(row=13, column=2)
                    label.after(3000, lambda: label.destroy())

                except:
                    label = tk.Label(frame, text='Please Enter a\n Valid Filename', foreground='red',
                                     bg='lightskyblue')
                    label.grid(row=13, column=2)
                    label.after(3000, lambda: label.destroy())

    def single_destroy(self, entry_input, label_input):
        """
        A function that destroy the tkinter widget for the single page viewing
        :param entry_input: The list of input entry for single point prediction
        :param label_input: The list of label for single point prediction
        :return: Clears the tkinter widget for single page viewing
        """
        for label in label_input:
            label.destroy()

        for entry in entry_input:
            entry.delete(0, 'end')
            entry.destroy()

    def file_destroy(self, file_input):
        """
        A function that destroy the tkinter widget for the file page viewing
        :param file_input: The list of widgets like buttons, label etc, for file prediction
        :return: Clears the tkinter widget for file page viewing
        """
        for file in file_input:
            file.destroy()

        self.file_inputted = ''

    def result_destroy(self, result):
        """
        A function that destroy the tkinter widget for the result frame
        :param result: The list of widgets like treeview for the prediction result
        :return: Clears the tkinter widget for result frame
        """
        for result in result:
            result.destroy()

    def get_file_data(self, frame, file_path, tree):
        """
        A function that gets the file inputs and show to the input treeview
        :param frame: The frame that puts the tkinter widgets
        :param file_path: The file path for the file inputted
        :param tree: The input treeview that will show the input value
        :return: A dataframe that consist the inputted data, treeview that shows the input value and the label for the file inputted
        """
        try:
            f_types = [('XLSX files', "*.xlsx"), ('All', "*.*")]
            file = filedialog.askopenfilename(filetypes=f_types)
            self.file_inputted = file

            self.input_dataframe = pd.read_excel(file)
            self.input_dataframe = self.input_dataframe[self.input_column]

            input_list = self.input_dataframe.to_numpy().tolist()

            failed = False

        except:
            label = tk.Label(frame, text='Please Enter a\nValid File', foreground='red', bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())

            failed = True

        if not failed:
            file_path.config(text=self.file_inputted)
            tree.delete(*tree.get_children())

            for i in range(0, 10):
                tree.heading(i, text=self.input_column[i])

            for item_list in input_list:
                values = [item for item in item_list]
                tree.insert("", 'end', values=values)

    def empty_check_entry(self, entry_list):
        """
        A function that checks if all the input entry are filled
        :param entry_list: The list of input entry
        :return: A boolean that checks all the input entry
        """
        empty = False
        if self.view_options == 'single':
            for entry in entry_list:
                if len(entry.get()) == 0:
                    empty = True

        return empty

    def numeric_check_entry(self, entry_list):
        """
        A function that checks if all the input entry are numerical only
        :param entry_list: The list of input entry
        :return: A boolean that checks all the values of input entry and the input entry the user's inputted
        """
        entry_empty = self.empty_check_entry(entry_list)
        entry_numeric = True
        entry_result = []

        if self.view_options == 'single':
            if not entry_empty:
                for entry in entry_list:
                    entry_value = entry.get()
                    entry_result.append(entry_value)

                    if entry_value.isalpha():
                        entry_numeric = False

        return entry_empty, entry_numeric, entry_result

    def check_file(self):
        """
        A function that checks if the user has inputted the file for prediction
        :return: A boolean that checks the file
        """
        file_input = True
        if self.view_options == 'file':
            if self.file_inputted == '':
                file_input = False

        return file_input

    def check_dependent_var(self):
        """
        A function that checks if the user has chose the dependent variable for prediction
        :return: A boolean that checks if any of the dependent variable is chosen
        """
        if self.t_variable.get() == 0 and self.ah_variable.get() == 0 and self.rh_variable.get() == 0:
            chose = False
        else:
            chose = True

        return chose

    def check_prediction(self, frame, entry_list):
        """
        A function that checks if the user has inputted and chose the variables correctly
        :param frame: The frame that puts the tkinter widgets
        :param entry_list: The list of input entry
        :return: A label for the user to know if any input fails, if passed, then give the input dataframe
        """
        entry_empty, entry_numeric, input_df = self.numeric_check_entry(entry_list)
        dependent_passed = self.check_dependent_var()
        file_passed = self.check_file()
        passed = False

        if entry_empty:
            label = tk.Label(frame, text='Please Enter\nIndependent\nFeature(s)', foreground='red',
                             bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())

        elif not entry_numeric:
            label = tk.Label(frame, text='Please Enter\nIndependent\nNumeric Value', foreground='red', bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())

        elif not file_passed:
            label = tk.Label(frame, text='Please Enter\nA File to\nPredict', foreground='red', bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())

        elif not dependent_passed:
            label = tk.Label(frame, text='Please Choose\nDependent\nFeature(s)', foreground='red', bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())
        else:
            passed = True

        return passed, input_df

    def do_prediction(self, input_df):
        """
        A function that process the inputted dataframe and predicts the inputs
        :param input_df: A dataframe that the user inputted for prediction
        :return: The length of the dataframe and the result of the prediction
        """
        if self.view_options == 'file':
            df = self.input_dataframe.copy()
            df[df == -200] = np.NaN

            self.result_df = self.input_dataframe.copy()
            self.result_df[self.result_df == -200] = np.NaN
            self.result_df = self.result_df.drop(columns=['NMHC(GT)'])
            self.result_df = self.result_df.dropna().reset_index(drop=True)

        elif self.view_options == 'single':
            df = pd.DataFrame([input_df], columns=self.input_column)
            df[df == -200] = np.NaN

            self.result_df = df.copy()
            self.result_df = self.result_df.drop(columns=['NMHC(GT)'])
            self.result_df = self.result_df.dropna().reset_index(drop=True)

        if self.t_variable.get() == 1:
            normalised_t_df = self.aiModel.T_normalise.transform(df)
            normalised_t_df = pd.DataFrame(normalised_t_df, columns=self.input_column)

            normalised_t_df = normalised_t_df.drop(columns=['NMHC(GT)'])
            normalised_t_df = normalised_t_df.dropna().reset_index(drop=True)

            input_t_df = self.aiModel.T_scaling.transform(normalised_t_df)
            input_t_df = pd.DataFrame(input_t_df, columns=self.aiModel.T_features)

            predicted_t = self.aiModel.T_model.predict(input_t_df)
            predicted_t = pd.DataFrame(predicted_t, columns=['T'])

            self.result_df = pd.concat([self.result_df, predicted_t], axis=1)

        if self.ah_variable.get() == 1:
            normalised_ah_df = self.aiModel.AH_normalise.transform(df)
            normalised_ah_df = pd.DataFrame(normalised_ah_df, columns=self.input_column)

            normalised_ah_df = normalised_ah_df.drop(columns=['NMHC(GT)'])
            input_ah_df = normalised_ah_df.dropna().reset_index(drop=True)

            predicted_ah = self.aiModel.AH_model.predict(input_ah_df)
            predicted_ah = pd.DataFrame(predicted_ah, columns=['AH'])

            self.result_df = pd.concat([self.result_df, predicted_ah], axis=1)

        if self.rh_variable.get() == 1:
            normalised_rh_df = self.aiModel.RH_normalise.transform(df)
            normalised_rh_df = pd.DataFrame(normalised_rh_df, columns=self.input_column)

            normalised_rh_df = normalised_rh_df.drop(columns=['NMHC(GT)'])
            normalised_rh_df = normalised_rh_df.dropna().reset_index(drop=True)

            input_rh_df = self.aiModel.RH_scaling.transform(normalised_rh_df)
            input_rh_df = pd.DataFrame(input_rh_df, columns=self.aiModel.RH_features)

            predicted_rh = self.aiModel.RH_model.predict(input_rh_df)
            predicted_rh = pd.DataFrame(predicted_rh, columns=['RH'])

            self.result_df = pd.concat([self.result_df, predicted_rh], axis=1)

        length = len(self.result_df.columns)

        return length, self.result_df

    def prediction(self, frame, result_label, prediction_func):
        """
        A function that shows the user the software is predicting and show the heading for the result
        :param frame: The frame that puts the tkinter widgets
        :param result_label: The heading for the result
        :param prediction_func: The function to create the prediction tkinter widgets
        :return: The predicted result and the result heading
        """
        label = tk.Label(frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
        label.grid(row=13, column=2)
        label.after(3000, lambda: label.destroy())

        self.result = 'RESULTS'
        self.prediction_options = True
        result_label.config(text=self.result)

    def clear_all(self, frame, canvas, canvas_func, independent_label, dependent_label, result_label,
                  file_entry, entry_input, label_input, file_input, result, t_Button, ah_Button, rh_Button):
        """
        A function that clears all the user's input and prediction, set the page back to the initial page view
        :param frame: The frame that puts the tkinter widgets
        :param canvas: The canvas created for the frame
        :param canvas_func: The function to create the tkinter widgets
        :param independent_label: The heading for the independent variable
        :param dependent_label: The heading for the dependent variable
        :param result_label: The heading for the result
        :param file_entry: The entry for the name of the file that want to be saved
        :param entry_input: The list of input entry for single point prediction
        :param label_input: The list of label for single point prediction
        :param file_input: The list of widgets like buttons, label etc, for file prediction
        :param result: The list of widgets like treeview for the prediction result
        :param t_Button: The button for dependent variable T
        :param ah_Button: The button for dependent variable AH
        :param rh_Button: The button for dependent variable RH
        :return: A clean initial page view that does not have any inputs and predictions
        """

        if self.view_options == 'single':
            self.single_destroy(entry_input, label_input)

        elif self.view_options == 'file':
            self.file_destroy(file_input)

        elif self.view_options == 'initial':
            canvas.destroy()

        self.view_options = 'initial'

        frame.config(pady=2)

        independent_label.config(text='')
        dependent_label.config(text='')

        file_entry.delete(0, 'end')

        if self.prediction_options is True:
            result_label.config(text='')
            self.result_destroy(result)
            self.prediction_options = False

        self.file_inputted = ''

        self.button_config('disabled', t_Button, ah_Button, rh_Button)

