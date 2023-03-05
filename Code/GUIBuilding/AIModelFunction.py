import tkinter as tk


class AIModelFunction:
    def __init__(self):
        #self.input_independent_type = 'SINGLE POINT INPUT'
        self.input_independent_type = 'FILE INPUT'
        self.input_dependent_type = 'CHOOSE THE DEPENDENT VARIABLE FOR PREDICTION'

        self.t_variable = tk.IntVar()
        self.ah_variable = tk.IntVar()
        self.rh_variable = tk.IntVar()
