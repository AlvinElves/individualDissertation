import tkinter as tk
import webbrowser


class HomePageWidget:
    """
    HomePageWidget Class to be imported into GUI files. This class contains the tkinter widgets like the label.
    """

    # The widgets for the inner right side of the software
    def inner_homepage_widget(self, frame):
        """
        A function that creates the inner right side of the GUI that contains all the tkinter widgets.
        :param frame: Right inner frame that puts the tkinter widgets
        :return: The labels and introduction text on the frame
        """

        # A label and text that greets and show the instruction for the user
        intro_text = "Welcome to the Visualisation and Prediction of Air Quality (VPAQ)\n" \
                     "Software. There are five pages in total: Home, Historical Vis, Live Vis,\n" \
                     "AI Prediction, and AI Model Vis.\n\n" \
                     "There are two types of datasets used for visualisation: historical data\n" \
                     "and live data. Furthermore, the model used for prediction can be\n" \
                     "visualised and understood in the AI Model Vis Page.\n\n" \
                     "Once the button is clicked, all of the pages will be fully displayed,\n" \
                     "allowing users to select which variables/pollutants to visualise.\n\n" \
                     "Furthermore, information about the dataset and the selected\n" \
                     "visualisation is displayed at the bottom right of the screen.\n\n" \
                     "The AI Prediction page allows the user to enter data using either\n" \
                     "single point entry or file entry. The predicted result will be displayed\n" \
                     "in a treeview and will be available for download.\n\n" \
                     "The link below go into greater detail about the software's functionality."

        introduction_text = tk.Label(frame, text=intro_text, width=58, height=20,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        introduction_text.grid(row=0, column=0, columnspan=2, padx=(33, 32), pady=(15, 0), sticky='w')

        def callback(url):
            """
            A function that open the URL link when clicks
            :param url: Link to open the website
            :return: The website based on the URL
            """
            webbrowser.open_new(url)

        # A labels that let the user click on to open a video
        functionality_text = tk.Label(frame, text='Functionality\nDemonstration: ', width=15, height=2,
                                      font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        functionality_text.grid(row=1, column=0, padx=(25, 0), pady=(10, 18), sticky='w')

        url_text = tk.Label(frame, text='URL ', width=35, height=2,
                            font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw', cursor="hand2")
        url_text.grid(row=1, column=1, padx=(0, 5), pady=(10, 18), sticky='w')
        url_text.bind("<Button-1>", lambda e: callback("https://public.opendatasoft.com/explore/dataset/openaq"))
