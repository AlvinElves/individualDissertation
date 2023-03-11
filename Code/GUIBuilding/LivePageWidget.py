from Code.GUIBuilding.LivePageFunction import *


class LivePageWidget:
    def __init__(self):
        self.livePageFunction = LivePageFunction()

    def inner_livepage_widget(self, right_inside_frame):
        self.pop_up_visualisation(row=0, frame=right_inside_frame)
        self.draw_line(row=3, frame=right_inside_frame)
        self.graph_on_map_visualisation(row=4, frame=right_inside_frame)
        self.draw_line(row=5, frame=right_inside_frame)

        left_frame = tk.Frame(right_inside_frame, width=155, height=268, bg='lightskyblue')
        left_frame.grid(row=6, column=0, rowspan=5)

        self.choose_pollutant(row=0, frame=left_frame)

        middle_frame = tk.Frame(right_inside_frame, width=155, height=268, bg='lightskyblue')
        middle_frame.grid(row=6, column=1, rowspan=5)

        self.choose_graph_type_label(row=0, frame=middle_frame)

        self.show_chosen_info(row=6, frame=right_inside_frame)
        self.visualise_button(row=11, frame=right_inside_frame)

    def pop_up_visualisation(self, row, frame):
        # Pop Up Vis Buttons and Text
        pop_up_text = tk.Label(frame, text="Pop Up Map\nVisualisation: ", width=21, height=3,
                               font=('Raleway', 10, 'bold'), bg='lightskyblue')
        pop_up_text.grid(row=row, column=0, rowspan=3)

        pm2_dot_5_button = tk.Button(frame, text="PM2.5 MAP", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.livePageFunction.choose_method('pm2.5', self.vis_chosen_label,
                                                                                         self.graph_type_label,
                                                                                         self.type_chosen_label, self.pollutant_label,
                                                                                         self.list_box, self.last_updated_button,
                                                                                         self.most_frequent_button))
        pm2_dot_5_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        pm10_button = tk.Button(frame, text="PM10 MAP", width=22, height=2,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                activebackground='cornflowerblue',
                                command=lambda: self.livePageFunction.choose_method('pm10', self.vis_chosen_label,
                                                                                    self.graph_type_label,
                                                                                    self.type_chosen_label, self.pollutant_label,
                                                                                    self.list_box, self.last_updated_button,
                                                                                    self.most_frequent_button))
        pm10_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        o3_button = tk.Button(frame, text="O3 MAP", width=22, height=2,
                              font=('Raleway', 10, 'bold'), bg='lightskyblue',
                              activebackground='cornflowerblue',
                              command=lambda: self.livePageFunction.choose_method('o3', self.vis_chosen_label,
                                                                                  self.graph_type_label,
                                                                                  self.type_chosen_label, self.pollutant_label,
                                                                                  self.list_box, self.last_updated_button,
                                                                                  self.most_frequent_button))
        o3_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

        no2_button = tk.Button(frame, text="NO2 MAP", width=22, height=2,
                               font=('Raleway', 10, 'bold'), bg='lightskyblue',
                               activebackground='cornflowerblue',
                               command=lambda: self.livePageFunction.choose_method('no2', self.vis_chosen_label,
                                                                                   self.graph_type_label,
                                                                                   self.type_chosen_label, self.pollutant_label,
                                                                                   self.list_box, self.last_updated_button,
                                                                                   self.most_frequent_button))
        no2_button.grid(row=row + 1, column=1, pady=(10, 0), padx=(5, 5))

        so2_button = tk.Button(frame, text="SO2 MAP", width=22, height=2,
                               font=('Raleway', 10, 'bold'), bg='lightskyblue',
                               activebackground='cornflowerblue',
                               command=lambda: self.livePageFunction.choose_method('so2', self.vis_chosen_label,
                                                                                   self.graph_type_label,
                                                                                   self.type_chosen_label, self.pollutant_label,
                                                                                   self.list_box, self.last_updated_button,
                                                                                   self.most_frequent_button))
        so2_button.grid(row=row + 1, column=2, pady=(10, 0), padx=(5, 5))

        co_button = tk.Button(frame, text="CO MAP", width=22, height=2,
                              font=('Raleway', 10, 'bold'), bg='lightskyblue',
                              activebackground='cornflowerblue',
                              command=lambda: self.livePageFunction.choose_method('co', self.vis_chosen_label,
                                                                                  self.graph_type_label,
                                                                                  self.type_chosen_label, self.pollutant_label,
                                                                                  self.list_box, self.last_updated_button,
                                                                                  self.most_frequent_button))
        co_button.grid(row=row + 1, column=3, pady=(10, 0), padx=(5, 5))

        bc_button = tk.Button(frame, text="BC MAP", width=22, height=2,
                              font=('Raleway', 10, 'bold'), bg='lightskyblue',
                              activebackground='cornflowerblue',
                              command=lambda: self.livePageFunction.choose_method('bc', self.vis_chosen_label,
                                                                                  self.graph_type_label,
                                                                                  self.type_chosen_label, self.pollutant_label,
                                                                                  self.list_box, self.last_updated_button,
                                                                                  self.most_frequent_button))
        bc_button.grid(row=row + 2, column=1, pady=(10, 0), padx=(5, 5))

        enhanced_button = tk.Button(frame, text="ENHANCED MAP", width=22, height=2,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                    activebackground='cornflowerblue',
                                    command=lambda: self.livePageFunction.choose_method('enhanced',
                                                                                        self.vis_chosen_label,
                                                                                        self.graph_type_label,
                                                                                        self.type_chosen_label, self.pollutant_label,
                                                                                        self.list_box, self.last_updated_button,
                                                                                        self.most_frequent_button))
        enhanced_button.grid(row=row + 2, column=2, pady=(10, 0), padx=(5, 5))

    def graph_on_map_visualisation(self, row, frame):
        # Graph On Map Vis Buttons and Text
        graph_on_text = tk.Label(frame, text="Graph On Map\nVisualisation: ", width=21, height=3,
                                 font=('Raleway', 10, 'bold'), bg='lightskyblue')
        graph_on_text.grid(row=row, column=0)

        bubble_map_button = tk.Button(frame, text="BUBBLE MAP", width=22, height=2,
                                      font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                      activebackground='cornflowerblue',
                                      command=lambda: self.livePageFunction.choose_method('bubble',
                                                                                          self.vis_chosen_label,
                                                                                          self.graph_type_label,
                                                                                          self.type_chosen_label, self.pollutant_label,
                                                                                          self.list_box, self.last_updated_button,
                                                                                          self.most_frequent_button))
        bubble_map_button.grid(row=row, column=1, pady=(10, 0), padx=(5, 5))

        bar_graph_button = tk.Button(frame, text="BAR GRAPH\nON MAP", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.livePageFunction.choose_method('bar', self.vis_chosen_label,
                                                                                         self.graph_type_label,
                                                                                         self.type_chosen_label, self.pollutant_label,
                                                                                         self.list_box, self.last_updated_button,
                                                                                         self.most_frequent_button))
        bar_graph_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

        pie_chart_button = tk.Button(frame, text="PIE CHART\nON MAP", width=22, height=2,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.livePageFunction.choose_method('pie', self.vis_chosen_label,
                                                                                         self.graph_type_label,
                                                                                         self.type_chosen_label, self.pollutant_label,
                                                                                         self.list_box, self.last_updated_button,
                                                                                         self.most_frequent_button))
        pie_chart_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 5))

    @staticmethod
    def draw_line(row, frame):
        # Draw line
        top_canvas = tk.Canvas(frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
        top_canvas.grid(row=row, columnspan=5)
        top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

    def choose_pollutant(self, row, frame):
        # Choose Pollutant Label & Listbox
        self.pollutant_label = tk.Label(frame, text=self.livePageFunction.choose_pollutant_text, width=21,
                                       height=3,
                                       font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.pollutant_label.grid(row=row, column=0)

        self.list_box = tk.Listbox(frame, height=11, width=25, selectmode='single', highlightthickness=0,
                                   activestyle='none', justify='center', bg='lightskyblue',
                                   highlightbackground='lightskyblue',
                                   relief='flat', bd=0, state='disabled')
        self.list_box.grid(row=row + 1, column=0, rowspan=4)

    def choose_graph_type_label(self, row, frame):
        # Choose graph on map type Label
        self.graph_type_label = tk.Label(frame, text=self.livePageFunction.choose_type_text, width=21,
                                         height=3,
                                         font=('Raleway', 10, 'bold'), bg='lightskyblue')
        self.graph_type_label.grid(row=row, column=0)

        self.last_updated_button = tk.Button(frame, text='', width=19, height=2, bd=0,
                                             font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                             activebackground='cornflowerblue',
                                             state='normal',
                                             command=lambda: self.livePageFunction.choose_type('last',
                                                                                               self.type_chosen_label))
        self.last_updated_button.grid(row=row + 1, column=0, padx=(5, 0), pady=20, rowspan=2)

        self.most_frequent_button = tk.Button(frame, text='', width=19, height=2, bd=0,
                                              font=('Raleway', 10, 'bold'), bg='lightskyblue',
                                              activebackground='cornflowerblue',
                                              state='normal',
                                              command=lambda: self.livePageFunction.choose_type('most',
                                                                                                self.type_chosen_label))
        self.most_frequent_button.grid(row=row + 3, column=0, padx=(5, 0), pady=20, rowspan=2)

    def show_chosen_info(self, row, frame):
        # Show all the button pressed
        chosen_title_text = tk.Label(frame, text="Chosen Visualisation & \nMap Type", width=25, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
        chosen_title_text.grid(row=row, column=2, columnspan=2)

        vis_chosen_text = tk.Label(frame, text="Visualisation Chosen: ", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='lightskyblue')
        vis_chosen_text.grid(row=row + 1, column=2)

        self.vis_chosen_label = tk.Label(frame, text=self.livePageFunction.visualisation_text, width=21,
                                         height=2,
                                         font=('Raleway', 10, 'bold'), bg='royalblue')
        self.vis_chosen_label.grid(row=row + 1, column=3)

        type_chosen_text = tk.Label(frame, text="On Map Type Chosen: ", width=21, height=3,
                                    font=('Raleway', 10, 'bold'), bg='lightskyblue')
        type_chosen_text.grid(row=row + 2, column=2, pady=(0, 70))

        self.type_chosen_label = tk.Label(frame, text=self.livePageFunction.map_text,
                                          width=21, height=2,
                                          font=('Raleway', 10, 'bold'), bg='royalblue')
        self.type_chosen_label.grid(row=row + 2, column=3, pady=(0, 70))

        last_updated_text = tk.Label(frame, text="Dataset Last Updated", width=21, height=3,
                             font=('Raleway', 10, 'bold'), bg='lightskyblue')
        last_updated_text.grid(row=row + 2, column=2, pady=(50, 0))

        self.last_updated_label = tk.Label(frame, text="Dataset Last Updated", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='royalblue')
        self.last_updated_label.grid(row=row + 2, column=3, pady=(50, 0))

        website_text = tk.Label(frame, text="Dataset Website", width=21, height=2,
                                font=('Raleway', 10, 'bold'), bg='lightskyblue')
        website_text.grid(row=row + 3, column=2, pady=(0, 5))

        website_label = tk.Label(frame, text='https://public.opendatasoft.com/\nexplore/dataset/openaq',
                                 width=25, height=2, font=('Raleway', 8, 'bold'), bg='royalblue')
        website_label.grid(row=row + 3, column=3, pady=(0, 5))

    def visualise_button(self, row, frame):
        clear_button = tk.Button(frame, text="Clear All", width=21, height=2,
                                 font=('Raleway', 10, 'bold'), bg='dodgerblue', activebackground='cornflowerblue',
                                 command=lambda: self.livePageFunction.clear(self.vis_chosen_label,
                                                                             self.graph_type_label,
                                                                             self.type_chosen_label, self.pollutant_label,
                                                                             self.list_box, self.last_updated_button,
                                                                             self.most_frequent_button))
        clear_button.grid(row=row, column=2, padx=(4, 2), pady=(5, 3))

        visualise_button = tk.Button(frame, text="Visualise the\nLive Data", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), bg='dodgerblue',
                                     activebackground='cornflowerblue',
                                     command=lambda: self.livePageFunction.visualise(frame, 'visualise'))
        visualise_button.grid(row=row, column=3, padx=(2, 2), pady=(5, 3))
