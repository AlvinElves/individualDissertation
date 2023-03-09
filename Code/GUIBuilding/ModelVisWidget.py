from Code.GUIBuilding.ModelVisFunction import *


class ModelVisWidget:
    def __init__(self):

        self.modelVisFunction = ModelVisFunction()

    def inner_modelvis_widget(self, right_inside_frame):
        self.data_preprocessing(row=0, frame=right_inside_frame)
        self.draw_line(row=1, frame=right_inside_frame)
        self.ai_model(row=2, frame=right_inside_frame)
        self.draw_line(row=4, frame=right_inside_frame)
        self.choose_visualise_label(row=5, frame=right_inside_frame)
        self.list_box, self.t_button, self.ah_button, self.rh_button \
            = self.choose_visualise_variable(row=5, frame=right_inside_frame)
        self.show_chosen(row=5, frame=right_inside_frame)
        self.download_visualise_button(row=8, frame=right_inside_frame)

    def data_preprocessing(self, row, frame):
        # Data Preprocessing Buttons and Text
        data_preprocessing_text = tk.Label(frame, text="Data Preprocessing: ", width=21, height=3,
                                           font=('Raleway', 10, 'bold'), bg='lightskyblue')
        data_preprocessing_text.grid(row=row, column=0)

        normalised_button = tk.Button(frame, text="NORMALISED DATA", width=22, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.modelVisFunction.choose_method('normalised',
                                                                                          self.visualisation_chosen_label,
                                                                                          self.variable_label,
                                                                                          self.ai_model_label, self.list_box,
                                                                                          self.t_button, self.ah_button,
                                                                                          self.rh_button))
        normalised_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        outliers_button = tk.Button(frame, text="OUTLIERS DATA", width=22, height=2,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.modelVisFunction.choose_method('outliers',
                                                                                        self.visualisation_chosen_label,
                                                                                        self.variable_label,
                                                                                        self.ai_model_label, self.list_box,
                                                                                        self.t_button, self.ah_button,
                                                                                        self.rh_button))
        outliers_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        feature_button = tk.Button(frame, text="FEATURE CORRELATION", width=22, height=2,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   activebackground='cornflowerblue',
                                   command=lambda: self.modelVisFunction.choose_method('feature',
                                                                                       self.visualisation_chosen_label,
                                                                                       self.variable_label,
                                                                                       self.ai_model_label, self.list_box,
                                                                                       self.t_button, self.ah_button,
                                                                                       self.rh_button))
        feature_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    def ai_model(self, row, frame):
        # Visualise AI Model Buttons and Text
        ai_model_text = tk.Label(frame, text="Model Visualisation: ", width=21, height=3,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue')
        ai_model_text.grid(row=row, column=0, rowspan=2)

        feature_importance_button = tk.Button(frame, text="FEATURE IMPORTANCE", width=22, height=2,
                                              font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                              activebackground='cornflowerblue',
                                              command=lambda: self.modelVisFunction.choose_method('feature_importance',
                                                                                                  self.visualisation_chosen_label,
                                                                                                  self.variable_label,
                                                                                                  self.ai_model_label, self.list_box,
                                                                                                  self.t_button,
                                                                                                  self.ah_button,
                                                                                                  self.rh_button))
        feature_importance_button.grid(row=row, column=1, pady=(10, 5), padx=(5, 5))

        learning_rate_button = tk.Button(frame, text="LEARNING CURVE", width=22, height=2,
                                         font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                         activebackground='cornflowerblue',
                                         command=lambda: self.modelVisFunction.choose_method('learning',
                                                                                             self.visualisation_chosen_label,
                                                                                             self.variable_label,
                                                                                             self.ai_model_label, self.list_box,
                                                                                             self.t_button,
                                                                                             self.ah_button,
                                                                                             self.rh_button))
        learning_rate_button.grid(row=row, column=2, pady=(10, 5), padx=(5, 5))

        hyperparameter_button = tk.Button(frame, text="HYPERPARAMETER TUNING", width=22, height=2,
                                          font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                          activebackground='cornflowerblue',
                                          command=lambda: self.modelVisFunction.choose_method('hyperparameter',
                                                                                              self.visualisation_chosen_label,
                                                                                              self.variable_label,
                                                                                              self.ai_model_label, self.list_box,
                                                                                              self.t_button,
                                                                                              self.ah_button,
                                                                                              self.rh_button))
        hyperparameter_button.grid(row=row, column=3, pady=(10, 5), padx=(5, 5))

        tree_visualise_button = tk.Button(frame, text="DECISION TREE", width=22, height=2,
                                          font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                          activebackground='cornflowerblue',
                                          command=lambda: self.modelVisFunction.choose_method('tree',
                                                                                              self.visualisation_chosen_label,
                                                                                              self.variable_label,
                                                                                              self.ai_model_label, self.list_box,
                                                                                              self.t_button,
                                                                                              self.ah_button,
                                                                                              self.rh_button))
        tree_visualise_button.grid(row=row + 1, column=1, pady=(10, 0), padx=(5, 5))

        actual_vs_predicted_button = tk.Button(frame, text="ACTUAL VS PREDICTED", width=22, height=2,
                                               font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                               activebackground='cornflowerblue',
                                               command=lambda: self.modelVisFunction.choose_method('predicted',
                                                                                                   self.visualisation_chosen_label,
                                                                                                   self.variable_label,
                                                                                                   self.ai_model_label, self.list_box,
                                                                                                   self.t_button,
                                                                                                   self.ah_button,
                                                                                                   self.rh_button))
        actual_vs_predicted_button.grid(row=row + 1, column=2, pady=(10, 0), padx=(5, 5))

    @staticmethod
    def draw_line(row, frame):
        # Draw line
        top_canvas = tk.Canvas(frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def choose_visualise_label(self, row, frame):
        # Choose Variable Label
        self.variable_label = tk.Label(frame, text=self.modelVisFunction.choose_variable_text, width=21,
                                       height=3,
                                       font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.variable_label.grid(row=row, column=0)

        self.ai_model_label = tk.Label(frame, text=self.modelVisFunction.choose_model_text, width=21,
                                       height=3,
                                       font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.ai_model_label.grid(row=row, column=1)

    def choose_visualise_variable(self, row, frame):
        # Choose Variable Button and ListBox
        variable_box = tk.Listbox(frame, height=19, width=25, selectmode='multiple',
                                  activestyle='none', justify='center', bg='lightskyblue', highlightbackground='lightskyblue',
                                  relief='flat', bd=0, state='disabled')
        variable_box.grid(row=row + 1, column=0, rowspan=4)

        t_button = tk.Button(frame, text='', width=22, height=2, bd=0,
                             font=('Raleway', 10, 'bold'), bg='lightskyblue', activebackground='cornflowerblue', state='disabled',
                             command=lambda: self.modelVisFunction.choose_model('t', self.model_chosen_label))
        t_button.grid(row=row + 1, column=1)

        ah_button = tk.Button(frame, text='', width=22, height=2, bd=0,
                              font=('Raleway', 10, 'bold'), bg='lightskyblue', activebackground='cornflowerblue', state='disabled',
                              command=lambda: self.modelVisFunction.choose_model('ah', self.model_chosen_label))
        ah_button.grid(row=row + 2, column=1)

        rh_button = tk.Button(frame, text='', width=22, height=2, bd=0,
                              font=('Raleway', 10, 'bold'), bg='lightskyblue', activebackground='cornflowerblue', state='disabled',
                              command=lambda: self.modelVisFunction.choose_model('rh', self.model_chosen_label))
        rh_button.grid(row=row + 3, column=1)

        return variable_box, t_button, ah_button, rh_button

    def show_chosen(self, row, frame):
        # Show all the button pressed
        chosen_title_text = tk.Label(frame, text="Chosen Visualisation & Model", width=25, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        chosen_title_text.grid(row=row, column=2, columnspan=2)

        model_chosen_text = tk.Label(frame, text="AI Model Chosen: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        model_chosen_text.grid(row=row + 1, column=2)

        self.model_chosen_label = tk.Label(frame, text=self.modelVisFunction.model_text, width=21,
                                           height=2,
                                           font=('Raleway', 10, 'bold'), bg='royalblue')
        self.model_chosen_label.grid(row=row + 1, column=3)

        visualisation_chosen_text = tk.Label(frame, text="Visualisation Chosen: ", width=21, height=3,
                                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        visualisation_chosen_text.grid(row=row + 2, column=2, pady=(0, 70))

        self.visualisation_chosen_label = tk.Label(frame, text=self.modelVisFunction.visualisation_text,
                                                   width=21,
                                                   height=2,
                                                   font=('Raleway', 10, 'bold'), bg='royalblue')
        self.visualisation_chosen_label.grid(row=row + 2, column=3, pady=(0, 70))

        save_text = tk.Label(frame, text="Name of File to Save: ", width=21, height=3,
                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        save_text.grid(row=row + 2, column=2, pady=(50, 0))

        save_entry = tk.Entry(frame, width=24, font=('Raleway', 10, 'bold'), bg='royalblue')
        save_entry.grid(row=row + 2, column=3, pady=(50, 0))

    def download_visualise_button(self, row, frame):
        download_dataset_button = tk.Button(frame, text="Download\nPreprocessed Data", width=21,
                                            height=2,
                                            font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                            activebackground='cornflowerblue')
        download_dataset_button.grid(row=row, column=2, padx=(4, 2), pady=(20, 0))

        save_tree_button = tk.Button(frame, text="Save Tree & Visualise", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.modelVisFunction.visualise(frame, 'save'))
        save_tree_button.grid(row=row, column=3, padx=(2, 2), pady=(20, 0))

        clear_button = tk.Button(frame, text="Clear All", width=21, height=2,
                                 font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue',
                                 command=lambda: self.modelVisFunction.clear(self.model_chosen_label,
                                                                             self.visualisation_chosen_label,
                                                                             self.variable_label,
                                                                             self.ai_model_label, self.list_box,
                                                                             self.t_button,
                                                                             self.ah_button, self.rh_button))
        clear_button.grid(row=row + 1, column=2, padx=(4, 2), pady=(20, 16))

        visualise_button = tk.Button(frame, text="Visualise the Model", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.modelVisFunction.visualise(frame, 'normal'))
        visualise_button.grid(row=row + 1, column=3, padx=(2, 2), pady=(20, 16))
