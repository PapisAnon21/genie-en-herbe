import tkinter as tk
from datetime import datetime
import main


class Chrono:
    def __init__(self, root):
        self.counter = 0
        self.running = False
        self.delay = 5
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Call functions
        #self.create_widgets()


    def create_text(self):
        self.print_label = tk.Label(self.root, text="Demarrez", fg="black", font="Verdana 50 bold", bg="white")
        """
        try:
            main.widgets["chrono"] = {"name": "Chrono", "widget": self.print_label,
                                      "x": main.widgets_placement["chrono"]["x"],
                                      "y": main.widgets_placement["chrono"]["y"]}
        except Exception as e:
            main.widgets["chrono"] = {"name": "Chrono", "widget": self.print_label,
                                      "x": 3 * self.screen_width / 10 + 140, "y": 1 * self.screen_height / 9 + 50}
        """
        #self.print_label.place(x=main.widgets["chrono"]["x"], y=main.widgets["chrono"]["y"])
        return self.print_label

        
        #del self.buttons_frame
    def creation_chrono_widgets(self):
        self.buttons_frame = tk.Frame(self.root)
        self.start_btn = tk.Button(self.buttons_frame, text='Start', width=6,
                                   command=lambda: self.start(self.print_label))
        self.stop_btn = tk.Button(self.buttons_frame, text='Stop', width=6, state='disabled', command=self.stop)
        self.reset_btn = tk.Button(self.buttons_frame, text='Reset', width=6, state='disabled',
                                   command=lambda: self.reset(self.print_label))
        self.buttons_frame.place(x=3 * self.screen_width / 10 + 240, y=0.7 * self.screen_height / 9 + 180)
        self.start_btn.pack(side="left")
        self.stop_btn.pack(side="left")
        self.reset_btn.pack(side="left")
        return self.buttons_frame


    def counter_label(self, label):
        def count():
            if self.running:
                tt = datetime.fromtimestamp(self.counter)
                string = tt.strftime("%H:%M:%S")
                label['text'] = string

                label.after(1000, count)
                self.counter += 1

        count()

    def start(self, label):
        self.running = True
        self.counter_label(label)
        self.start_btn['state'] = 'disabled'
        self.stop_btn['state'] = 'normal'
        self.reset_btn['state'] = 'normal'

    def stop(self):
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'
        self.reset_btn['state'] = 'normal'
        self.running = False

    def reset(self, label):
        self.counter = 0

        if self.running == False:
            self.reset_btn['state'] = 'disabled'
            label['text'] = ''


        else:
            label['text'] = 'Starting...'
