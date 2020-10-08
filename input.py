from tkinter import *
# Creating root
root = Tk()
root.geometry("300x200+10+20")

#Entry widget
e = Entry(root)
e.pack()
#Fn for button
def myClick():
	myLabel = Label(root,text="Hello "+e.get(),fg="blue").pack()
#Creating button using Button() widget
myButton = Button(root,text="Click Me",command=myClick,bg="green",fg="white")
# Packing button
myButton.pack()
# Lasting we need to loop this event
root.mainloop()