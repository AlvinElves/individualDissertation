import tkinter as tk
from HistoricalData.HistoricalDataVis import *


class HistoricalPageFunction:
    """
    HistoricalPageFunction Class to be imported into HistoricalPageWidget files. This class contains the tkinter widgets functions.
    """
    def __init__(self):
        """
        HistoricalPageFunction Class Constructor that calls the HistoricalDataVisualisation Class and creates the list and variables
        used for the page.
        """
        self.historicalVis = HistoricalDataVisualisation()

        self.variable_text = ''
        self.visualisation_text = ''
        self.visualisation_type_text = ''
        self.visualise_variable = ['T (Temperature)', 'AH (Absolute Humidity)', 'RH (Relative Humidity)', 'CO(GT)', 'PT08.S1(CO)',
                                   'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)']

    def get_listbox(self, listbox):
        """
        A function that gets the item chose from the listbox.
        :param listbox: The listbox for the independent variable to visualise
        :return: A list of item the user clicked
        """
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

        return items

    def visualise(self, right_inside_frame, variable_label, visualisation_label, vis_type_label, listbox, entry, method):
        """
        A function that shows the visualisation that the user chose or saves the visualisation/dataset based on what the user clicks.
        :param right_inside_frame: The frame that puts the tkinter widgets
        :param variable_label: The label that tells the user to choose the item from the listbox
        :param visualisation_label: The label that shows the type fo visualisation chose
        :param vis_type_label: The label that tells the user the type of visualisation chose, normal or animated
        :param listbox: The listbox for the independent variable to visualise
        :param entry: The file entry for the user to enter the filename
        :param method: The type of saving the user wants, save dataset or visualisation
        :return: A matplotlib or plotly figure that shows the visualisation
        """
        features, checked_passed, file_name, file_passed = self.check_filename(right_inside_frame, listbox, entry, method)

        if checked_passed:
            file = ''
            if file_passed and method == 'save':
                path = self.historicalVis.historical_data.create_folder('SavedVisualisation')
                file = path + '/' + file_name + '.html'

            if self.visualisation_type_text == 'Animated' and file_passed:
                if self.visualisation_text == 'Line Graph':
                    dataset = self.historicalVis.animated_line_graph(features, method)

                elif self.visualisation_text == 'Bar Graph':
                    dataset = self.historicalVis.animated_bar_graph(features[0], method)

            elif self.visualisation_type_text == 'Normal' and file_passed:
                if self.visualisation_text == 'All Data':
                    dataset = self.historicalVis.plot_line_all(features, method, file)

                elif self.visualisation_text == 'Daily Data':
                    dataset = self.historicalVis.plot_Bar_by_Day(features[0], method, file)

                elif self.visualisation_text == 'Monthly Data':
                    dataset = self.historicalVis.plot_Bar_by_Month(features[0], method, file)

            if file_passed:
                if method == 'dataset':
                    label = tk.Label(right_inside_frame, text='Saving the Dataset', foreground='green', bg='lightskyblue')
                    label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                    label.after(3000, lambda: label.destroy())

                    path = self.historicalVis.historical_data.create_folder('SavedDataset')
                    try:
                        dataset.to_excel(path + '/' + file_name + '.xlsx', index=False)
                    except:
                        label = tk.Label(right_inside_frame, text='Please Enter a\n Valid Filename', foreground='red',
                                         bg='lightskyblue')
                        label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                        label.after(3000, lambda: label.destroy())

                elif method == 'save':
                    label = tk.Label(right_inside_frame, text='Saving the File', foreground='green', bg='lightskyblue')
                    label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                    label.after(3000, lambda: label.destroy())

                else:
                    label = tk.Label(right_inside_frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
                    label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                    label.after(3000, lambda: label.destroy())
                    self.clear(variable_label, visualisation_label, vis_type_label, listbox, entry)

    def check_filename(self, right_inside_frame, listbox, entry, method):
        """
        A function that checks the filename inputted by the user and saves the file to the user's computer.
        :param right_inside_frame: The frame that puts the tkinter widgets
        :param listbox: The listbox for the independent variable to visualise
        :param entry: The file entry for the user to enter the filename
        :param method: The type of saving the user wants, save dataset or visualisation
        :return: A list of listbox item, a boolean that checks if the filename is entered correctly for the saving buttons
        """
        features, checked_passed = self.check_visualise(right_inside_frame, listbox)
        file_name = entry.get()
        file_passed = False

        if checked_passed and (method == 'dataset' or method == 'save'):
            if file_name == '':
                label = tk.Label(right_inside_frame, text='Please Enter a\nFilename to Save', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                label.after(3000, lambda: label.destroy())
                file_passed = False

            else:
                if self.visualisation_type_text == 'Animated' and method == 'save':
                    label = tk.Label(right_inside_frame, text='Animated Graph is\nUnable to be Saved', foreground='red',
                                     bg='lightskyblue')
                    label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
                    label.after(3000, lambda: label.destroy())
                    file_passed = False
                else:
                    file_passed = True
        elif method == 'visualise':
            file_passed = True

        return features, checked_passed, file_name, file_passed

    def check_visualise(self, right_inside_frame, listbox):
        """
        A function that checks if the user had choose a type of visualisation to visualise.
        :param right_inside_frame: The frame that puts the tkinter widgets
        :param listbox: The listbox for the independent variable to visualise
        :return: A list of listbox item, a boolean that checks if any of the visualisation is chosen
        """
        variables = self.get_listbox(listbox)
        if self.visualisation_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
            label.after(3000, lambda: label.destroy())
            checked = False

        elif not variables:
            label = tk.Label(right_inside_frame, text='Please Choose the\nVariable(s) to Visualise', foreground='red',
                             bg='lightskyblue')
            label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
            label.after(3000, lambda: label.destroy())
            checked = False

        else:
            checked = True

        return variables, checked

    def choose_method(self, vis_type, method, variable_label, visualisation_label, vis_type_label, listbox, entry):
        """
        A function that changes the page view based on what the user chose from the buttons.
        :param vis_type: The type of visualisation the user clicked, normal or animated
        :param method: The type of visualisation the user clicked
        :param variable_label: The label that tells the user to choose the item from the listbox
        :param visualisation_label: The label that shows the type fo visualisation chose
        :param vis_type_label: The label that tells the user the type of visualisation chose, normal or animated
        :param listbox: The listbox for the independent variable to visualise
        :param entry: The entry for the name of the file that want to be saved
        :return: A page view based on the user inputs
        """
        listbox.delete(0, 'end')
        entry.delete(0, 'end')

        if vis_type == 'animated':
            self.visualisation_type_text = 'Animated'

        elif vis_type == 'normal':
            self.visualisation_type_text = 'Normal'

        if method == 'line':
            self.visualisation_text = 'Line Graph'
            self.variable_text = 'Choose the Variable(s)\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='multiple')

        elif method == 'bar':
            self.visualisation_text = 'Bar Graph'
            self.variable_text = 'Choose the Variable\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='single')

        elif method == 'all':
            self.visualisation_text = 'All Data'
            self.variable_text = 'Choose the Variable(s)\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='multiple')

        elif method == 'daily':
            self.visualisation_text = 'Daily Data'
            self.variable_text = 'Choose the Variable\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='single')

        elif method == 'monthly':
            self.visualisation_text = 'Monthly Data'
            self.variable_text = 'Choose the Variable\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='single')

        for item in self.visualise_variable:
            listbox.insert('end', item)

        variable_label.config(text=self.variable_text)
        visualisation_label.config(text=self.visualisation_text)
        vis_type_label.config(text=self.visualisation_type_text)

    def clear(self, variable_label, visualisation_label, vis_type_label, listbox, entry):
        """
        A function that clears all the user's input, set the page back to the initial page view.
        :param variable_label: The label that tells the user to choose the item from the listbox
        :param visualisation_label: The label that shows the type fo visualisation chose
        :param vis_type_label: The label that tells the user the type of visualisation chose, normal or animated
        :param listbox: The listbox for the independent variable to visualise
        :param entry: The entry for the name of the file that want to be saved
        :return: A clean initial page view that does not have any inputs
        """
        self.visualisation_text = ''
        self.variable_text = ''
        self.visualisation_type_text = ''

        variable_label.config(text=self.variable_text)
        visualisation_label.config(text=self.visualisation_text)
        vis_type_label.config(text=self.visualisation_type_text)

        listbox.delete(0, 'end')
        listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')

        entry.delete(0, 'end')
