import tkinter as tk

#root = tk.Tk()

#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()

#root.geometry()
# centrer leccran

def center_window(w):
    eval_ = w.nametowidget('.').eval
    eval_('tk::PlaceWindow %s center' % w)
 
#root = tk.Tk()
w = tk.Toplevel()
#center_window(w)
w.tk.call('tk::PlaceWindow', w)
tk.mainloop()

