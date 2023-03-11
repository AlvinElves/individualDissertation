from Code.GUIBuilding.HistoricalPageFunction import *


class HistoricalPageWidget:
    def __init__(self):
        self.historicalPageFunction = HistoricalPageFunction()

    def inner_historicalpage_widget(self, right_inside_frame):
        self.normal_visualisation(row=0, frame=right_inside_frame)
        self.draw_line(row=1, frame=right_inside_frame)
        self.animated_visualisation(row=2, frame=right_inside_frame)
        self.draw_line(row=4, frame=right_inside_frame)
        self.choose_vis_variable(row=5, frame=right_inside_frame)
        self.show_chosen(row=5, frame=right_inside_frame)
        self.download_visualise_button(row=9, frame=right_inside_frame)

    def normal_visualisation(self, row, frame):
        # Normal Vis Buttons and Text
        normal_vis_text = tk.Label(frame, text="Normal Visualisation: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        normal_vis_text.grid(row=row, column=0)

        all_data_button = tk.Button(frame, text="ALL DATA\n(LINE GRAPH)", width=22, height=2,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.historicalPageFunction.choose_method('normal', 'all',
                                                                                              self.variable_label,
                                                                                              self.visualisation_chosen_label,
                                                                                              self.vis_type_chosen_label,
                                                                                              self.variable_box, self.save_entry))
        all_data_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        daily_button = tk.Button(frame, text="DAILY DATA\n(BAR GRAPH)", width=22, height=2,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                 activebackground='cornflowerblue',
                                 command=lambda: self.historicalPageFunction.choose_method('normal', 'daily',
                                                                                           self.variable_label,
                                                                                           self.visualisation_chosen_label,
                                                                                           self.vis_type_chosen_label,
                                                                                           self.variable_box, self.save_entry))
        daily_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        monthly_button = tk.Button(frame, text="MONTHLY DATA\n(BAR GRAPH)", width=22, height=2,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   activebackground='cornflowerblue',
                                   command=lambda: self.historicalPageFunction.choose_method('normal', 'monthly',
                                                                                             self.variable_label,
                                                                                             self.visualisation_chosen_label,
                                                                                             self.vis_type_chosen_label,
                                                                                             self.variable_box, self.save_entry))
        monthly_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    def animated_visualisation(self, row, frame):
        # Animated Vis Buttons and Text
        animated_vis_text = tk.Label(frame, text="Animated Visualisation: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        animated_vis_text.grid(row=row, column=0)

        line_graph_button = tk.Button(frame, text="DAILY DATA\n(LINE GRAPH)", width=22, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.historicalPageFunction.choose_method('animated', 'line',
                                                                                                self.variable_label,
                                                                                                self.visualisation_chosen_label,
                                                                                                self.vis_type_chosen_label,
                                                                                                self.variable_box, self.save_entry))
        line_graph_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        bar_graph_button = tk.Button(frame, text="DAY COMPARISON\n(BAR GRAPH)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.choose_method('animated', 'bar',
                                                                                               self.variable_label,
                                                                                               self.visualisation_chosen_label,
                                                                                               self.vis_type_chosen_label,
                                                                                               self.variable_box, self.save_entry))
        bar_graph_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        pie_chart_button = tk.Button(frame, text="DAY COMPARISON\n(PIE CHART)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.choose_method('animated', 'pie',
                                                                                               self.variable_label,
                                                                                               self.visualisation_chosen_label,
                                                                                               self.vis_type_chosen_label,
                                                                                               self.variable_box, self.save_entry))
        pie_chart_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    @staticmethod
    def draw_line(row, frame):
        # Draw line
        top_canvas = tk.Canvas(frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5, pady=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def choose_vis_variable(self, row, frame):
        # Choose Variable Label and Listbox
        self.variable_label = tk.Label(frame, text=self.historicalPageFunction.variable_text, width=21,
                                       height=3, font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.variable_label.grid(row=row, column=0)

        self.variable_box = tk.Listbox(frame, height=12, width=25, selectmode='multiple', highlightthickness=0,
                                       activestyle='none', justify='center', bg='lightskyblue',
                                       highlightbackground='lightskyblue',
                                       relief='flat', bd=0, state='disabled')
        self.variable_box.grid(row=row + 1, column=0, rowspan=4)

    def show_chosen(self, row, frame):
        # Show all the button pressed
        chosen_title_text = tk.Label(frame, text="Chosen Visualisation & Variable", width=25, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        chosen_title_text.grid(row=row, column=2, columnspan=2)

        vis_type_chosen_text = tk.Label(frame, text="Types of Visualisation: ", width=21, height=3,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue')
        vis_type_chosen_text.grid(row=row + 1, column=2, pady=(10, 10))

        self.vis_type_chosen_label = tk.Label(frame,
                                              text=self.historicalPageFunction.visualisation_type_text, width=21,
                                              height=2,
                                              font=('Raleway', 10, 'bold'), bg='royalblue')
        self.vis_type_chosen_label.grid(row=row + 1, column=3, pady=(10, 10))

        visualisation_chosen_text = tk.Label(frame, text="Visualisation Chosen: ", width=21, height=3,
                                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        visualisation_chosen_text.grid(row=row + 2, column=2, pady=(10, 10))

        self.visualisation_chosen_label = tk.Label(frame,
                                                   text=self.historicalPageFunction.visualisation_text,
                                                   width=21,
                                                   height=2,
                                                   font=('Raleway', 10, 'bold'), bg='royalblue')
        self.visualisation_chosen_label.grid(row=row + 2, column=3, pady=(10, 10))

        save_text = tk.Label(frame, text="Name of File to Save: ", width=21, height=3,
                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        save_text.grid(row=row + 3, column=2, pady=(10, 10))

        self.save_entry = tk.Entry(frame, width=24, font=('Raleway', 10, 'bold'), bg='royalblue')
        self.save_entry.grid(row=row + 3, column=3, pady=(10, 10))

    def download_visualise_button(self, row, frame):
        download_dataset_button = tk.Button(frame, text="Download Dataset\nUsed in Visualisation",
                                            width=21,
                                            height=2, font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                            activebackground='cornflowerblue',
                                            command=lambda: self.historicalPageFunction.visualise(frame, self.variable_label,
                                                                                   self.visualisation_chosen_label,
                                                                                   self.vis_type_chosen_label,
                                                                                                  self.variable_box,
                                                                                                  self.save_entry,
                                                                                                  'dataset'))
        download_dataset_button.grid(row=row, column=2, padx=(4, 2), pady=(10, 10))

        save_vis_button = tk.Button(frame, text="Save Visualisation\nas HTML", width=21, height=2,
                                    font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.historicalPageFunction.visualise(frame, self.variable_label,
                                                                                   self.visualisation_chosen_label,
                                                                                   self.vis_type_chosen_label, self.variable_box,
                                                                                          self.save_entry,
                                                                                          'save'))
        save_vis_button.grid(row=row, column=3, padx=(2, 2), pady=(10, 10))

        clear_button = tk.Button(frame, text="Clear All", width=21, height=2,
                                 font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue',
                                 command=lambda: self.historicalPageFunction.clear(self.variable_label,
                                                                                   self.visualisation_chosen_label,
                                                                                   self.vis_type_chosen_label,
                                                                                   self.variable_box, self.save_entry))
        clear_button.grid(row=row + 1, column=2, padx=(4, 2), pady=(20, 11))

        visualise_button = tk.Button(frame, text="Visualise the\nHistorical Data", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.visualise(frame, self.variable_label,
                                                                                   self.visualisation_chosen_label,
                                                                                   self.vis_type_chosen_label, self.variable_box,
                                                                                           self.save_entry,
                                                                                           'visualise'))
        visualise_button.grid(row=row + 1, column=3, padx=(2, 2), pady=(20, 11))
