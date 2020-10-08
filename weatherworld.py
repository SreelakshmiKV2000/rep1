from tkinter import *
import json
import requests

# Creating root
root = Tk()
root.geometry("500x200")

# Entry widget
e = Entry(root)
e.pack()
#Fn for button
def myClick():
    try:
    	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=44302d24e62d5d8d48ab2845aa6c2b25".format(e.get())
    	api_req = requests.get(url)
    	api = json.loads(api_req.content)
    	the_w = api['main']['temp']
    	the_pname = api['name']
    	myLabel = Label(root,text=str(the_w)+'C',font=("Helvetical",45)).pack()
    	myCity = Label(root,text=the_pname,font=("Helvetical",25)).pack()
    except:
    	myLabel = Label(root,text="no data found",fg="blue").pack()
#Creating button using Button() widget
myButton = Button(root,text="check",command=myClick,bg="green",fg="white")
# Packing button
myButton.pack()
# Lasting we need to loop this event
root.mainloop()