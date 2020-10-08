from tkinter import *
import json
import requests
root = Tk()
root.title("Weather App using tkinter")
root.geometry("200x200")
# CODE HERE
try:
	api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=kochi&units=metric&appid=44302d24e62d5d8d48ab2845aa6c2b25")
	api = json.loads(api_req.content)
	the_w = api['main']['temp']
	the_pname = api['name']

except Exception as e:
	api = "ERROR"
	print(e)

the_deg = Label(root,text=str(the_w)+'C',font=("Helvetical",45))
the_city = Label(root,text=the_pname,font=("Helvetical",25))
the_deg.grid(row=0,column=0,padx=30,pady=(30,0))
the_city.grid(row=1,column=0)
root.mainloop()