import tkinter

#Tk object creation
window= tkinter.Tk()
#setting up windwo title and window size
window.title("First Tkinter Program")
window.minsize(width=500,height=200)

#label in tkinter
my_label =tkinter.Label(text="User Name ....",font=("Arial",14,"bold"))
my_label.pack(expand=True)
# na
name=" ...."
my_label.config(text=f"User Name : {name}")

def close_me():
    name=inp__.get()
    my_label.config(text=f"Your Name is : {name}")

#buttons
button=tkinter.Button(text="Close Window", command=close_me)
button.pack()
inp__ =tkinter.Entry(width=25)
inp__.pack()

#windwo's main llop
window.mainloop()