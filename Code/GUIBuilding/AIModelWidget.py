import numpy as np

from Code.GUIBuilding.AIModelFunction import *
from tkinter import ttk


class AIModelWidget:
    def __init__(self):
        self.aiModelFunction = AIModelFunction()

    def inner_aimodel_widget(self, right_inside_frame):
        top_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        top_frame.grid(row=0, column=0, columnspan=5, rowspan=3)

        self.frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.frame.grid(row=3, column=0, columnspan=5, rowspan=4)
        self.frame.config(pady=2)

        dependent_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        dependent_frame.grid(row=8, column=0, columnspan=5, rowspan=2)

        self.result_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.result_frame.grid(row=10, column=0, columnspan=5, rowspan=3)

        bottom_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        bottom_frame.grid(row=13, column=0, columnspan=5)

        self.choose_input_type(row=0, frame=top_frame)
        self.draw_line(row=1, frame=top_frame)

        self.independent_label = self.heading(row=3, frame=top_frame, text=self.aiModelFunction.input_independent_type)

        self.draw_canvas(row=4, frame=self.frame)
        self.single_input(row=4, frame=self.frame)
        self.aiModelFunction.single_destroy(self.entry, self.label)

        self.file_input(row=4, frame=self.frame)
        self.aiModelFunction.file_destroy(self.file)

        self.dependent_label = self.heading(row=8, frame=dependent_frame,
                                            text=self.aiModelFunction.input_dependent_type)
        self.dependent_variable(row=9, frame=dependent_frame)

        self.draw_line(row=10, frame=self.result_frame)
        self.result_label = self.heading(row=11, frame=self.result_frame, text=self.aiModelFunction.result)

        self.draw_canvas2(row=12, frame=self.result_frame)
        self.prediction_result(row=12, frame=self.result_frame)
        self.aiModelFunction.result_destroy(self.result)

        self.final_button(row=13, frame=bottom_frame)

    def choose_input_type(self, row, frame):
        # Choose input type, single point or file
        input_type_text = tk.Label(frame, text="Input type: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        input_type_text.grid(row=row, column=0)

        single_point_button = tk.Button(frame, text="SINGLE PREDICTION", width=30, height=2,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                        activebackground='cornflowerblue',
                                        command=lambda: self.view('single'))
        single_point_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 45), columnspan=2)

        file_input_button = tk.Button(frame, text="FILE PREDICTION", width=30, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.view('file'))
        file_input_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 25), columnspan=2)

    @staticmethod
    def draw_line(row, frame):
        # Draw line
        top_canvas = tk.Canvas(frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def draw_canvas(self, row, frame):
        # Draw Canvas
        self.canvas = tk.Canvas(frame, width=750, height=144, bg='lightskyblue', highlightthickness=0)
        self.canvas.grid(row=row, columnspan=5, rowspan=2, pady=3)

    def draw_canvas2(self, row, frame):
        # Draw Canvas
        self.canvas2 = tk.Canvas(frame, width=750, height=130, bg='lightskyblue', highlightthickness=0)
        self.canvas2.grid(row=row, columnspan=5, pady=3)

    def heading(self, row, frame, text):
        input_type_label = tk.Label(frame, text=text, width=55, height=1,
                                    font=('Raleway', 12, 'bold'), bg='lightskyblue')
        input_type_label.grid(row=row, column=0, columnspan=5, pady=(1, 0))

        return input_type_label

    def single_input(self, row, frame):
        self.single_independent_feature_label(row=row, frame=frame)
        self.single_independent_feature_input(row=row + 1, frame=frame)

        self.entry = [self.input_1_entry, self.input_2_entry, self.input_3_entry, self.input_4_entry,
                      self.input_5_entry, self.input_6_entry, self.input_7_entry, self.input_8_entry,
                      self.input_9_entry, self.input_10_entry]
        self.label = [self.input_1, self.input_2, self.input_3, self.input_4, self.input_5,
                      self.input_6, self.input_7, self.input_8, self.input_9, self.input_10]

    def single_independent_feature_input(self, row, frame):
        # Independent Feature Input
        self.input_1_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_1_entry.grid(row=row, column=0)

        self.input_2_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_2_entry.grid(row=row, column=1)

        self.input_3_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_3_entry.grid(row=row, column=2)

        self.input_4_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_4_entry.grid(row=row, column=3)

        self.input_5_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_5_entry.grid(row=row, column=4)

        self.input_6_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_6_entry.grid(row=row + 2, column=0)

        self.input_7_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_7_entry.grid(row=row + 2, column=1)

        self.input_8_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_8_entry.grid(row=row + 2, column=2)

        self.input_9_entry = tk.Entry(frame, width=16,
                                      font=('Raleway', 10, 'bold'))
        self.input_9_entry.grid(row=row + 2, column=3)

        self.input_10_entry = tk.Entry(frame, width=16,
                                       font=('Raleway', 10, 'bold')
                                       )
        self.input_10_entry.grid(row=row + 2, column=4)

    def single_independent_feature_label(self, row, frame):
        # Independent Feature Label
        self.input_1 = tk.Label(frame, text='CO(GT)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_1.grid(row=row, column=0)

        self.input_2 = tk.Label(frame, text='PT08.S1(CO)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_2.grid(row=row, column=1)

        self.input_3 = tk.Label(frame, text='NMHC(GT)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_3.grid(row=row, column=2)

        self.input_4 = tk.Label(frame, text='C6H6(GT)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_4.grid(row=row, column=3)

        self.input_5 = tk.Label(frame, text='PT08.S2(NMHC)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_5.grid(row=row, column=4)

        self.input_6 = tk.Label(frame, text='NOx(GT)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_6.grid(row=row + 2, column=0)

        self.input_7 = tk.Label(frame, text='PT08.S3(NOx)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_7.grid(row=row + 2, column=1)

        self.input_8 = tk.Label(frame, text='NO2(GT)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_8.grid(row=row + 2, column=2)

        self.input_9 = tk.Label(frame, text='PT08.S4(NO2)', width=16, height=3,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.input_9.grid(row=row + 2, column=3)

        self.input_10 = tk.Label(frame, text='PT08.S5(O3)', width=16, height=3,
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

        self.file_path = tk.Label(frame, text=self.aiModelFunction.file_inputted, width=29, height=1,
                                  font=('Raleway', 12, 'bold', 'underline'), bg='white', anchor='w')
        self.file_path.grid(row=row, column=2, padx=(3, 65), columnspan=3, pady=(5, 0))

        self.input_view = ttk.Treeview(frame, selectmode='browse', height=4,
                                       show='headings',
                                       columns=['test'])
        self.input_view.grid(row=row + 1, column=0, columnspan=5, pady=(5, 0))

        self.input_view.column("0", width=600, anchor='c')

        self.input_scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.input_view.yview)
        self.input_view.configure(yscrollcommand=self.input_scrollbar.set)
        self.input_scrollbar.grid(row=row + 1, column=4, sticky='ns', padx=(59, 0), pady=(6, 1))

        self.file = [self.browse_file, self.file_text, self.file_path, self.input_view, self.input_scrollbar]

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

    def prediction_result(self, row, frame):
        result_view = ttk.Treeview(frame, selectmode='browse', height=5,
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

        vertical_scrollbar = tk.Scrollbar(frame, orient="vertical", command=result_view.yview)
        result_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.grid(row=row, column=4, sticky='ns', padx=(90, 0), pady=(11, 1))

        self.result = [result_view, vertical_scrollbar]

    def final_button(self, row, frame):
        clear_button = tk.Button(frame, text="Clear All", width=16,
                                 height=2, font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                 activebackground='cornflowerblue',
                                 command=lambda: self.clear())
        clear_button.grid(row=row, column=0, pady=(8, 5), padx=(5, 0))

        prediction_button = tk.Button(frame, text="Do Prediction", width=16, height=2,
                                      font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue',
                                      command=lambda: self.predict(frame, self.result_label))
        prediction_button.grid(row=row, column=1, pady=(8, 5), padx=(5, 5))

        label = tk.Label(frame, text="", width=16, height=2, bg='lightskyblue')
        label.grid(row=row, column=2, pady=(8, 5), padx=(0, 0))

        view_prediction_button = tk.Button(frame, text="View Prediction", width=16, height=2,
                                           font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                           activebackground='cornflowerblue')
        view_prediction_button.grid(row=row, column=3, pady=(8, 5), padx=(5, 5))

        self.row_label = tk.Label(frame, text='', width=10, height=3,
                                  font=('Raleway', 8, 'bold'), bg='lightskyblue', anchor='w')
        self.row_label.grid(row=row, column=4, pady=(8, 5), padx=(0, 70))

        self.row_entry = tk.Entry(frame, width=10, font=('Raleway', 10, 'bold'), bg='lightskyblue', relief='flat', cursor='arrow')
        self.row_entry.grid(row=row, column=4, pady=(8, 5), padx=(80, 0))

    def predict(self, frame, result_label):
        if self.aiModelFunction.view_options != 'initial':
            if self.aiModelFunction.prediction_options is False:
                self.aiModelFunction.prediction(frame, result_label, self.prediction_result(row=12, frame=self.result_frame))

    def view(self, method):
        if method == 'file':
            if self.aiModelFunction.view_options != 'file':
                self.aiModelFunction.change_input('file', self.frame, self.file_input(row=4, frame=self.frame),
                                                  self.canvas, self.independent_label, self.dependent_label, self.row_label,
                                                  self.row_entry, self.entry, self.label, self.file,
                                                  self.t_Button, self.ah_Button, self.rh_Button)
        elif method == 'single':
            if self.aiModelFunction.view_options != 'single':
                self.aiModelFunction.change_input('single', self.frame, self.single_input(row=4, frame=self.frame),
                                                  self.canvas, self.independent_label, self.dependent_label, self.row_label,
                                                  self.row_entry, self.entry, self.label, self.file,
                                                  self.t_Button, self.ah_Button, self.rh_Button)

    def clear(self):
        if self.aiModelFunction.view_options != 'initial':
            self.aiModelFunction.clear_all(self.frame, self.canvas, self.draw_canvas(row=4, frame=self.frame),
                                           self.independent_label, self.dependent_label, self.result_label, self.row_label,
                                           self.row_entry, self.entry, self.label, self.file, self.result, self.t_Button,
                                           self.ah_Button,  self.rh_Button)
