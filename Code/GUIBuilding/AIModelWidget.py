import numpy as np

from Code.GUIBuilding.AIModelFunction import *
from tkinter import ttk


class AIModelWidget:
    def __init__(self):
        self.aiModelFunction = AIModelFunction()

    def inner_aimodel_widget(self, right_inside_frame):
        self.choose_input_type(row=0, right_inside_frame=right_inside_frame)
        self.draw_line(row=1, right_inside_frame=right_inside_frame)

        self.frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.frame.grid(row=2, column=0, columnspan=5, rowspan=8)
        self.frame.config(pady=4)

        self.independent_label = self.heading(row=3, frame=self.frame, text=self.aiModelFunction.input_independent_type)

        #self.draw_canvas(row=4, frame=self.frame)
        self.single_input(row=4, frame=self.frame)
        #self.file_input(row=4, frame=self.frame)

        self.dependent_label = self.heading(row=8, frame=self.frame, text=self.aiModelFunction.input_dependent_type)
        self.dependent_variable(row=9, frame=self.frame)

        self.draw_line(row=10, right_inside_frame=right_inside_frame)
        self.heading(row=11, frame=right_inside_frame, text='RESULTS')
        self.prediction_result(row=12, right_inside_frame=right_inside_frame)
        self.final_button(row=13, right_inside_frame=right_inside_frame)

    def choose_input_type(self, row, right_inside_frame):
        # Choose input type, single point or file
        input_type_text = tk.Label(right_inside_frame, text="Input type: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_type_text.grid(row=row, column=0)

        single_point_button = tk.Button(right_inside_frame, text="SINGLE PREDICTION", width=30, height=2,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                        activebackground='cornflowerblue',
                                        command=lambda: self.aiModelFunction.change_input('single', self.frame,
                                                                                          self.independent_label,
                                                                                          self.dependent_label,
                                                                                          self.entry,
                                                                                          self.label,
                                                                                          self.t_Button, self.ah_Button,
                                                                                          self.rh_Button))
        single_point_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 45), columnspan=2)

        file_input_button = tk.Button(right_inside_frame, text="FILE PREDICTION", width=30, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.aiModelFunction.change_input('file', self.frame,
                                                                                        self.independent_label,
                                                                                        self.dependent_label,
                                                                                        self.entry,
                                                                                        self.label, self.t_Button,
                                                                                        self.ah_Button, self.rh_Button))
        file_input_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 25), columnspan=2)

    @staticmethod
    def draw_line(row, right_inside_frame):
        # Draw line
        top_canvas = tk.Canvas(right_inside_frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def draw_canvas(self, row, frame):
        # Draw Canvas
        self.canvas = tk.Canvas(frame, width=750, height=144, bg='lightskyblue', highlightthickness=0)
        self.canvas.grid(row=row, columnspan=5, rowspan=2)

    def heading(self, row, frame, text):
        input_type_label = tk.Label(frame, text=text, width=55, height=1,
                                    font=('Raleway', 12, 'bold'), bg='lightskyblue')
        input_type_label.grid(row=row, column=0, columnspan=5, pady=(3, 0))

        return input_type_label

    def single_input(self, row, frame):
        self.single_independent_feature_label(row=row, frame=frame)
        self.single_independent_feature_input(row=row+1, frame=frame)

        self.entry = [self.input_1_entry, self.input_2_entry, self.input_3_entry, self.input_4_entry,
                      self.input_5_entry, self.input_6_entry, self.input_7_entry, self.input_8_entry,
                      self.input_9_entry, self.input_10_entry]
        self.label = [self.input_1, self.input_2, self.input_3, self.input_4, self.input_5,
                      self.input_6, self.input_7, self.input_8, self.input_9, self.input_10]

    def single_independent_feature_input(self, row, frame):
        # Independent Feature Input
        self.input_1_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_1_entry.grid(row=row, column=0)

        self.input_2_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_2_entry.grid(row=row, column=1)

        self.input_3_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_3_entry.grid(row=row, column=2)

        self.input_4_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_4_entry.grid(row=row, column=3)

        self.input_5_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_5_entry.grid(row=row, column=4)

        self.input_6_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_6_entry.grid(row=row + 2, column=0)

        self.input_7_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_7_entry.grid(row=row + 2, column=1)

        self.input_8_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_8_entry.grid(row=row + 2, column=2)

        self.input_9_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                      disabledbackground='lightskyblue', cursor='arrow')
        self.input_9_entry.grid(row=row + 2, column=3)

        self.input_10_entry = tk.Entry(frame, width=16,
                                       font=('Raleway', 10, 'bold'), state='disabled', bd=0,
                                       disabledbackground='lightskyblue', cursor='arrow')
        self.input_10_entry.grid(row=row + 2, column=4)

    def single_independent_feature_label(self, row, frame):
        # Independent Feature Label
        self.input_1 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_1.grid(row=row, column=0)

        self.input_2 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_2.grid(row=row, column=1)

        self.input_3 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_3.grid(row=row, column=2)

        self.input_4 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_4.grid(row=row, column=3)

        self.input_5 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_5.grid(row=row, column=4)

        self.input_6 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_6.grid(row=row + 2, column=0)

        self.input_7 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_7.grid(row=row + 2, column=1)

        self.input_8 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_8.grid(row=row + 2, column=2)

        self.input_9 = tk.Label(frame, text='', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_9.grid(row=row + 2, column=3)

        self.input_10 = tk.Label(frame, text='', width=16, height=3,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_10.grid(row=row + 2, column=4)

    def file_input(self, row, frame):
        self.browse_file = tk.Button(frame, text="Browse File", width=15, height=1,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue')
        self.browse_file.grid(row=row, column=0, padx=(65, 10), pady=(5, 0))

        self.file_text = tk.Label(frame, text='Inputted File Path: ', width=15, height=1,
                                  font=('Raleway', 12, 'bold'), bg='lightskyblue')
        self.file_text.grid(row=row, column=1, padx=(3, 3), pady=(5, 0))

        self.file_path = tk.Label(frame, text='Inputted File Path:', width=29, height=1,
                                  font=('Raleway', 12, 'bold', 'underline'), bg='white', anchor='w')
        self.file_path.grid(row=row, column=2, padx=(3, 65), columnspan=3, pady=(5, 0))

        input_view = ttk.Treeview(frame, selectmode='browse', height=4,
                                  show='headings',
                                  columns=['test'])
        input_view.grid(row=row + 1, column=0, columnspan=5, pady=(5, 0))

        input_view.column("0", width=600, anchor='c')

        input_scrollbar = tk.Scrollbar(frame, orient="vertical", command=input_view.yview)
        input_view.configure(yscrollcommand=input_scrollbar.set)
        input_scrollbar.grid(row=row + 1, column=4, sticky='ns', padx=(52, 0), pady=(6, 1))

    def dependent_variable(self, row, frame):
        self.t_Button = tk.Checkbutton(frame, text='', bd=0, indicatoron=False,
                                       font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                       variable=self.aiModelFunction.t_variable, onvalue=1, offvalue=0,
                                       height=3, width=15)
        self.t_Button.grid(row=row, column=0, pady=(3, 3))

        self.ah_Button = tk.Checkbutton(frame, text='', bd=0, indicatoron=False,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                        variable=self.aiModelFunction.ah_variable, onvalue=1, offvalue=0,
                                        height=3, width=15)
        self.ah_Button.grid(row=row, column=2, pady=(3, 3))

        self.rh_Button = tk.Checkbutton(frame, text='', bd=0, indicatoron=False,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                        variable=self.aiModelFunction.rh_variable, onvalue=1, offvalue=0,
                                        height=3, width=15)
        self.rh_Button.grid(row=row, column=4, pady=(3, 3))

    def prediction_result(self, row, right_inside_frame):
        result_view = ttk.Treeview(right_inside_frame, selectmode='browse', height=5,
                                   show='headings',
                                   columns=['test'])
        result_view.grid(row=row, column=0, columnspan=5, pady=(10, 0))

        # result_view['columns'] = ('test','test')

        result_view.column("0", width=600, anchor='c')
        # result_view.column("1", width=45, anchor='c')
        # result_view.column("2", width=45, anchor='c')
        # result_view.column("3", width=45, anchor='c')
        # result_view.column("4", width=45, anchor='c')
        # result_view.column("5", width=45, anchor='c')
        # result_view.column("6", width=45, anchor='c')
        # result_view.column("7", width=45, anchor='c')
        # result_view.column("8", width=45, anchor='c')
        # result_view.column("9", width=45, anchor='c')
        # result_view.column("10", width=45, anchor='c')
        # result_view.column("11", width=45, anchor='se')
        # result_view.column("12", width=45, anchor='se')

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

        # result_view.destroy()
        # vertical_scrollbar.destroy()

    def final_button(self, row, right_inside_frame):
        clear_button = tk.Button(right_inside_frame, text="Clear All", width=16,
                                 height=2, font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                 activebackground='cornflowerblue',
                                 command=lambda: self.aiModelFunction.clear_all(self.frame, self.independent_label,
                                                                                self.dependent_label,
                                                                                self.entry,
                                                                                self.label, self.t_Button,
                                                                                self.ah_Button, self.rh_Button))
        clear_button.grid(row=row, column=0, pady=(8, 5), padx=(2, 21), columnspan=2)

        prediction_button = tk.Button(right_inside_frame, text="Do Prediction", width=16, height=2,
                                      font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue')
        prediction_button.grid(row=row, column=2, pady=(8, 5), padx=(2, 2))

        view_prediction_button = tk.Button(right_inside_frame, text="View Prediction", width=16, height=2,
                                           font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                           activebackground='cornflowerblue')
        view_prediction_button.grid(row=row, column=3, pady=(8, 5), padx=(25, 2), columnspan=2)
