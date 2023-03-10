import tkinter as tk

from GUIBuilding.FrameWidgetBuilder import left_frame_widget, right_frame_widget
from GUIBuilding.HomePageWidget import *
from GUIBuilding.HistoricalPageWidget import *
from GUIBuilding.LivePageWidget import *
from GUIBuilding.AIModelWidget import *
from GUIBuilding.ModelVisWidget import *


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
        for F in (HomePage, HistoricalDataPage, LiveDataPage, PredictionPage, ModelVisPage):
            frame = F(container, self)

            # initializing frame of that object from all the pages within the for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HistoricalDataPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# HomePage window frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        homePageWidget = HomePageWidget()

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5, highlightcolor='darkblue')
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'home', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(ModelVisPage))
        right_frame_widget(right_frame, "Home Page")
        homePageWidget.inner_homepage_widget(right_inside_frame)


# Historical Data window frame
class HistoricalDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        historicalPageWidget = HistoricalPageWidget()

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5, highlightcolor='darkblue')
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'historical', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(ModelVisPage))
        right_frame_widget(right_frame, "Historical Data Visualisation")
        historicalPageWidget.inner_historicalpage_widget(right_inside_frame)


# Live Data window frame
class LiveDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        livePageWidget = LivePageWidget()

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5, highlightcolor='darkblue')
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=583, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'live', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(ModelVisPage))
        right_frame_widget(right_frame, "Live Data Visualisation")
        livePageWidget.inner_livepage_widget(right_inside_frame)


# Prediction window frame
class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        aiModelWidget = AIModelWidget()

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5, highlightcolor='darkblue')
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'prediction', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(ModelVisPage))
        right_frame_widget(right_frame, "Air Quality Prediction")
        aiModelWidget.inner_aimodel_widget(right_inside_frame)


# AI Model Vis window frame
class ModelVisPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        modelVisWidget = ModelVisWidget()

        # Create left, right and inner right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="darkblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=(2, 0), pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="darkblue",
                               highlightthickness=5, highlightcolor='darkblue')
        right_frame.grid(row=0, column=1, padx=(0, 2), pady=3)

        right_inside_frame = tk.Frame(right_frame, width=767, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Create widgets that is in Left_Frame, Right Frame and Inner Right Frame
        left_frame_widget(left_frame, 'model', lambda: controller.show_frame(HomePage),
                          lambda: controller.show_frame(HistoricalDataPage),
                          lambda: controller.show_frame(LiveDataPage), lambda: controller.show_frame(PredictionPage),
                          lambda: controller.show_frame(ModelVisPage))
        right_frame_widget(right_frame, "AI Model Visualisation")
        modelVisWidget.inner_modelvis_widget(right_inside_frame)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    software = GUI()
    software.mainloop()
