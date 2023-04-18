from GUIBuilding.AIModelFunction import *
from tkinter import ttk


class AIModelWidget:
    """
    AIModelWidget Class to be imported into GUI files. This class contains the tkinter widgets like button, label etc.
    """
    def __init__(self):
        """
        AIModelWidget Class Constructor that calls the AIModelFunction Class.
        """
        self.aiModelFunction = AIModelFunction()

    def inner_aimodel_widget(self, right_inside_frame):
        """
        A function that creates the inner right side of the GUI that contains all the tkinter widgets.
        :param right_inside_frame: Right inner frame that puts the tkinter widgets
        :return: The labels, buttons, entry, treeviews and frame on the frame
        """
        top_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        top_frame.grid(row=0, column=0, columnspan=5, rowspan=3)

        self.frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.frame.grid(row=3, column=0, columnspan=5, rowspan=4)
        self.frame.config(pady=2)

        dependent_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        dependent_frame.grid(row=8, column=0, columnspan=5, rowspan=2)

        self.result_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.result_frame.grid(row=10, column=0, columnspan=5, rowspan=3)

        self.bottom_frame = tk.Frame(right_inside_frame, width=767, height=268, bg='lightskyblue')
        self.bottom_frame.grid(row=13, column=0, columnspan=5)

        self.choose_input_type(row=0, frame=top_frame)
        self.draw_line(row=1, frame=top_frame)

        self.independent_label = self.heading(row=3, frame=top_frame, text=self.aiModelFunction.input_independent_type)

        self.draw_canvas(row=4, frame=self.frame)
        self.single_input(row=4, frame=self.frame)
        self.aiModelFunction.single_destroy(self.entry, self.label)

        self.file_input(row=4, frame=self.frame, frame2=self.bottom_frame)
        self.aiModelFunction.file_destroy(self.file)

        self.dependent_label = self.heading(row=8, frame=dependent_frame,
                                            text=self.aiModelFunction.input_dependent_type)
        self.dependent_variable(row=9, frame=dependent_frame)

        self.draw_line(row=10, frame=self.result_frame)
        self.result_label = self.heading(row=11, frame=self.result_frame, text=self.aiModelFunction.result)

        self.draw_canvas2(row=12, frame=self.result_frame)
        self.prediction_result(row=12, frame=self.result_frame, number=0, result_df=None)
        self.aiModelFunction.result_destroy(self.result)

        self.final_button(row=13, frame=self.bottom_frame)

    def choose_input_type(self, row, frame):
        """
        A function that creates the button and label to allow the user to choose the type of input.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The label and buttons on the frame
        """
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
        """
        A function that creates a horizontal line on the frame.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: A horizontal line across the frame
        """
        # Draw line
        top_canvas = tk.Canvas(frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def draw_canvas(self, row, frame):
        """
        A function that creates a canvas on the frame.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: A 2 row-span canvas on the frame
        """
        # Draw Canvas
        self.canvas = tk.Canvas(frame, width=750, height=144, bg='lightskyblue', highlightthickness=0)
        self.canvas.grid(row=row, columnspan=5, rowspan=2, pady=3)

    def draw_canvas2(self, row, frame):
        """
        A function that creates a canvas on the frame.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: A one row canvas on the frame
        """
        # Draw Canvas
        self.canvas2 = tk.Canvas(frame, width=750, height=130, bg='lightskyblue', highlightthickness=0)
        self.canvas2.grid(row=row, columnspan=5, pady=3)

    def heading(self, row, frame, text):
        """
        A function that creates a subtitle on the frame
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :param text: The title of the heading
        :return: The page subtitle on the frame
        """
        # A label that shows the heading for each section
        input_type_label = tk.Label(frame, text=text, width=55, height=1,
                                    font=('Raleway', 12, 'bold'), bg='lightskyblue')
        input_type_label.grid(row=row, column=0, columnspan=5, pady=(1, 0))

        return input_type_label

    def single_input(self, row, frame):
        """
        A function that creates the button and label to allow the user to input the single prediction.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The label and buttons on the frame
        """
        # Entry and Label that allows the user to enter the input for prediction
        self.single_independent_feature_label(row=row, frame=frame)
        self.single_independent_feature_input(row=row + 1, frame=frame)

        self.entry = [self.input_1_entry, self.input_2_entry, self.input_3_entry, self.input_4_entry,
                      self.input_5_entry, self.input_6_entry, self.input_7_entry, self.input_8_entry,
                      self.input_9_entry, self.input_10_entry]
        self.label = [self.input_1, self.input_2, self.input_3, self.input_4, self.input_5,
                      self.input_6, self.input_7, self.input_8, self.input_9, self.input_10]

    def single_independent_feature_input(self, row, frame):
        """
        A function that creates the label for the single prediction.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The list of label on the frame
        """
        # Independent Feature Input
        self.input_1_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input1,
                                      font=('Raleway', 10, 'bold'))
        self.input_1_entry.grid(row=row, column=0)

        self.input_2_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input2,
                                      font=('Raleway', 10, 'bold'))
        self.input_2_entry.grid(row=row, column=1)

        self.input_3_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input3,
                                      font=('Raleway', 10, 'bold'))
        self.input_3_entry.grid(row=row, column=2)

        self.input_4_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input4,
                                      font=('Raleway', 10, 'bold'))
        self.input_4_entry.grid(row=row, column=3)

        self.input_5_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input5,
                                      font=('Raleway', 10, 'bold'))
        self.input_5_entry.grid(row=row, column=4)

        self.input_6_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input6,
                                      font=('Raleway', 10, 'bold'))
        self.input_6_entry.grid(row=row + 2, column=0)

        self.input_7_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input7,
                                      font=('Raleway', 10, 'bold'))
        self.input_7_entry.grid(row=row + 2, column=1)

        self.input_8_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input8,
                                      font=('Raleway', 10, 'bold'))
        self.input_8_entry.grid(row=row + 2, column=2)

        self.input_9_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input9,
                                      font=('Raleway', 10, 'bold'))
        self.input_9_entry.grid(row=row + 2, column=3)

        self.input_10_entry = tk.Entry(frame, width=16, textvariable=self.aiModelFunction.input10,
                                       font=('Raleway', 10, 'bold')
                                       )
        self.input_10_entry.grid(row=row + 2, column=4)

    def single_independent_feature_label(self, row, frame):
        """
        A function that creates the input for the single prediction.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The list of input on the frame
        """
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

    def file_input(self, row, frame, frame2):
        """
        A function that creates the treeview, button and label to allow the user to input the file prediction.
        :param row: The row of frame to put the widgets
        :param frame: The first frame that puts the tkinter widgets
        :param frame2: The second frame that puts the tkinter widgets
        :return: The input treeview, label and buttons on the frame
        """
        # Button and Label that allows the user to enter the file for prediction
        self.browse_file = tk.Button(frame, text="Browse File", width=10, height=1,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.aiModelFunction.get_file_data(frame2, self.file_path,
                                                                                        self.input_view))
        self.browse_file.grid(row=row, column=0, padx=(65, 10), pady=(5, 0))

        self.file_text = tk.Label(frame, text='File Path: ', width=8, height=1,
                                  font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.file_text.grid(row=row, column=1, pady=(5, 0))

        self.file_path = tk.Label(frame, text=self.aiModelFunction.file_inputted, width=60, height=1,
                                  font=('Raleway', 8, 'bold', 'underline'), bg='white', anchor='w')
        self.file_path.grid(row=row, column=2, padx=(3, 65), columnspan=3, pady=(5, 0))

        self.input_view = ttk.Treeview(frame, selectmode='browse', height=4,
                                       show='headings',
                                       columns=['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'PT08.S2(NMHC)',
                                                'NOx(GT)',
                                                'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)'])
        self.input_view.grid(row=row + 1, column=0, columnspan=5, pady=(5, 0))

        for i in range(0, 10):
            self.input_view.column(i, minwidth=60, width=60, anchor='c', stretch=False)

        self.input_scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.input_view.yview)
        self.input_view.configure(yscrollcommand=self.input_scrollbar.set)
        self.input_scrollbar.grid(row=row + 1, column=4, sticky='ns', padx=(200, 0), pady=(6, 1))

        self.file = [self.browse_file, self.file_text, self.file_path, self.input_view, self.input_scrollbar]

    def dependent_variable(self, row, frame):
        """
        A function that creates the checkbutton to allow the user to choose the dependent variable.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The check buttons on the frame
        """
        # Checkbuttons that let the user choose the dependent variables for prediction
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

    def prediction_result(self, row, frame, number, result_df):
        """
        A function that creates the treeview for the user to see the result.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :param number: The number of dependent variables chose
        :param result_df: The prediction result from the AI Model
        :return: The result treeview on the frame
        """
        # Treeview that shows the prediction result
        self.result_view = ttk.Treeview(frame, selectmode='browse', height=5,
                                        show='headings',
                                        columns=['test'])
        self.result_view.grid(row=row, column=0, columnspan=5, pady=(10, 0))

        if number == 0:
            self.result_view.column("0", width=600, anchor='c')

        elif number == 1:
            self.result_view['columns'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

            for i in range(0, 10):
                self.result_view.column(i, width=60, anchor='c')

            for i in range(0, 10):
                self.result_view.heading(i, text=self.aiModelFunction.result_df.columns[i])

            result_list = result_df.to_numpy().tolist()

            for item_list in result_list:
                values = [item for item in item_list]
                self.result_view.insert("", 'end', values=values)

        elif number == 2:
            self.result_view['columns'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

            for i in range(0, 10):
                self.result_view.column(i, width=55, anchor='c')

            self.result_view.column("10", width=50, anchor='c')

            for i in range(0, 11):
                self.result_view.heading(i, text=self.aiModelFunction.result_df.columns[i])

            result_list = result_df.to_numpy().tolist()

            for item_list in result_list:
                values = [item for item in item_list]
                self.result_view.insert("", 'end', values=values)

        elif number == 3:
            self.result_view['columns'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')

            for i in range(0, 12):
                self.result_view.column(i, width=50, anchor='c')

            for i in range(0, 12):
                self.result_view.heading(i, text=self.aiModelFunction.result_df.columns[i])

            result_list = result_df.to_numpy().tolist()

            for item_list in result_list:
                values = [item for item in item_list]
                self.result_view.insert("", 'end', values=values)

        vertical_scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.result_view.yview)
        self.result_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.grid(row=row, column=4, sticky='ns', padx=(90, 0), pady=(11, 1))

        self.result = [self.result_view, vertical_scrollbar]

    def final_button(self, row, frame):
        """
        A function that creates the buttons, label and entry for the user to visualise or save files.
        :param row: The row of frame to put the widgets
        :param frame: The frame that puts the tkinter widgets
        :return: The buttons, label and entry on the frame
        """
        # Buttons that let the user clear the inputs, do prediction or save the result
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

        download_result_button = tk.Button(frame, text="Download\nPrediction Result", width=16, height=2,
                                           font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                           activebackground='cornflowerblue',
                                           command=lambda: self.aiModelFunction.save_file(frame, self.filename_entry))
        download_result_button.grid(row=row, column=3, pady=(8, 5), padx=(5, 5))

        filename_label = tk.Label(frame, text='Enter a\nFilename', width=10, height=3,
                                  font=('Raleway', 8, 'bold'), bg='lightskyblue', anchor='w')
        filename_label.grid(row=row, column=4, pady=(8, 5), padx=(0, 70))

        self.filename_entry = tk.Entry(frame, width=15, font=('Raleway', 10, 'bold'), bg='dodgerblue')
        self.filename_entry.grid(row=row, column=4, pady=(8, 5), padx=(80, 0))

    def predict(self, frame, result_label):
        """
        A function that check the current page viewing and predict the user's input.
        :param frame: The frame that puts the tkinter widgets
        :param result_label: The label for result heading
        :return: The result treeview and label on the frame
        """
        # Do prediction if the user has entered the inputs correctly
        if self.aiModelFunction.view_options != 'initial':
            if self.aiModelFunction.prediction_options is False:
                passed, input_df = self.aiModelFunction.check_prediction(frame, self.entry)
                if passed:
                    length, self.prediction_df = self.aiModelFunction.do_prediction(input_df)
                    if length == 10:
                        self.aiModelFunction.prediction(frame, result_label,
                                                        self.prediction_result(row=12, frame=self.result_frame,
                                                                               number=1, result_df=self.prediction_df))
                    elif length == 11:
                        self.aiModelFunction.prediction(frame, result_label,
                                                        self.prediction_result(row=12, frame=self.result_frame,
                                                                               number=2, result_df=self.prediction_df))
                    else:
                        self.aiModelFunction.prediction(frame, result_label,
                                                        self.prediction_result(row=12, frame=self.result_frame,
                                                                               number=3, result_df=self.prediction_df))
            else:
                label = tk.Label(frame, text='Please Clear the\nScreen Before\nPredicting Again', foreground='red', bg='lightskyblue')
                label.grid(row=13, column=2)
                label.after(3000, lambda: label.destroy())
        else:
            label = tk.Label(frame, text='Please Select\nthe Input type', foreground='red', bg='lightskyblue')
            label.grid(row=13, column=2)
            label.after(3000, lambda: label.destroy())

    def view(self, method):
        """
        A function that check the current page viewing and change the view user's chose.
        :param method: The user's input chosen from the input buttons
        :return: The type of viewing frame based on the method chosen
        """
        # Change the page based on what the user has chosen
        if method == 'file':
            if self.aiModelFunction.view_options != 'file':
                self.aiModelFunction.change_input('file', self.frame, self.file_input(row=4, frame=self.frame,
                                                                                      frame2=self.bottom_frame),
                                                  self.canvas, self.independent_label, self.dependent_label, self.result_label,
                                                  self.filename_entry,
                                                  self.entry, self.label, self.file, self.result,
                                                  self.t_Button, self.ah_Button, self.rh_Button)
        elif method == 'single':
            if self.aiModelFunction.view_options != 'single':
                self.aiModelFunction.change_input('single', self.frame, self.single_input(row=4, frame=self.frame),
                                                  self.canvas, self.independent_label, self.dependent_label, self.result_label,
                self.filename_entry,
                                                  self.entry, self.label, self.file, self.result,
                                                  self.t_Button, self.ah_Button, self.rh_Button)

    def clear(self):
        """
        A function that clear the current page viewing and change to the initial page view.
        :return: Clear the inputs and go back to the initial page view
        """
        # Clear the inputs and results
        if self.aiModelFunction.view_options != 'initial':
            self.aiModelFunction.clear_all(self.frame, self.canvas, self.draw_canvas(row=4, frame=self.frame),
                                           self.independent_label, self.dependent_label, self.result_label, self.filename_entry,
                                           self.entry, self.label, self.file, self.result,
                                           self.t_Button,
                                           self.ah_Button, self.rh_Button)
