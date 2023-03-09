import tkinter as tk


class HistoricalPageFunction:
    def __init__(self):
        self.variable_text = ''
        self.visualisation_text = ''
        self.visualisation_type_text = ''

    def visualise(self, right_inside_frame, method):
        if self.visualisation_text == '':
            label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                             bg='lightskyblue')
            label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
            label.after(3000, lambda: label.destroy())
        else:
            label = tk.Label(right_inside_frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
            label.grid(row=10, column=1, padx=(10, 0), pady=(0, 5))
            label.after(3000, lambda: label.destroy())

    def choose_method(self, vis_type, method, variable_label, visualisation_label, vis_type_label, listbox):
        listbox.delete(0, 'end')

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

        elif method == 'pie':
            self.visualisation_text = 'Pie Chart'
            self.variable_text = 'Choose the Variable\nto Visualise'
            listbox.config(state='normal', bg='white', highlightbackground='white', selectmode='single')

        for i in range(0, 51):
            listbox.insert('end', "test" + str(i))

        variable_label.config(text=self.variable_text)
        visualisation_label.config(text=self.visualisation_text)
        vis_type_label.config(text=self.visualisation_type_text)

    def clear(self, variable_label, visualisation_label, vis_type_label, listbox):
        self.visualisation_text = ''
        self.variable_text = ''
        self.visualisation_type_text = ''

        variable_label.config(text=self.variable_text)
        visualisation_label.config(text=self.visualisation_text)
        vis_type_label.config(text=self.visualisation_type_text)

        listbox.delete(0, 'end')
        listbox.config(state='disabled', bg='lightskyblue', highlightbackground='lightskyblue')
