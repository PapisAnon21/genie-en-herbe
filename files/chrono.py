from timeit import default_timer
import time
#import tkinter as tk

#fenetre = tk.Tk()
#def chronos():
time.sleep(3)
print(default_timer())


"""
for i in range(0,5):
	now = default_timer()
	print(now) 
	minutes , second = divmod(now , 60)
	#print(minutes , second)
	hour , minutes = divmod(minutes , 60)
	#print(hour , minutes)
	str_time = "%d:%02d:%02d" % (hour , minutes , second) #on use lesrapeaux
	print(str_time)
	time.sleep(1)
"""	
#label = tk.Label(text = str_time)
#label.place(x = 0 , y = 0)
#fenetre.after(1000, chronos) on appelle cette fonction apres 1econd
#"fenetre.mainloop()



#chronos()