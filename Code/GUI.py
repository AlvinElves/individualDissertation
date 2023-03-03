import tkinter as tk

from GUIBuilding.FrameWidgetBuilder import left_frame_widget, right_frame_widget


class GUI(tk.Tk):

    # __init__ function for class GUI
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # self.resizable(False, False)
        self.title('Smart City Visualisation')
        window_Width = self.winfo_screenwidth()
        window_Height = self.winfo_screenheight()
        app_Width = 1100
        app_Height = 700

        x = int((window_Width / 2) - (app_Width / 2))
        y = int((window_Height / 2) - (app_Height / 2))

        self.geometry("{}x{}+{}+{}".format(app_Width, app_Height, x, y))

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        # for F in (HomePage, HistoricalDataPage, LiveDataPage, PredictionPage, AIModelPage):
        for F in (HomePage, HistoricalDataPage, AIModelPage):
            frame = F(container, self)

            # initializing frame of that object from all the pages within the for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AIModelPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# HomePage window frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'home', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(AIModelPage))
        right_frame_widget(right_frame, "Home Page")


# Historical Data window frame
class HistoricalDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'historical', lambda: controller.show_frame(HomePage), lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(AIModelPage))
        right_frame_widget(right_frame, "Historical Data Visualisation")


# Live Data window frame
class LiveDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        #
        # live_Data = LiveData()
        self.map_type = ""
        self.pollutant_type = ""
        self.last_updated = ""
        self.data_website = ""
        self.map_type_label = tk.StringVar()
        self.pollutant_type_label = tk.StringVar()
        self.last_updated_label = tk.StringVar()
        self.data_website_label = tk.StringVar()

        def right_inner_frame_widget():
            basic_button = tk.Button(right_inside_frame, text="BASIC MAP", width=25, height=3,
                                     font=('Raleway', 10, 'bold'))
            basic_button.grid(row=0, column=0, columnspan=3, pady=(10, 5), padx=(0, 80))

            advanced_button = tk.Button(right_inside_frame, text="ADVANCED MAP", width=25, height=3,
                                        font=('Raleway', 10, 'bold'))
            advanced_button.grid(row=0, column=3, columnspan=2, pady=(10, 5))

            top_canvas = tk.Canvas(right_inside_frame, width=767, height=30, bg='lightskyblue', highlightthickness=0)
            top_canvas.grid(row=1, columnspan=5, pady=6)
            top_canvas.create_line(5, 15, 762, 15, fill="black", width=10)

            pm2_dot_5_button = tk.Button(right_inside_frame, text="PM2.5", width=15, height=3,
                                         font=('Raleway', 10, 'bold'))
            pm2_dot_5_button.grid(row=2, column=0, columnspan=2, pady=(5, 3), padx=(20, 0))

            pm10_button = tk.Button(right_inside_frame, text="PM10", width=15, height=3, font=('Raleway', 10, 'bold'))
            pm10_button.grid(row=3, column=0, columnspan=2, pady=3, padx=(20, 0))

            o3_button = tk.Button(right_inside_frame, text="O3", width=15, height=3, font=('Raleway', 10, 'bold'))
            o3_button.grid(row=4, column=0, columnspan=2, pady=3, padx=(20, 0))

            no2_button = tk.Button(right_inside_frame, text="NO2", width=15, height=3, font=('Raleway', 10, 'bold'))
            no2_button.grid(row=5, column=0, columnspan=2, pady=3, padx=(20, 0))

            so2_button = tk.Button(right_inside_frame, text="SO2", width=15, height=3, font=('Raleway', 10, 'bold'))
            so2_button.grid(row=6, column=0, columnspan=2, pady=3, padx=(20, 0))

            co_button = tk.Button(right_inside_frame, text="CO", width=15, height=3, font=('Raleway', 10, 'bold'))
            co_button.grid(row=7, column=0, columnspan=2, pady=3, padx=(20, 0))

            bc_button = tk.Button(right_inside_frame, text="BC", width=15, height=3, font=('Raleway', 10, 'bold'))
            bc_button.grid(row=8, column=0, columnspan=2, pady=(3, 5), padx=(20, 0))

            map_type_text = tk.Label(right_inside_frame, text="Selected Map Type: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='royalblue')
            map_type_text.grid(row=2, column=2, padx=(0, 40))

            map_type_label = tk.Label(right_inside_frame, textvariable=self.map_type_label, width=40, height=3,
                                      font=('Raleway', 10, 'bold'), bg='royalblue')
            map_type_label.grid(row=2, column=3, columnspan=2, padx=(0, 19))

            button_text = tk.Label(right_inside_frame, text="Selected Pollutant:", width=21, height=3,
                                   font=('Raleway', 10, 'bold'), bg='royalblue')
            button_text.grid(row=3, column=2, padx=(0, 40))

            button_label = tk.Label(right_inside_frame, textvariable=self.pollutant_type_label, width=40, height=3,
                                    font=('Raleway', 10, 'bold'), bg='royalblue')
            button_label.grid(row=3, column=3, columnspan=2, padx=(0, 19))

            last_update_text = tk.Label(right_inside_frame, text="Last update: ", width=21, height=3,
                                        font=('Raleway', 10, 'bold'), bg='royalblue')
            last_update_text.grid(row=4, column=2, padx=(0, 40))

            last_update_label = tk.Label(right_inside_frame, textvariable=self.last_updated_label, width=40, height=3,
                                         font=('Raleway', 10, 'bold'), bg='royalblue')
            last_update_label.grid(row=4, column=3, columnspan=2, padx=(0, 19))

            data_url_text = tk.Label(right_inside_frame, text="Dataset website:", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='royalblue')
            data_url_text.grid(row=5, column=2, padx=(0, 40))

            data_url_label = tk.Label(right_inside_frame, textvariable=self.data_website_label, width=40, height=3,
                                      font=('Raleway', 10, 'bold'), bg='royalblue')
            data_url_label.grid(row=5, column=3, columnspan=2, padx=(0, 19))

            download_excel_button = tk.Button(right_inside_frame, text="Download", width=25, height=3,
                                              font=('Raleway', 10, 'bold'))
            download_excel_button.grid(row=6, column=2, padx=(0, 5))

            clear_button = tk.Button(right_inside_frame, text="Clear", width=25, height=3, font=('Raleway', 10, 'bold'))
            clear_button.grid(row=6, column=3, columnspan=2)

            refresh_button = tk.Button(right_inside_frame, text="Refresh", width=25, height=3,
                                       font=('Raleway', 10, 'bold'))
            refresh_button.grid(row=7, column=2, padx=(0, 5))

            visualise_button = tk.Button(right_inside_frame, text="Visualise", width=25, height=3,
                                         font=('Raleway', 10, 'bold'))
            visualise_button.grid(row=7, column=3, columnspan=2)

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'live', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(AIModelPage))
        right_frame_widget(right_frame, "Live Data Visualisation")
        right_inner_frame_widget()


