from tkinter import *
window=Tk()
window.title('Hello World')
window.geometry("300x200+10+20")
lbl=Label(window, text="Hello World from GUI ",fg='green', font=("Helvetica",16))
lbl.place(x=60, y=50)
window.mainloop()