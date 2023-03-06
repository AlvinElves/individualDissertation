import tkinter as tk


class AIModelFunction:
    def __init__(self):
        self.input_independent_type = ''
        self.input_dependent_type = ''

        self.t_variable = tk.IntVar()
        self.ah_variable = tk.IntVar()
        self.rh_variable = tk.IntVar()

        self.view_options = 'initial'

    def change_input(self, method, frame, independent_label, dependent_label, entry_input, label_input, t_Button, ah_Button, rh_Button):
        frame.config(pady=0)
        if method == 'single':
            if self.view_options == 'initial':
                self.view_options = 'single'

                self.entry_config('normal', entry_input, label_input)

                self.t_variable = 0
                self.ah_variable = 0
                self.rh_variable = 0
                t_Button.config(text='T Variable\n(TEMPERATURE)', state='normal', bd=2, indicatoron=True)
                ah_Button.config(text='AH Variable\n(ABSOLUTE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)
                rh_Button.config(text='RH Variable\n(RELATIVE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)

                independent_label.config(text='ENTER THE INDEPENDENT FEATURES FOR SINGLE POINT INPUT')
                dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')

            elif self.view_options == 'file':
                self.view_options = 'single'
                independent_label.config(text='ENTER THE INDEPENDENT FEATURES FOR SINGLE POINT INPUT')

                t_Button.deselect()
                ah_Button.deselect()
                rh_Button.deselect()

        elif method == 'file':
            if self.view_options == 'initial':
                self.view_options = 'file'

                t_Button.config(text='T Variable\n(TEMPERATURE)', state='normal', bd=2, indicatoron=True)
                ah_Button.config(text='AH Variable\n(ABSOLUTE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)
                rh_Button.config(text='RH Variable\n(RELATIVE\nHUMIDITY)', state='normal', bd=2, indicatoron=True)

                independent_label.config(text='UPLOAD A FILE WITH INDEPENDENT FEATURES FOR FILE INPUT')
                dependent_label.config(text='CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION')

            elif self.view_options == 'single':
                self.view_options = 'file'
                independent_label.config(text='UPLOAD A FILE WITH INDEPENDENT FEATURES FOR FILE INPUT')

                t_Button.deselect()
                ah_Button.deselect()
                rh_Button.deselect()

    def entry_config(self, method, entry_input, label_input):
        for entry in entry_input:
            entry.delete(0, 'end')
            if method == 'normal':
                entry.config(state='normal', bd=1, cursor='xterm')
            elif method == 'disabled':
                entry.config(state='disabled', bd=0, disabledbackground='lightskyblue', cursor='arrow')

        feature_name = ['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'PT08.S2(NMHC)',
                        'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)']

        if method == 'normal':
            for i in range(0, len(label_input)):
                label_input[i].config(text=feature_name[i])
        elif method == 'disabled':
            for label in label_input:
                label.config(text='')

    def clear_all(self, frame, independent_label, dependent_label, entry_input, label_input, t_Button, ah_Button, rh_Button):
        frame.config(pady=4)
        if self.view_options == 'single':
            self.view_options = 'initial'

            self.entry_config('disabled', entry_input, label_input)

            independent_label.config(text='')
            dependent_label.config(text='')
            self.t_variable = 0
            self.ah_variable = 0
            self.rh_variable = 0
            t_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            t_Button.deselect()
            ah_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            ah_Button.deselect()
            rh_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            rh_Button.deselect()

        elif self.view_options == 'file':
            self.view_options = 'initial'

            independent_label.config(text='')
            dependent_label.config(text='')

            self.t_variable = 0
            self.ah_variable = 0
            self.rh_variable = 0
            t_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            t_Button.deselect()
            ah_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            ah_Button.deselect()
            rh_Button.config(text='', state='disabled', bd=0, indicatoron=False)
            rh_Button.deselect()
