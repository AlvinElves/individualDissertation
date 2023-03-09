from Code.GUIBuilding.HistoricalPageFunction import *


class HistoricalPageWidget:
    def __init__(self):
        self.historicalPageFunction = HistoricalPageFunction()

    def inner_historicalpage_widget(self, right_inside_frame):
        self.normal_visualisation(row=0, right_inside_frame=right_inside_frame)
        self.draw_line(row=1, right_inside_frame=right_inside_frame)
        self.animated_visualisation(row=2, right_inside_frame=right_inside_frame)
        self.draw_line(row=4, right_inside_frame=right_inside_frame)
        self.choose_vis_variable(row=5, right_inside_frame=right_inside_frame)
        self.show_chosen(row=5, right_inside_frame=right_inside_frame)
        self.download_visualise_button(row=9, right_inside_frame=right_inside_frame)

    def normal_visualisation(self, row, right_inside_frame):
        # Normal Vis Buttons and Text
        normal_vis_text = tk.Label(right_inside_frame, text="Normal Visualisation: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        normal_vis_text.grid(row=row, column=0)

        all_data_button = tk.Button(right_inside_frame, text="ALL DATA\n(LINE GRAPH)", width=22, height=2,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.historicalPageFunction.choose_method('normal', 'line',
                                                                                              self.variable_label,
                                                                                              self.visualisation_chosen_label,
                                                                                              self.vis_type_chosen_label,
                                                                                              self.variable_box))
        all_data_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        daily_button = tk.Button(right_inside_frame, text="DAILY DATA\n(BAR GRAPH)", width=22, height=2,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                 activebackground='cornflowerblue',
                                 command=lambda: self.historicalPageFunction.choose_method('normal', 'bar',
                                                                                           self.variable_label,
                                                                                           self.visualisation_chosen_label,
                                                                                           self.vis_type_chosen_label,
                                                                                           self.variable_box))
        daily_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        monthly_button = tk.Button(right_inside_frame, text="MONTHLY DATA\n(PIE CHART)", width=22, height=2,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   activebackground='cornflowerblue',
                                   command=lambda: self.historicalPageFunction.choose_method('normal', 'pie',
                                                                                             self.variable_label,
                                                                                             self.visualisation_chosen_label,
                                                                                             self.vis_type_chosen_label,
                                                                                             self.variable_box))
        monthly_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    def animated_visualisation(self, row, right_inside_frame):
        # Animated Vis Buttons and Text
        animated_vis_text = tk.Label(right_inside_frame, text="Animated Visualisation: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        animated_vis_text.grid(row=row, column=0)

        line_graph_button = tk.Button(right_inside_frame, text="DAILY DATA\n(LINE GRAPH)", width=22, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.historicalPageFunction.choose_method('animated', 'line',
                                                                                                self.variable_label,
                                                                                                self.visualisation_chosen_label,
                                                                                                self.vis_type_chosen_label,
                                                                                                self.variable_box))
        line_graph_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        bar_graph_button = tk.Button(right_inside_frame, text="DAY COMPARISON\n(BAR GRAPH)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.choose_method('animated', 'bar',
                                                                                               self.variable_label,
                                                                                               self.visualisation_chosen_label,
                                                                                               self.vis_type_chosen_label,
                                                                                               self.variable_box))
        bar_graph_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        pie_chart_button = tk.Button(right_inside_frame, text="DAY COMPARISON\n(PIE CHART)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.choose_method('animated', 'pie',
                                                                                               self.variable_label,
                                                                                               self.visualisation_chosen_label,
                                                                                               self.vis_type_chosen_label,
                                                                                               self.variable_box))
        pie_chart_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    @staticmethod
    def draw_line(row, right_inside_frame):
        # Draw line
        top_canvas = tk.Canvas(right_inside_frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5, pady=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def choose_vis_variable(self, row, right_inside_frame):
        # Choose Variable Label and Listbox
        self.variable_label = tk.Label(right_inside_frame, text=self.historicalPageFunction.variable_text, width=21,
                                       height=3, font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.variable_label.grid(row=row, column=0)

        self.variable_box = tk.Listbox(right_inside_frame, height=19, width=25, selectmode='multiple',
                                       activestyle='none', justify='center', bg='lightskyblue',
                                       highlightbackground='lightskyblue',
                                       relief='flat', bd=0, state='disabled')
        self.variable_box.grid(row=row + 1, column=0, rowspan=4)

    def show_chosen(self, row, right_inside_frame):
        # Show all the button pressed
        chosen_title_text = tk.Label(right_inside_frame, text="Chosen Visualisation & Variable", width=25, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        chosen_title_text.grid(row=row, column=2, columnspan=2)

        vis_type_chosen_text = tk.Label(right_inside_frame, text="Types of Visualisation: ", width=21, height=3,
                                        font=('Raleway', 10, 'bold'), bg='lightskyblue')
        vis_type_chosen_text.grid(row=row + 1, column=2)

        self.vis_type_chosen_label = tk.Label(right_inside_frame,
                                              text=self.historicalPageFunction.visualisation_type_text, width=21,
                                              height=2,
                                              font=('Raleway', 10, 'bold'), bg='royalblue')
        self.vis_type_chosen_label.grid(row=row + 1, column=3)

        visualisation_chosen_text = tk.Label(right_inside_frame, text="Visualisation Chosen: ", width=21, height=3,
                                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        visualisation_chosen_text.grid(row=row + 2, column=2)

        self.visualisation_chosen_label = tk.Label(right_inside_frame,
                                                   text=self.historicalPageFunction.visualisation_text,
                                                   width=21,
                                                   height=2,
                                                   font=('Raleway', 10, 'bold'), bg='royalblue')
        self.visualisation_chosen_label.grid(row=row + 2, column=3)

        save_text = tk.Label(right_inside_frame, text="Name of File to Save: ", width=21, height=3,
                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        save_text.grid(row=row + 3, column=2)

        save_entry = tk.Entry(right_inside_frame, width=24, font=('Raleway', 10, 'bold'), bg='royalblue')
        save_entry.grid(row=row + 3, column=3)

    def download_visualise_button(self, row, right_inside_frame):
        download_dataset_button = tk.Button(right_inside_frame, text="Download Dataset\nUsed in Visualisation",
                                            width=21,
                                            height=2, font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                            activebackground='cornflowerblue')
        download_dataset_button.grid(row=row, column=2, padx=(4, 2))

        save_vis_button = tk.Button(right_inside_frame, text="Save Visualisation", width=21, height=2,
                                    font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.historicalPageFunction.visualise(right_inside_frame, 'save'))
        save_vis_button.grid(row=row, column=3, padx=(2, 2))

        clear_button = tk.Button(right_inside_frame, text="Clear All", width=21, height=2,
                                 font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue',
                                 command=lambda: self.historicalPageFunction.clear(self.variable_label,
                                                                                   self.visualisation_chosen_label,
                                                                                   self.vis_type_chosen_label,
                                                                                   self.variable_box))
        clear_button.grid(row=row + 1, column=2, padx=(4, 2), pady=(0, 11))

        visualise_button = tk.Button(right_inside_frame, text="Visualise the Model", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.historicalPageFunction.visualise(right_inside_frame,
                                                                                           'visualise'))
        visualise_button.grid(row=row + 1, column=3, padx=(2, 2), pady=(0, 11))
