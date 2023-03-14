import tkinter as tk
from Code.LiveData.LiveDataVis import *


class LivePageFunction:
    def __init__(self):
        self.liveDataVis = LiveDataVisualisation()

        self.visualisation_type = ''
        self.choose_type_text = ''
        self.choose_pollutant_text = ''
        self.visualisation_text = ''
        self.map_text = ''
        self.last_updated_text = self.liveDataVis.live_data.last_updated

        self.pollutant_type = ['PM2.5', 'PM10', 'O3', 'NO2', ' SO2', 'CO', 'BC']

    def save_dataset(self, frame, entry, listbox):
        variables, vis_passed = self.check_visualise(frame, listbox)

        file_name = entry.get()

        if file_name == '':
            label = tk.Label(frame, text='Please Enter a\nFilename to Save', foreground='red',
                             bg='lightskyblue')
            label.grid(row=11, column=1)
            label.after(3000, lambda: label.destroy())

        else:
            file_passed = True
            path = self.liveDataVis.create_Folder('SavedDataset', False)

            if self.visualisation_text == 'Normal Map':
                dataset = self.liveDataVis.live_data.split_data_based_on_pollutant(self.liveDataVis.live_data.live_dataset,
                                                                                   variables)
            elif self.visualisation_text == 'Enhanced Map':
                dataset = self.liveDataVis.live_data.all_live_dataset

            try:
                dataset.to_excel(path + '/' + file_name + '.xlsx', index=False)

                label = tk.Label(frame, text='Saving the Dataset', foreground='green', bg='lightskyblue')
                label.grid(row=11, column=1)
                label.after(3000, lambda: label.destroy())
            except:
                label = tk.Label(frame, text='Please Enter a\n Valid Filename', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=11, column=1)
                label.after(3000, lambda: label.destroy())

    def visualise(self, frame, listbox):
        variables, vis_passed = self.check_visualise(frame, listbox)

        if self.map_text == 'Last Updated':
            map_type = 'last_updated'
        elif self.map_text == 'Most Frequent':
            map_type = 'most_frequent'

        if vis_passed:
            if self.visualisation_text == 'Bubble Map':
                self.liveDataVis.bubble_map(self.liveDataVis.live_data, variables)

            elif self.visualisation_text == 'Bar Graph On Map':
                self.liveDataVis.bar_graph_on_map(self.liveDataVis.live_data, variables, map_type)

            elif self.visualisation_text == 'Pie Chart On Map':
                self.liveDataVis.pie_chart_on_map(self.liveDataVis.live_data, variables, map_type)

            elif self.visualisation_text == 'Normal Map':
                if variables == self.pollutant_type[0]:
                    file = 'PM2_dot_5.html'

                elif variables == self.pollutant_type[1]:
                    file = 'PM10.html'

                elif variables == self.pollutant_type[2]:
                    file = 'O3.html'

                elif variables == self.pollutant_type[3]:
                    file = 'NO2.html'

                elif variables == self.pollutant_type[4]:
                    file = 'SO2.html'

                elif variables == self.pollutant_type[5]:
                    file = 'CO.html'

                elif variables == self.pollutant_type[6]:
                    file = 'BC.html'

                self.liveDataVis.display_Map(file)

            elif self.visualisation_text == 'Enhanced Map':
                self.liveDataVis.display_Map('Enhanced.html')

            label = tk.Label(frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
            label.grid(row=11, column=1)
            label.after(3000, lambda: label.destroy())

    def check_visualise(self, right_inside_frame, listbox):
        variables = self.get_listbox(listbox)
        if self.visualisation_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=11, column=1)
            label.after(3000, lambda: label.destroy())
            checked = False

        elif self.visualisation_text != 'Enhanced Map':
            if not variables:
                label = tk.Label(right_inside_frame, text='Please Choose the\nVariable(s) to Visualise', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=11, column=1)
                label.after(3000, lambda: label.destroy())
                checked = False
            else:
                if self.visualisation_text == 'Bar Graph On Map' or self.visualisation_text == 'Pie Chart On Map':
                    if self.map_text == '':
                        label = tk.Label(right_inside_frame, text='Please Choose the\nMap Type to Visualise',
                                         foreground='red',
                                         bg='lightskyblue')
                        label.grid(row=11, column=1)
                        label.after(3000, lambda: label.destroy())
                        checked = False
                    else:
                        checked = True
                else:
                    checked = True

        else:
            checked = True

        return variables, checked

    def get_listbox(self, listbox):
        index = listbox.curselection()

        if index:
            items = self.pollutant_type[index[0]]
        else:
            items = []

        return items

    def choose_method(self, method, visualisation_label, choose_type_label, type_label, pollutant_label, listbox, button1, button2):
        listbox.delete(0, 'end')
        if method != 'bar' and method != 'pie' and method != 'bubble' and method != 'normal':
            self.choose_type_text = ''
            self.choose_pollutant_text = ''
            listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
            button1.config(text='', state='disabled', bd=0)
            button2.config(text='', state='disabled', bd=0)

        else:
            listbox.config(state='normal', bg='white', highlightbackground='white')
            for item in self.pollutant_type:
                listbox.insert('end', item)

            self.choose_pollutant_text = 'Choose the Pollutant'

            if method == 'bar' or method == 'pie':
                self.choose_type_text = 'Choose the Graph\nOn Map Type'
                button1.config(text='Last Updated', state='normal', bd=2)
                button2.config(text='Most Frequent', state='normal', bd=2)
            else:
                self.choose_type_text = ''
                button1.config(text='', state='disabled', bd=0)
                button2.config(text='', state='disabled', bd=0)

        if method == 'normal':
            self.visualisation_text = 'Normal Map'

        elif method == 'enhanced':
            self.visualisation_text = 'Enhanced Map'

        elif method == 'bubble':
            self.visualisation_text = 'Bubble Map'

        elif method == 'bar':
            self.visualisation_text = 'Bar Graph On Map'

        elif method == 'pie':
            self.visualisation_text = 'Pie Chart On Map'

        self.map_text = ''
        visualisation_label.config(text=self.visualisation_text)
        choose_type_label.config(text=self.choose_type_text)
        type_label.config(text=self.map_text)
        pollutant_label.config(text=self.choose_pollutant_text)

    def choose_type(self, type_var, type_label):
        if type_var == 'last':
            self.map_text = 'Last Updated'
        elif type_var == 'most':
            self.map_text = 'Most Frequent'

        type_label.config(text=self.map_text)

    def clear(self, visualisation_label, choose_type_label, type_label, pollutant_label, listbox, button1, button2):
        self.choose_type_text = ''
        self.visualisation_text = ''
        self.map_text = ''
        self.choose_pollutant_text = ''

        visualisation_label.config(text=self.visualisation_text)
        choose_type_label.config(text=self.choose_type_text)
        type_label.config(text=self.map_text)
        pollutant_label.config(text=self.choose_pollutant_text)

        listbox.delete(0, 'end')
        listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
        button1.config(text='', state='disabled', bd=0)
        button2.config(text='', state='disabled', bd=0)


