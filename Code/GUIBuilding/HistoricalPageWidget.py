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

    def normal_visualisation(self, row, right_inside_frame):
        # Normal Vis Buttons and Text
        normal_vis_text = tk.Label(right_inside_frame, text="Normal Visualisation: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        normal_vis_text.grid(row=row, column=0)

        all_data_button = tk.Button(right_inside_frame, text="ALL DATA\n(LINE GRAPH)", width=22, height=2,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                    activebackground='cornflowerblue')
        all_data_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        daily_button = tk.Button(right_inside_frame, text="DAILY DATA\n(BAR GRAPH)", width=22, height=2,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                 activebackground='cornflowerblue')
        daily_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        monthly_button = tk.Button(right_inside_frame, text="MONTHLY DATA\n(PIE CHART)", width=22, height=2,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                   activebackground='cornflowerblue')
        monthly_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    def animated_visualisation(self, row, right_inside_frame):
        # Animated Vis Buttons and Text
        animated_vis_text = tk.Label(right_inside_frame, text="Animated Visualisation: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        animated_vis_text.grid(row=row, column=0)

        line_graph_button = tk.Button(right_inside_frame, text="DAILY DATA\n(LINE GRAPH)", width=22, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue')
        line_graph_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        bar_graph_button = tk.Button(right_inside_frame, text="DAY COMPARISON\n(BAR GRAPH)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue')
        bar_graph_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        pie_chart_button = tk.Button(right_inside_frame, text="DAY COMPARISON\n(PIE CHART)", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue')
        pie_chart_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    @staticmethod
    def draw_line(row, right_inside_frame):
        # Draw line
        top_canvas = tk.Canvas(right_inside_frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def choose_vis_variable(self, row, right_inside_frame):
        # Choose Variable Label and Listbox
        """self.variable_label = tk.Label(right_inside_frame, text=self.historicalPageFunction.variable_text, width=21,
                                       height=3, font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.variable_label.grid(row=row, column=0)

        variable_box = tk.Listbox(right_inside_frame, height=19, width=25, selectmode='multiple',
                                  activestyle='none', justify='center', bg='lightskyblue',
                                  highlightbackground='lightskyblue',
                                  relief='flat', bd=0, state='disabled')
        variable_box.grid(row=row + 1, column=0, rowspan=4)"""

        self.variable_label = tk.Label(right_inside_frame, text='Testing', width=21,
                                       height=3, font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.variable_label.grid(row=row, column=0)

        variable_box = tk.Listbox(right_inside_frame, height=19, width=25, selectmode='multiple',
                                  activestyle='none', justify='center', bg='lightskyblue',
                                  highlightbackground='white',
                                  relief='flat', bd=0, state='disabled')
        variable_box.grid(row=row + 1, column=0, rowspan=4)

    def show_chosen(self, row, right_inside_frame):
        # Show all the button pressed
        chosen_title_text = tk.Label(right_inside_frame, text="Chosen Visualisation & Variable", width=25, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        chosen_title_text.grid(row=row, column=2, columnspan=2)

        model_chosen_text = tk.Label(right_inside_frame, text="AI Model Chosen: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        model_chosen_text.grid(row=row + 1, column=2)

        self.model_chosen_label = tk.Label(right_inside_frame, text='', width=21,
                                           height=2,
                                           font=('Raleway', 10, 'bold'), bg='royalblue')
        self.model_chosen_label.grid(row=row + 1, column=3)

        visualisation_chosen_text = tk.Label(right_inside_frame, text="Visualisation Chosen: ", width=21, height=3,
                                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        visualisation_chosen_text.grid(row=row + 2, column=2)

        self.visualisation_chosen_label = tk.Label(right_inside_frame, text='',
                                                   width=21,
                                                   height=2,
                                                   font=('Raleway', 10, 'bold'), bg='royalblue')
        self.visualisation_chosen_label.grid(row=row + 2, column=3)
