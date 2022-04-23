import tkinter

###Tk object creation
window= tkinter.Tk()

###setting up windwo title and window size
window.title("First Tkinter Program")
window.minsize(width=500,height=200)

####label in tkinter
my_label =tkinter.Label(text="I'm small label of tkinter class",font=("Arial",14,"bold"))
my_label.pack(expand=True)

####windwo's main llop
window.mainloop()