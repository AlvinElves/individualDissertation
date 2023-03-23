import tkinter as tk


class HomePageWidget:
    """
    HomePageWidget Class to be imported into GUI files. This class contains the tkinter widgets like the label.
    """

    def inner_homepage_widget(self, frame):
        """
        A function that creates the inner right side of the GUI that contains all the tkinter widgets.
        :param frame: Right inner frame that puts the tkinter widgets
        :return: The labels and introduction text on the frame
        """
        intro_text = "• Welcome to the Visualisation and Prediction on Air Quality, VPAQ\n" \
                     "Software. There are a total of five pages, Home, Historical Vis, Live Vis," \
                     "\nAI Prediction, and AI Model Vis."
        introduction_text = tk.Label(frame, text=intro_text, width=58, height=22,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        introduction_text.grid(row=0, column=0, padx=(33, 32), pady=(24, 25), sticky='w')
