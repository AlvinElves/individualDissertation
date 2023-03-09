import tkinter as tk


class HomePageWidget:

    def inner_homepage_widget(self, frame):
        intro_text = "• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n" \
                     "• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n" \
                     "• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n• Testing\n"
        introduction_text = tk.Label(frame, text=intro_text, width=58, height=22,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        introduction_text.grid(row=0, column=0, padx=(33, 32), pady=(24, 25))
