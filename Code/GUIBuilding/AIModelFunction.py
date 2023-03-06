import tkinter as tk


class AIModelFunction:
    def __init__(self):
        self.input_independent_type = 'ENTER THE INDEPENDENT FEATURES FOR SINGLE POINT INPUT'
        #self.input_independent_type = 'UPLOAD A FILE WITH INDEPENDENT FEATURES FOR FILE INPUT'
        self.input_dependent_type = 'CHOOSE THE DEPENDENT FEATURE(S) FOR PREDICTION'

        self.t_variable = tk.IntVar()
        self.ah_variable = tk.IntVar()
        self.rh_variable = tk.IntVar()
