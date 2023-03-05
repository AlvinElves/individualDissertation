import numpy as np

from Code.GUIBuilding.AIModelFunction import *
from tkinter import ttk


class AIModelWidget:
    def __init__(self):
        self.aiModelFunction = AIModelFunction()

    def inner_aimodel_widget(self, right_inside_frame):
        self.choose_input_type(row=0, right_inside_frame=right_inside_frame)
        self.draw_line(row=1, right_inside_frame=right_inside_frame)

        self.heading(row=3, right_inside_frame=right_inside_frame, text=self.aiModelFunction.input_independent_type)
        self.independent_variable_label(row=4, right_inside_frame=right_inside_frame)
        self.independent_variable_input(row=5, right_inside_frame=right_inside_frame)
        self.heading(row=8, right_inside_frame=right_inside_frame, text=self.aiModelFunction.input_dependent_type)
        self.dependent_variable(row=9, right_inside_frame=right_inside_frame)
        self.draw_line(row=10, right_inside_frame=right_inside_frame)

        self.heading(row=11, right_inside_frame=right_inside_frame, text='RESULTS')
        self.prediction_result(row=12, right_inside_frame=right_inside_frame)
        self.final_button(row=13, right_inside_frame=right_inside_frame)

    def choose_input_type(self, row, right_inside_frame):
        # Choose input type, single point or file
        input_type_text = tk.Label(right_inside_frame, text="Input type: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_type_text.grid(row=row, column=0)

        single_point_button = tk.Button(right_inside_frame, text="SINGLE PREDICTION", width=30, height=2,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                        activebackground='cornflowerblue')
        single_point_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 45), columnspan=2)

        file_input_button = tk.Button(right_inside_frame, text="FILE PREDICTION", width=30, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue')
        file_input_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 25), columnspan=2)

    @staticmethod
    def draw_line(row, right_inside_frame):
        # Draw line
        top_canvas = tk.Canvas(right_inside_frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    @staticmethod
    def heading(row, right_inside_frame, text):
        input_type_label = tk.Label(right_inside_frame, text=text, width=50, height=1,
                                    font=('Raleway', 12, 'bold'), bg='lightskyblue')
        input_type_label.grid(row=row, column=0, columnspan=5, pady=(3, 0))

    def independent_variable_input(self, row, right_inside_frame):
        # Independent Feature Input
        input_1_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_1_entry.grid(row=row, column=0, padx=(2, 3))

        input_2_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_2_entry.grid(row=row, column=1, padx=(0, 3))

        input_3_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_3_entry.grid(row=row, column=2)

        input_4_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_4_entry.grid(row=row, column=3, padx=(3, 3))

        input_5_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_5_entry.grid(row=row, column=4, padx=(0, 3))

        input_6_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_6_entry.grid(row=row + 2, column=0, padx=(2, 3))

        input_7_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_7_entry.grid(row=row + 2, column=1, padx=(0, 3))

        input_8_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_8_entry.grid(row=row + 2, column=2)

        input_9_entry = tk.Entry(right_inside_frame, width=16,
                                 font=('Raleway', 10, 'bold'), bg='white')
        input_9_entry.grid(row=row + 2, column=3, padx=(3, 3))

        input_10_entry = tk.Entry(right_inside_frame, width=16,
                                  font=('Raleway', 10, 'bold'), bg='white')
        input_10_entry.grid(row=row + 2, column=4, padx=(0, 3))

    def independent_variable_label(self, row, right_inside_frame):
        # Independent Feature Label
        input_1 = tk.Label(right_inside_frame, text='CO(GT)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_1.grid(row=row, column=0, padx=(2, 3))

        input_2 = tk.Label(right_inside_frame, text='PT08.S1(CO)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_2.grid(row=row, column=1, padx=(0, 3))

        input_3 = tk.Label(right_inside_frame, text='NMHC(GT)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_3.grid(row=row, column=2)

        input_4 = tk.Label(right_inside_frame, text='C6H6(GT)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_4.grid(row=row, column=3, padx=(3, 3))

        input_5 = tk.Label(right_inside_frame, text='PT08.S2(NMHC)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_5.grid(row=row, column=4, padx=(0, 3))

        input_6 = tk.Label(right_inside_frame, text='NOx(GT)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_6.grid(row=row + 2, column=0, padx=(2, 3))

        input_7 = tk.Label(right_inside_frame, text='PT08.S3(NOx)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_7.grid(row=row + 2, column=1, padx=(0, 3))

        input_8 = tk.Label(right_inside_frame, text='NO2(GT)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_8.grid(row=row + 2, column=2)

        input_9 = tk.Label(right_inside_frame, text='PT08.S4(NO2)', width=16, height=3,
                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_9.grid(row=row + 2, column=3, padx=(3, 3))

        input_10 = tk.Label(right_inside_frame, text='PT08.S5(O3)', width=16, height=3,
                            font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_10.grid(row=row + 2, column=4, padx=(0, 3))

    def dependent_variable(self, row, right_inside_frame):
        t_Button = tk.Checkbutton(right_inside_frame, text='T Variable\n(TEMPERATURE)',
                                  font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                  variable=self.aiModelFunction.t_variable, onvalue=1, offvalue=0,
                                  height=3, width=15)
        t_Button.grid(row=row, column=0, pady=(3, 3))

        ah_Button = tk.Checkbutton(right_inside_frame, text='AH Variable\n(ABSOLUTE\nHUMIDITY)',
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   variable=self.aiModelFunction.ah_variable, onvalue=1, offvalue=0,
                                   height=3, width=15)
        ah_Button.grid(row=row, column=2, pady=(3, 3))

        rh_Button = tk.Checkbutton(right_inside_frame, text='RH Variable\n(RELATIVE\nHUMIDITY)',
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   variable=self.aiModelFunction.rh_variable, onvalue=1, offvalue=0,
                                   height=3, width=15)
        rh_Button.grid(row=row, column=4, pady=(3, 3))

    def prediction_result(self, row, right_inside_frame):
        result_view = ttk.Treeview(right_inside_frame, selectmode='browse', height=5,
                                   show='headings',
                                   columns=['test'])
        result_view.grid(row=row, column=0, columnspan=5, pady=(10, 0))

        #result_view['columns'] = ('test','test')

        result_view.column("0", width=600, anchor='c')
        #result_view.column("1", width=45, anchor='c')
        #result_view.column("2", width=45, anchor='c')
        #result_view.column("3", width=45, anchor='c')
        #result_view.column("4", width=45, anchor='c')
        #result_view.column("5", width=45, anchor='c')
        #result_view.column("6", width=45, anchor='c')
        #result_view.column("7", width=45, anchor='c')
        #result_view.column("8", width=45, anchor='c')
        #result_view.column("9", width=45, anchor='c')
        #result_view.column("10", width=45, anchor='c')
        #result_view.column("11", width=45, anchor='se')
        #result_view.column("12", width=45, anchor='se')

        """
        result_view.heading("0", text="Name")
        result_view.heading("1", text="Sex")
        result_view.heading("2", text="Age")
        result_view.heading("3", text="Sex")
        result_view.heading("4", text="Age")
        result_view.heading("5", text="Sex")
        result_view.heading("6", text="Last")
        result_view.heading("7", text="Age")
        result_view.heading("8", text="Sex")
        result_view.heading("9", text="Last")
        result_view.heading("10", text="Age")
        #result_view.heading("11", text="Sex")
        #result_view.heading("12", text="Last")"""

        vertical_scrollbar = tk.Scrollbar(right_inside_frame, orient="vertical", command=result_view.yview)
        result_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.grid(row=row, column=4, sticky='ns', padx=(2, 0), pady=(11, 1))

        #result_view.destroy()
        #vertical_scrollbar.destroy()

    def final_button(self, row, right_inside_frame):
        clear_button = tk.Button(right_inside_frame, text="Clear All", width=16,
                                 height=2, font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                 activebackground='cornflowerblue')
        clear_button.grid(row=row, column=0, pady=(8, 5), padx=(2, 21), columnspan=2)

        prediction_button = tk.Button(right_inside_frame, text="Do Prediction", width=16, height=2,
                                      font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue')
        prediction_button.grid(row=row, column=2, pady=(8, 5), padx=(2, 2))

        view_prediction_button = tk.Button(right_inside_frame, text="View Prediction", width=16, height=2,
                                      font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue')
        view_prediction_button.grid(row=row, column=3, pady=(8, 5), padx=(25, 2), columnspan=2)
