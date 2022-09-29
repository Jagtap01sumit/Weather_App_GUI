from tkinter import *
from PIL import Image,ImageTk  #for import image
from geopy.geocoders import Nominatim  #for Nominatim
from timezonefinder import TimezoneFinder  #to find location time
from datetime import datetime  #to import date and time
from tkinter import messagebox
import requests   #make request to web page
import pytz #bring the Olson database into Python and thus supports all time zone
import tkinter.messagebox as msg

root=Tk()
root.geometry("950x550")
root.title("Weather Application")
root.resizable(False,False)

label=Label(text="TODAYS FORECAST",fg="white",bg="sky blue",font="comicsansms 30 bold")
label.pack(side=TOP,fill=X)
frame = Frame(root)
def destroy_text():
    frame.destroy()







def wind_command():

    message = '''
   Message
  '''
    text_box = Text(
      frame,
        height=13,
        width=30
    )

    text_box.pack(side=LEFT)
    text_box.insert('end', message)
    text_box.config(state='disabled')

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)
    # sb.pack(side=BOTTOM, fill=BOTH)


    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    exit_button = Button(frame,text="Exit",fg="green",command=exit)
    exit_button.pack(side=RIGHT)

    frame.pack(expand=True)
    button = Button(root, text='CLEAR', command=destroy_text)
    button.place(x=900,y=50)


def Humidity_command():

    message = '''
    We often hear people talking about humidity especially when it is a hot day. While we experience this phenomenon more frequently in the coastal regions. Humidity is defined as the ratio between the vapor pressure of water vapor in the air to the vapor pressure at saturation. It is expressed at different levels depending on certain factors. However, there is no official or special SI unit for humidity measurement.
    '''
    text_box = Text(
        frame,
        height=15,
        width=30
    )

    text_box.pack(side=LEFT)
    text_box.insert('end', message)
    text_box.config(state='disabled')

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)
    # sb.pack(side=BOTTOM, fill=BOTH)

    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    exit_button = Button(frame, text="Exit", fg="green", command=exit)
    exit_button.pack(side=RIGHT)

    frame.pack(expand=True)
    button = Button(root, text='CLEAR', command=destroy_text)
    button.place(x=900, y=50)



def Description_command():
    message = ''' Message
        '''

    text_box = Text(
        frame,
        height=13,
        width=30
    )

    text_box.pack(side=LEFT)
    text_box.insert('end', message)
    text_box.config(state='disabled')

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)


    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    exit_button = Button(frame, text="Exit", fg="green", command=exit)
    exit_button.pack(side=RIGHT)

    frame.pack(expand=True)
    button = Button(root, text='CLEAR', command=destroy_text)
    button.place(x=900, y=50)


def Pressure_command():
    # demo alert 
   
    print("Thanks for visiting our application!!")
    msg.showinfo("Thanks for visiting","Have a Nice day!!!")
   
   

def getWeather():
    try:
        print("successful")
        city=textfield.get()

        geolocation=Nominatim(user_agent="geoapiExerciese")
        location=geolocation.geocode(city)
        global humidity
        obj=TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        # weather API

        api ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=695962bc436d0359d36298c6834002c4"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        L.config(text=wind)
        L1.config(text=humidity)

        L2.config(text=description)

        L3.config(text=pressure)

        print(L3.config(text=pressure))

    except Exception as e:

        messagebox.showerror("Weather App","Invalid Entry")



#Time
name=Label(root,font="arial 19 bold")
name.place(x=20,y=130)
clock=Label(root,font="Helvetica 20")
clock.place(x=20,y=170)



#search image
search_image=PhotoImage(file="search.png")
n_label=Label(image=search_image)
n_label.place(x=20,y=55)
#listBox=Listbox(root,yscrollcommand=scrollbar.set)



#search text
textfield=Entry(root,justify="center", width=17,font="poppins 25 bold", bg="#404040",border=0,fg="white")
textfield.place(x=80,y=74)
textfield.focus()



#search Buttton
search_button=PhotoImage(file="search_button.png")
varun_label=Button(image=search_button,command=getWeather)
varun_label.place(x=484,y=65)



#logo
search_logo=PhotoImage(file="logo.png")
varun_label=Label(image=search_logo)
varun_label.place(x=60,y=200)

search1_logo=PhotoImage(file="cloud.png")
varun1_label=Label(image=search1_logo)
varun1_label.place(x=550,y=316)




#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)



#Labels in bottom Box

wind_label=Button(root,text="WIND",fg="white",bg="#1ab5ef",font="lucida 12 bold",command=wind_command)
wind_label.place(x=155,y=450)

#label2=Label(root,text="HUMIDITY",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
Humidity_label=Button(root,text="HUMIDITY",fg="white",bg="#1ab5ef",font="lucida 12 bold",command=Humidity_command)
Humidity_label.place(x=300,y=450)

Description_label=Button(root,text="DESCRIPTION",fg="white",bg="#1ab5ef",font="lucida 12 bold",command=Description_command)
Description_label.place(x=480,y=450)

#label4=Label(root,text="PRESSURE",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
Pressure_label=Button(root,text="PRESSURE",fg="white",bg="#1ab5ef",font="lucida 12 bold",command=Pressure_command)
Pressure_label.place(x=675,y=450)

L=Label(root,text="....",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L.place(x=145,y=489)
L7=Label(root,text="mps",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L7.place(x=190,y=489)
L1=Label(root,text="....",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L1.place(x=330,y=489)
L5=Label(root,text="%",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L5.place(x=360,y=489)
L2=Label(root,text="....",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L2.place(x=500,y=489)
L3=Label(root,text="....",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L3.place(x=680,y=489)
L6=Label(root,text="mbar",font="Helvetica 15 bold",fg="black",bg="#1ab5ef")
L6.place(x=730,y=489)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=600,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=600,y=250)




root.mainloop()






