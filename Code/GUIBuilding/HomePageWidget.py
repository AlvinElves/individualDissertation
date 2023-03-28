import tkinter as tk
import webbrowser


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
        intro_text = "Welcome to the Visualisation and Prediction on Air Quality, VPAQ\n" \
                     "Software. There are a total of five pages, Home, Historical Vis, Live Vis,\n" \
                     "AI Prediction, and AI Model Vis.\n\n" \
                     "There are two different types of dataset used for visualisation, Historical\n" \
                     "Data and Live Data. In Addition, the Model used for prediction can also be\n" \
                     "visualise in the AI Model Vis Page.\n\n" \
                     "All of the pages will be fully shown once the button has been clicked, so\n" \
                     "the users are able to see the variables/pollutant to visualise.\n\n" \
                     "Furthermore, the information about the dataset and chosen visualisation\n" \
                     "are shown at the bottom right of the screen.\n\n" \
                     "The AI Prediction page allows the user to input the data either using\n" \
                     "single point entry or file entry. The predicted result will be shown in\n" \
                     "a treeview and is able to be downloaded."
        introduction_text = tk.Label(frame, text=intro_text, width=58, height=18,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        introduction_text.grid(row=0, column=0, padx=(33, 32), pady=(24, 0), sticky='w')

        def callback(url):
            """
            A function that open the URL link when clicks
            :param url: Link to open the website
            :return: The website based on the URL
            """
            webbrowser.open_new(url)

        feature_text = tk.Label(frame, text='Feature: ', width=58, height=2,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw', cursor="hand2")
        feature_text.grid(row=1, column=0, padx=(33, 32), pady=(5, 3), sticky='w')
        feature_text.bind("<Button-1>", lambda e: callback("https://public.opendatasoft.com/explore/dataset/openaq"))

        demo_text = tk.Label(frame, text='Demo: ', width=58, height=2,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw', cursor="hand2")
        demo_text.grid(row=2, column=0, padx=(33, 32), pady=(0, 5), sticky='w')
        demo_text.bind("<Button-1>", lambda e: callback("https://public.opendatasoft.com/explore/dataset/openaq"))
