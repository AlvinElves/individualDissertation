import tkinter as tk


class AIModelFunction:
    def __init__(self):

        self.input_independent_type = ''
        self.input_dependent_type = ''
        self.result = ''
        self.file_inputted = ''

        self.t_variable = tk.IntVar()
        self.ah_variable = tk.IntVar()
        self.rh_variable = tk.IntVar()

        self.view_options = 'initial'
        self.prediction_options = False

    def button_config(self, method, t_Button, ah_Button, rh_Button):
        self.t_variable = 0
        self.ah_variable = 0
        self.rh_variable = 0

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

    def change_input(self, method, frame, input_func, canvas, independent_label, dependent_label, row_label, row_entry, entry_input,
                     label_input, file_input, t_Button, ah_Button, rh_Button):
        if self.view_options == 'initial':
            canvas.destroy()

        elif self.view_options == 'single':
            self.single_destroy(entry_input, label_input)

        elif self.view_options == 'file':
            self.file_destroy(file_input)

        self.button_config('normal', t_Button, ah_Button, rh_Button)

        if method == 'single':
            self.view_options = 'single'
            frame.config(pady=1)

            independent_label.config(text='ENTER THE INDEPENDENT FEATURES FOR SINGLE POINT INPUT')
            dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')
            row_label.config(text='')
            row_entry.config(bg='lightskyblue', relief='flat', cursor='arrow')

        elif method == 'file':
            self.view_options = 'file'
            frame.config(pady=3)

            independent_label.config(text='UPLOAD A FILE WITH INDEPENDENT FEATURES FOR FILE INPUT')
            dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')
            row_label.config(text='Enter the\nRow to View\nPrediction:')
            row_entry.config(bg='dodgerblue', relief='sunken', cursor='xterm')

    def single_destroy(self, entry_input, label_input):
        for label in label_input:
            label.destroy()

        for entry in entry_input:
            entry.destroy()

    def file_destroy(self, file_input):
        for file in file_input:
            file.destroy()

    def result_destroy(self, result):
        for result in result:
            result.destroy()

    def prediction(self, frame, result_label, pred_func):
        label = tk.Label(frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
        label.grid(row=13, column=2)
        label.after(3000, lambda: label.destroy())

        self.result = 'RESULTS'
        self.prediction_options = True
        result_label.config(text=self.result)

    def clear_all(self, frame, canvas, canvas_func, independent_label, dependent_label, result_label, row_label, row_entry,
                  entry_input, label_input, file_input, result, t_Button, ah_Button, rh_Button):

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
        result_label.config(text='')
        row_label.config(text='')
        row_entry.config(bg='lightskyblue', relief='flat', cursor='arrow')

        if self.prediction_options is True:
            result_label.config(text='')
            self.result_destroy(result)
            self.prediction_options = False

        self.file_inputted = ''

        self.button_config('disabled', t_Button, ah_Button, rh_Button)
