# Weather forecast Application using python
# import libraries
from tkinter import *
from tkinter import ttk
import requests
from PIL import ImageTk, Image

# Collecting data from API
# Explicit function to get 
# Weather details 
def data_fetch():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c8467c25bd6e83878917c38f089573a9").json()
    temp_label1.config(text=str(int(data["main"]["temp"])-273)+"°C")
    hum_label1.config(text=str(data["main"]["humidity"])+"%")
    ws_label1.config(text=str(int(data["wind"]["speed"])*3.6)+"km/h")
    sd_label1.config(text=str(data["weather"][0]["description"]))

# Create object
win_app = Tk()
# Create tittle and configuration
win_app.title("Weather Forecast")
win_app.config(bg= "sky blue")
# Create window size
win_app.geometry("750x750")

# Add a background in the app
new_image = ImageTk.PhotoImage(Image.open('logo.jpg'))
pn = Label(win_app, image = new_image)
pn.place(x=0,y=0, height =750, width =750)

# Add label
name_label = Label(win_app, text="Weather Forecast", font = ("Time New Roman", 50, "bold"))
name_label.place(x=70, y=60, height=100, width=600)
# Create a combo box of city name
city_name = StringVar()
list_name = ["Delhi","Mumbai","Kolkata","Bangalore","Chennai","Hyderabad","Pune","Ahmedabad","Surat","Lucknow","Jaipur","Kanpur","Nagpur","Ghaziabad","Vadodara","Rajkot","Vishakhapatnam","Indore","Thane","Bhopal","Patna","Bilaspur","Ludhiana","Agra","Madurai","Jamshedpur","Prayagraj","Nasik","Faridabad","Meerut","Jabalpur","Varanasi","Srinagar","Aurangabad","Dhanbad","Amritsar","Guwahati","Ranchi","Gwalior","Chandigarh","Vijayavada","Jodhpur","Raipur","Kota","Muzaffarpur","New Delhi","Puducherry","Secunderabad","Shimla","Puri","Balasore","Manali"]
com_box = ttk.Combobox(win_app,text="Weather Forecast",values=list_name, font = ("Time New Roman", 30, "bold"), textvariable=city_name)
com_box.place(x=115, y=190, height=80, width=500)

# Create current weather information including temperature, humidity, wind speed, and a short description of the weather conditions.
# Also create a duplicate box for print the output results of weather
temp_label = Label(win_app, text="temperature", font = ("Time New Roman", 20))
temp_label.place(x=70, y=380, height=60, width=250)
temp_label1 = Label(win_app, text=" ", font = ("Time New Roman", 20))
temp_label1.place(x=430, y=380, height=60, width=250)
hum_label = Label(win_app, text="humidity", font = ("Time New Roman", 20))
hum_label.place(x=70, y=470, height=60, width=250)
hum_label1 = Label(win_app, text=" ", font = ("Time New Roman", 20))
hum_label1.place(x=430, y=470, height=60, width=250)
ws_label = Label(win_app, text="wind speed", font = ("Time New Roman", 20))
ws_label.place(x=70, y=560, height=60, width=250)
ws_label1 = Label(win_app, text=" ", font = ("Time New Roman", 20))
ws_label1.place(x=430, y=560, height=60, width=250)
sd_label = Label(win_app, text="short description", font = ("Time New Roman", 20))
sd_label.place(x=70, y=650, height=60, width=250)
sd_label1 = Label(win_app, text=" ", font = ("Time New Roman", 20))
sd_label1.place(x=430, y=650, height=60, width=250)

# Create a button for search weather of a particular city
search_button = Button(win_app, text="Search", font = ("Time New Roman", 20, "bold"), command=data_fetch)
search_button.place(x=250, y=300, height=50, width=200)

win_app.mainloop()


