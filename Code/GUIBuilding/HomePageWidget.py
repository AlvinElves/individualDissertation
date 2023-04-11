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
        intro_text = "Welcome to the Visualisation and Prediction of Air Quality (VPAQ) Software.\n" \
                     "There are five pages in total: Home, Historical Vis, Live Vis, AI Prediction,\n" \
                     "and AI Model Vis.\n\n" \
                     "There are two types of datasets used for visualisation: historical data and\n" \
                     "live data. Furthermore, the model used for prediction can be visualised and\n" \
                     "understood in the AI Model Vis Page.\n\n" \
                     "Once the button is clicked, all of the pages will be fully displayed, allowing\n" \
                     "users to select which variables/pollutants to visualise.\n\n" \
                     "Furthermore, information about the dataset and the selected visualisation is\n" \
                     "displayed at the bottom right of the screen.\n\n" \
                     "The AI Prediction page allows the user to enter data using either single point\n" \
                     "entry or file entry. The predicted result will be displayed in a treeview and\n" \
                     "will be available for download.\n\n" \
                     "Finally, the live data visualisation figures will be saved in the\n" \
                     "'LiveDataVisualisation' folder. The dataset and figures that the user wishes to\n" \
                     "save will be saved in the 'SavedDataset' and 'SavedVisualisation' folders,\n" \
                     "respectively.\n\n" \
                     "The link below go into greater detail about the software's functionality."

        introduction_text = tk.Label(frame, text=intro_text, width=63, height=24,
                                     font=('Raleway', 14, 'bold'), bg='lightskyblue', anchor='n')
        introduction_text.grid(row=0, column=0, columnspan=2, padx=(2, 3), sticky='n')

        def callback(url):
            """
            A function that open the URL link when clicks
            :param url: Link to open the website
            :return: The website based on the URL
            """
            webbrowser.open_new(url)

        # A labels that let the user click on to open a video
        functionality_text = tk.Label(frame, text='Functionality\nDemonstration: ', width=15, height=2,
                                      font=('Raleway', 13, 'bold'), bg='lightskyblue', anchor='n')
        functionality_text.grid(row=1, column=0, padx=(10, 0), pady=(2, 3), sticky='n')

        url_text = tk.Label(frame, text='https://drive.google.com/file/d/1JVW7gFTj6_cI_7aOBHMKtKm7O\nG-6aE8q/view?usp=share_link', width=50, height=2,
                            font=('Raleway', 13, 'bold'), bg='lightskyblue', anchor='w', cursor="hand2")
        url_text.grid(row=1, column=1, padx=(0, 70), pady=(2, 3), sticky='w')
        url_text.bind("<Button-1>", lambda e: callback("https://drive.google.com/file/d/1JVW7gFTj6_cI_7aOBHMKtKm7OG-6aE8q/view?usp=share_link"))