# Prediction window frame
class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'prediction', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(AIModelPage))
        right_frame_widget(right_frame, "Air Quality Prediction")


# AI Model Vis window frame
class AIModelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        self.model_chosen_string = tk.StringVar()
        self.visualisation_chosen_string = tk.StringVar()
        self.model_chosen = ''
        self.visualisation_chosen = ''

        def choose_method(method):
            if method == 'normalised':
                self.visualisation_chosen = 'Normalised Data'
            elif method == 'outliers':
                self.visualisation_chosen = 'Outliers Data'
            elif method == 'feature':
                self.visualisation_chosen = 'Feature Correlation'
            elif method == 'feature_importance':
                self.visualisation_chosen = 'Feature Importance'
            elif method == 'learning':
                self.visualisation_chosen = 'Learning Curve'
            elif method == 'hyperparameter':
                self.visualisation_chosen = 'Hyperparameter Tuning'
            elif method == 'tree':
                self.visualisation_chosen = 'Decision Tree'
            elif method == 'predicted':
                self.visualisation_chosen = 'Actual VS Predicted'

            self.visualisation_chosen_label.config(text=self.visualisation_chosen)

        def choose_model(model_var):
            if model_var == 't':
                self.model_chosen = 'T Variable'
            elif model_var == 'ah':
                self.model_chosen = 'AH Variable'
            elif model_var == 'rh':
                self.model_chosen = 'RH Variable'

            self.model_chosen_label.config(text=self.model_chosen)

        def clear():
            self.model_chosen_label.config(text='')
            self.visualisation_chosen_label.config(text='')

        def visualise(method):
            if self.visualisation_chosen == '':
                label = tk.Label(right_inside_frame, text='Please Choose the\ntype of Visualisation', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=9, column=1)
                label.after(3000, lambda: label.destroy())
            elif self.model_chosen == '':
                label = tk.Label(right_inside_frame, text='Please Choose the\nModel to Visualise', foreground='red',
                                 bg='lightskyblue')
                label.grid(row=9, column=1)
                label.after(3000, lambda: label.destroy())
            else:
                label = tk.Label(right_inside_frame, text='Loading, Please wait', foreground='green', bg='lightskyblue')
                label.grid(row=9, column=1)
                label.after(3000, lambda: label.destroy())

        def data_preprocessing(row):
            # Data Preprocessing Buttons and Text
            data_preprocessing_text = tk.Label(right_inside_frame, text="Data Preprocessing: ", width=21, height=3,
                                               font=('Raleway', 10, 'bold'), bg='lightskyblue')
            data_preprocessing_text.grid(row=row, column=0)

            normalised_button = tk.Button(right_inside_frame, text="NORMALISED DATA", width=22, height=2,
                                          font=('Raleway', 10, 'bold'), command=lambda: choose_method('normalised'))
            normalised_button.grid(row=row, column=1, pady=(10, 5))

            outliers_button = tk.Button(right_inside_frame, text="OUTLIERS DATA", width=22, height=2,
                                        font=('Raleway', 10, 'bold'), command=lambda: choose_method('outliers'))
            outliers_button.grid(row=row, column=2, pady=(10, 0), padx=(5, 5))

            feature_button = tk.Button(right_inside_frame, text="FEATURE CORRELATION", width=22, height=2,
                                       font=('Raleway', 10, 'bold'), command=lambda: choose_method('feature'))
            feature_button.grid(row=row, column=3, pady=(10, 0), padx=(5, 10))

        def ai_model(row):
            # Visualise AI Model Buttons and Text
            ai_model_text = tk.Label(right_inside_frame, text="Model Visualisation: ", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
            ai_model_text.grid(row=row, column=0, rowspan=2)

            feature_importance_button = tk.Button(right_inside_frame, text="FEATURE IMPORTANCE", width=22, height=2,
                                                  font=('Raleway', 10, 'bold'),
                                                  command=lambda: choose_method('feature_importance'))
            feature_importance_button.grid(row=row, column=1, pady=(10, 5))

            learning_rate_button = tk.Button(right_inside_frame, text="LEARNING CURVE", width=22, height=2,
                                             font=('Raleway', 10, 'bold'), command=lambda: choose_method('learning'))
            learning_rate_button.grid(row=row, column=2, pady=(10, 5), padx=(5, 5))

            hyperparameter_button = tk.Button(right_inside_frame, text="HYPERPARAMETER TUNING", width=22, height=2,
                                              font=('Raleway', 10, 'bold'),
                                              command=lambda: choose_method('hyperparameter'))
            hyperparameter_button.grid(row=row, column=3, pady=(10, 5), padx=(5, 10))

            tree_visualise_button = tk.Button(right_inside_frame, text="DECISION TREE", width=22, height=2,
                                              font=('Raleway', 10, 'bold'), command=lambda: choose_method('tree'))
            tree_visualise_button.grid(row=row + 1, column=1, pady=(10, 0))

            actual_vs_predicted_button = tk.Button(right_inside_frame, text="ACTUAL VS PREDICTED", width=22,
                                                   height=2,
                                                   font=('Raleway', 10, 'bold'),
                                                   command=lambda: choose_method('predicted'))
            actual_vs_predicted_button.grid(row=row + 1, column=2, pady=(10, 0), padx=(5, 5))

        def draw_line(row):
            top_canvas = tk.Canvas(right_inside_frame, width=767, height=20, bg='lightskyblue', highlightthickness=0)
            top_canvas.grid(row=row, columnspan=5)
            top_canvas.create_line(5, 15, 762, 15, fill="black", width=5)

        def choose_visualise_variable(row):
            # Choose Variable and Models
            ai_model_text = tk.Label(right_inside_frame, text="Choose the Variables/Tree", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
            ai_model_text.grid(row=row, column=0)

            variable_box = tk.Listbox(right_inside_frame, height=19, width=25, selectmode='multiple',
                                      activestyle='none', justify='center')
            variable_box.grid(row=row + 1, column=0, rowspan=4, pady=(0, 9))

            # Choose Variable and Models
            ai_model_text = tk.Label(right_inside_frame, text="Choose the AI Model", width=21, height=3,
                                     font=('Raleway', 10, 'bold'), bg='lightskyblue')
            ai_model_text.grid(row=row, column=1)

            t_button = tk.Button(right_inside_frame, text="T Variable\n(TEMPERATURE)", width=22,
                                 height=2,
                                 font=('Raleway', 10, 'bold'), command=lambda: choose_model('t'))
            t_button.grid(row=row + 1, column=1, pady=(2, 0), padx=(5, 5))

            ah_button = tk.Button(right_inside_frame, text="AH Variable\n(ABSOLUTE HUMIDITY)", width=22,
                                  height=2,
                                  font=('Raleway', 10, 'bold'), command=lambda: choose_model('ah'))
            ah_button.grid(row=row + 2, column=1, pady=(2, 2), padx=(5, 5))

            rh_button = tk.Button(right_inside_frame, text="RH Variable\n(RELATIVE HUMIDITY)", width=22,
                                  height=2,
                                  font=('Raleway', 10, 'bold'), command=lambda: choose_model('rh'))
            rh_button.grid(row=row + 3, column=1, pady=(0, 2), padx=(5, 5))

        def show_chosen(row):
            # Show all the button pressed
            chosen_title_text = tk.Label(right_inside_frame, text="Chosen Visualisation & Model", width=25, height=3,
                                         font=('Raleway', 10, 'bold'), bg='lightskyblue')
            chosen_title_text.grid(row=row, column=2, columnspan=2)

            model_chosen_text = tk.Label(right_inside_frame, text="AI Model Chosen: ", width=21, height=3,
                                         font=('Raleway', 10, 'bold'), bg='lightskyblue')
            model_chosen_text.grid(row=row + 1, column=2)

            self.model_chosen_label = tk.Label(right_inside_frame, text=self.model_chosen, width=21, height=2,
                                               font=('Raleway', 10, 'bold'), bg='royalblue')
            self.model_chosen_label.grid(row=row + 1, column=3)

            visualisation_chosen_text = tk.Label(right_inside_frame, text="Visualisation Chosen: ", width=21, height=3,
                                                 font=('Raleway', 10, 'bold'), bg='lightskyblue')
            visualisation_chosen_text.grid(row=row + 2, column=2)

            self.visualisation_chosen_label = tk.Label(right_inside_frame, text=self.visualisation_chosen,
                                                       width=21,
                                                       height=2,
                                                       font=('Raleway', 10, 'bold'), bg='royalblue')
            self.visualisation_chosen_label.grid(row=row + 2, column=3)

            download_dataset_button = tk.Button(right_inside_frame, text="Download\nPreprocessed Data", width=21,
                                                height=2,
                                                font=('Raleway', 10, 'bold'))
            download_dataset_button.grid(row=row + 3, column=2, padx=(4, 2))

            save_tree_button = tk.Button(right_inside_frame, text="Save Tree & Visualise", width=21, height=2,
                                         font=('Raleway', 10, 'bold'), command=lambda: visualise('save'))
            save_tree_button.grid(row=row + 3, column=3, padx=(4, 2))

            clear_button = tk.Button(right_inside_frame, text="Clear All", width=21, height=2,
                                     font=('Raleway', 10, 'bold'), command=lambda: clear())
            clear_button.grid(row=row + 4, column=2, padx=(4, 2), pady=(2, 9))

            visualise_button = tk.Button(right_inside_frame, text="Visualise the Model", width=21, height=2,
                                         font=('Raleway', 10, 'bold'), command=lambda: visualise('normal'))
            visualise_button.grid(row=row + 4, column=3, padx=(2, 4), pady=(2, 9))

        def right_inner_frame_widget():
            data_preprocessing(row=0)
            draw_line(row=1)
            ai_model(row=2)
            draw_line(row=4)
            choose_visualise_variable(row=5)
            show_chosen(row=5)

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'model', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(AIModelPage))
        right_frame_widget(right_frame, "AI Model Visualisation")
        right_inner_frame_widget()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    software = GUI()
    software.mainloop()
