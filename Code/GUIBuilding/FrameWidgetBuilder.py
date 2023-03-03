import tkinter as tk


# Create function for button hovers
def on_enter(e):
    e.widget['background'] = 'slateblue'


def on_leave(e):
    e.widget['background'] = 'royalblue'


# Check the current page to give different background and active background colour
def check_page(page, currentPage):
    if page != currentPage:
        background_colour = 'royalblue'
        active_colour = 'cornflowerblue'
    else:
        background_colour = 'cornflowerblue'
        active_colour = 'dodgerblue'

    return background_colour, active_colour


def left_frame_widget(left_frame, page, command1, command2, command3, command4, command5):
    # Left_Frame
    label = tk.Label(left_frame, text="LOGO", width=7, font=('Raleway', 35, 'bold'), bg='royalblue')
    label.grid(row=0, column=0, pady=75)

    background_colour, active_colour = check_page(page, 'home')
    home_button = tk.Button(left_frame, text="HOME", fg='lightsteelblue', bg=background_colour, width=25,
                            height=4, bd=0, activebackground=active_colour,
                            activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                            command=command1)
    home_button.grid(row=1, column=0, pady=3)

    if page != 'home':
        home_button.bind("<Enter>", on_enter)
        home_button.bind("<Leave>", on_leave)

    background_colour, active_colour = check_page(page, 'historical')
    visualise_button = tk.Button(left_frame, text="HISTORICAL VIS", fg='lightsteelblue', bg=background_colour,
                                 width=25, height=4, bd=0, activebackground=active_colour,
                                 activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                 command=command2)
    visualise_button.grid(row=2, column=0, pady=3)

    if page != 'historical':
        visualise_button.bind("<Enter>", on_enter)
        visualise_button.bind("<Leave>", on_leave)

    background_colour, active_colour = check_page(page, 'live')
    live_vis_button = tk.Button(left_frame, text="LIVE VIS", fg='lightsteelblue', bg=background_colour, width=25,
                                height=4, bd=0, activebackground=active_colour,
                                activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                command=command3)
    live_vis_button.grid(row=3, column=0, pady=3)

    if page != 'live':
        live_vis_button.bind("<Enter>", on_enter)
        live_vis_button.bind("<Leave>", on_leave)

    background_colour, active_colour = check_page(page, 'prediction')
    predict_button = tk.Button(left_frame, text="PREDICTION", fg='lightsteelblue', bg=background_colour, width=25,
                               height=4, bd=0, activebackground=active_colour,
                               activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                               command=command4)
    predict_button.grid(row=4, column=0, pady=3)

    if page != 'prediction':
        predict_button.bind("<Enter>", on_enter)
        predict_button.bind("<Leave>", on_leave)

    background_colour, active_colour = check_page(page, 'model')
    model_vis_button = tk.Button(left_frame, text="AI MODEL VIS", fg='lightsteelblue', bg=background_colour, width=25,
                                 height=4, bd=0, activebackground=active_colour,
                                 activeforeground='royalblue', font=('Raleway', 10, 'bold'),
                                 command=command5)
    model_vis_button.grid(row=5, column=0, pady=(3, 86))

    if page != 'model':
        model_vis_button.bind("<Enter>", on_enter)
        model_vis_button.bind("<Leave>", on_leave)


def right_frame_widget(right_frame, title_name):
    title_label = tk.Label(right_frame, text=title_name, width=26,
                           font=('Raleway', 35, 'bold'), bg='deepskyblue')
    title_label.grid(row=0, column=0, padx=51, pady=15)
