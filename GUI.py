import tkinter as tk


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
        for F in (HomePage, HistoricalDataPage, LiveDataPage, PredictionPage):
            frame = F(container, self)

            # initializing frame of that object from all the pages within the for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# HomePage window frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create function for button hovers
        def on_enter(e):
            e.widget['background'] = 'slateblue'

        def on_leave(e):
            e.widget['background'] = 'royalblue'

        # Create left and right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="deepskyblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=2, pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="royalblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=2, pady=3)

        label = tk.Label(right_frame, text="Home (Introduction)", width=26, font=('Raleway', 35, 'bold'),
                         bg='deepskyblue')
        label.grid(row=0, column=0, padx=51, pady=15)

        right_inside_frame = tk.Frame(right_frame, width=755, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Left_Frame
        label = tk.Label(left_frame, text="LOGO", width=7, font=('Raleway', 35, 'bold'), bg='royalblue')
        label.grid(row=0, column=0, pady=95)

        home_button = tk.Button(left_frame, text="HOME", fg='lightsteelblue', bg='cornflowerblue', width=25, height=4,
                                bd=0, activebackground='dodgerblue',
                                activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        home_button.grid(row=1, column=0, pady=3)

        visualise_button = tk.Button(left_frame, text="HISTORICAL VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                     height=4, bd=0, activebackground='cornflowerblue',
                                     activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                     command=lambda: controller.show_frame(HistoricalDataPage))
        visualise_button.grid(row=2, column=0, pady=3)

        visualise_button.bind("<Enter>", on_enter)
        visualise_button.bind("<Leave>", on_leave)

        live_vis_button = tk.Button(left_frame, text="LIVE VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                    height=4, bd=0, activebackground='cornflowerblue',
                                    activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                    command=lambda: controller.show_frame(LiveDataPage))
        live_vis_button.grid(row=3, column=0, pady=3)

        live_vis_button.bind("<Enter>", on_enter)
        live_vis_button.bind("<Leave>", on_leave)

        predict_button = tk.Button(left_frame, text="PREDICTION", fg='lightsteelblue', bg='royalblue', width=25,
                                   height=4, bd=0, activebackground='cornflowerblue',
                                   activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage))
        predict_button.grid(row=4, column=0, pady=3)

        predict_button.bind("<Enter>", on_enter)
        predict_button.bind("<Leave>", on_leave)

        label = tk.Label(left_frame, text="", bg='royalblue')
        label.grid(row=5, column=0, pady=50)


# Historical Data window frame
class HistoricalDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create function for button hovers
        def on_enter(e):
            e.widget['background'] = 'slateblue'

        def on_leave(e):
            e.widget['background'] = 'royalblue'

        # Create left and right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="deepskyblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=2, pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="royalblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=2, pady=3)

        label = tk.Label(right_frame, text="Historical Data Visualisation", width=26, font=('Raleway', 35, 'bold'),
                         bg='deepskyblue')
        label.grid(row=0, column=0, padx=51, pady=15)

        right_inside_frame = tk.Frame(right_frame, width=755, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Left_Frame
        label = tk.Label(left_frame, text="LOGO", width=7, font=('Raleway', 35, 'bold'), bg='royalblue')
        label.grid(row=0, column=0, pady=95)

        home_button = tk.Button(left_frame, text="HOME", fg='lightsteelblue', bg='royalblue', width=25,
                                height=4, bd=0, activebackground='cornflowerblue',
                                activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        home_button.grid(row=1, column=0, pady=3)

        home_button.bind("<Enter>", on_enter)
        home_button.bind("<Leave>", on_leave)

        visualise_button = tk.Button(left_frame, text="HISTORICAL VIS", fg='lightsteelblue', bg='cornflowerblue',
                                     width=25, height=4, bd=0, activebackground='dodgerblue',
                                     activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                     command=lambda: controller.show_frame(HistoricalDataPage))
        visualise_button.grid(row=2, column=0, pady=3)

        live_vis_button = tk.Button(left_frame, text="LIVE VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                    height=4, bd=0, activebackground='cornflowerblue',
                                    activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                    command=lambda: controller.show_frame(LiveDataPage))
        live_vis_button.grid(row=3, column=0, pady=3)

        live_vis_button.bind("<Enter>", on_enter)
        live_vis_button.bind("<Leave>", on_leave)

        predict_button = tk.Button(left_frame, text="PREDICTION", fg='lightsteelblue', bg='royalblue', width=25,
                                   height=4, bd=0, activebackground='cornflowerblue',
                                   activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage))
        predict_button.grid(row=4, column=0, pady=3)

        predict_button.bind("<Enter>", on_enter)
        predict_button.bind("<Leave>", on_leave)

        label = tk.Label(left_frame, text="", bg='royalblue')
        label.grid(row=5, column=0, pady=50)


# Live Data window frame
class LiveDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create function for button hovers
        def on_enter(e):
            e.widget['background'] = 'slateblue'

        def on_leave(e):
            e.widget['background'] = 'royalblue'

        # Create left and right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="deepskyblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=2, pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="royalblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=2, pady=3)

        label = tk.Label(right_frame, text="Live Data Visualisation", width=26, font=('Raleway', 35, 'bold'),
                         bg='deepskyblue')
        label.grid(row=0, column=0, padx=51, pady=15)

        right_inside_frame = tk.Frame(right_frame, width=755, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Left_Frame
        label = tk.Label(left_frame, text="LOGO", width=7, font=('Raleway', 35, 'bold'), bg='royalblue')
        label.grid(row=0, column=0, pady=95)

        home_button = tk.Button(left_frame, text="HOME", fg='lightsteelblue', bg='royalblue', width=25,
                                height=4, bd=0, activebackground='cornflowerblue',
                                activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        home_button.grid(row=1, column=0, pady=3)

        home_button.bind("<Enter>", on_enter)
        home_button.bind("<Leave>", on_leave)

        visualise_button = tk.Button(left_frame, text="HISTORICAL VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                     height=4, bd=0, activebackground='cornflowerblue',
                                     activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                     command=lambda: controller.show_frame(HistoricalDataPage))
        visualise_button.grid(row=2, column=0, pady=3)

        visualise_button.bind("<Enter>", on_enter)
        visualise_button.bind("<Leave>", on_leave)

        live_vis_button = tk.Button(left_frame, text="LIVE VIS", fg='lightsteelblue', bg='cornflowerblue',
                                    width=25, height=4, bd=0, activebackground='dodgerblue',
                                    activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                    command=lambda: controller.show_frame(LiveDataPage))
        live_vis_button.grid(row=3, column=0, pady=3)

        predict_button = tk.Button(left_frame, text="PREDICTION", fg='lightsteelblue', bg='royalblue', width=25,
                                   height=4, bd=0, activebackground='cornflowerblue',
                                   activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage))
        predict_button.grid(row=4, column=0, pady=3)

        predict_button.bind("<Enter>", on_enter)
        predict_button.bind("<Leave>", on_leave)

        label = tk.Label(left_frame, text="", bg='royalblue')
        label.grid(row=5, column=0, pady=50)


# Prediction window frame
class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create function for button hovers
        def on_enter(e):
            e.widget['background'] = 'slateblue'

        def on_leave(e):
            e.widget['background'] = 'royalblue'

        # Create left and right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="deepskyblue",
                              highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=2, pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="royalblue",
                               highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=2, pady=3)

        label = tk.Label(right_frame, text="Air Quality Prediction", width=26, font=('Raleway', 35, 'bold'),
                         bg='deepskyblue')
        label.grid(row=0, column=0, padx=51, pady=15)

        right_inside_frame = tk.Frame(right_frame, width=755, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        # Left_Frame
        label = tk.Label(left_frame, text="LOGO", width=7, font=('Raleway', 35, 'bold'), bg='royalblue')
        label.grid(row=0, column=0, pady=95)

        home_button = tk.Button(left_frame, text="HOME", fg='lightsteelblue', bg='royalblue', width=25,
                                height=4, bd=0, activebackground='cornflowerblue',
                                activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        home_button.grid(row=1, column=0, pady=3)

        home_button.bind("<Enter>", on_enter)
        home_button.bind("<Leave>", on_leave)

        visualise_button = tk.Button(left_frame, text="HISTORICAL VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                     height=4, bd=0, activebackground='cornflowerblue',
                                     activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                     command=lambda: controller.show_frame(HistoricalDataPage))
        visualise_button.grid(row=2, column=0, pady=3)

        visualise_button.bind("<Enter>", on_enter)
        visualise_button.bind("<Leave>", on_leave)

        live_vis_button = tk.Button(left_frame, text="LIVE VIS", fg='lightsteelblue', bg='royalblue', width=25,
                                    height=4, bd=0, activebackground='cornflowerblue',
                                    activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                    command=lambda: controller.show_frame(LiveDataPage))
        live_vis_button.grid(row=3, column=0, pady=3)

        live_vis_button.bind("<Enter>", on_enter)
        live_vis_button.bind("<Leave>", on_leave)

        predict_button = tk.Button(left_frame, text="PREDICTION", fg='lightsteelblue', bg='cornflowerblue',
                                   width=25, height=4, bd=0, activebackground='dodgerblue',
                                   activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage))
        predict_button.grid(row=4, column=0, pady=3)

        label = tk.Label(left_frame, text="", bg='royalblue')
        label.grid(row=5, column=0, pady=50)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    software = GUI()
    software.mainloop()
