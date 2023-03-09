import tkinter as tk


class LivePageFunction:
    def __init__(self):
        self.choose_type_text = ''
        self.visualisation_text = ''
        self.map_text = ''
        self.last_updated_text = ''

    def visualise(self, frame, method):
        if self.visualisation_text == '':
            label = tk.Label(frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=10, column=1)
            label.after(3000, lambda: label.destroy())
        else:
            label = tk.Label(frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
            label.grid(row=10, column=1)
            label.after(3000, lambda: label.destroy())

    def choose_method(self, method, visualisation_label, choose_type_label, type_label, button1, button2):
        if method != 'bar' and method != 'pie':
            self.choose_type_text = ''
            button1.config(text='', state='disabled', bd=0)
            button2.config(text='', state='disabled', bd=0)
        else:
            self.choose_type_text = 'Choose the Graph\nOn Map Type'
            button1.config(text='Last Updated', state='normal', bd=2)
            button2.config(text='Most Frequent', state='normal', bd=2)

        if method == 'pm2.5':
            self.visualisation_text = 'PM2.5 Map'

        elif method == 'pm10':
            self.visualisation_text = 'PM10 Map'

        elif method == 'o3':
            self.visualisation_text = 'O3 Map'

        elif method == 'no2':
            self.visualisation_text = 'NO2 Map'

        elif method == 'so2':
            self.visualisation_text = 'SO2 Map'

        elif method == 'co':
            self.visualisation_text = 'CO Map'

        elif method == 'bc':
            self.visualisation_text = 'BC Map'

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

    def choose_type(self, type_var, type_label):
        if type_var == 'last':
            self.map_text = 'Last Updated'
        elif type_var == 'most':
            self.map_text = 'Most Frequent'

        type_label.config(text=self.map_text)

    def clear(self, visualisation_label, choose_type_label, type_label, button1, button2):
        self.choose_type_text = ''
        self.visualisation_text = ''
        self.map_text = ''

        visualisation_label.config(text=self.visualisation_text)
        choose_type_label.config(text=self.choose_type_text)
        type_label.config(text=self.map_text)

        button1.config(text='', state='disabled', bd=0)
        button2.config(text='', state='disabled', bd=0)


