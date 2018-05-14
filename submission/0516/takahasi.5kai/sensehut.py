from sense_hat import SenseHat
from time import sleep
import csv

sense = SenseHat()


w = (150,150,150)
b = (0,0,255)
e = (0,0,0)
mage=[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,w,e,e,w,w,w,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

def ue():
    steve_pixels = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,b,w,e,e,w,b,w,
    w,w,w,e,e,w,w,w,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
    sense.set_pixels(steve_pixels)

def migi():
    steve_pixels =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,b,e,e,w,w,b,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
    sense.set_pixels(steve_pixels)

def hidari():
    steve_pixels =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    b,w,w,e,e,b,w,w,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
    sense.set_pixels(steve_pixels)


def sita():
    steve_pixels=[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,w,e,e,w,w,w,
    w,b,w,e,e,w,b,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
    sense.set_pixels(steve_pixels)

def osikomi():
     sense.clear()
     hum=sense.get_humidity()
     hum=round(hum,1)
     msg="Humidity=%s "% hum
     sense.show_message(msg,scroll_speed=0.03)
     f=open('situdo.csv','a')
     csvWriter=csv.writer(f)
     listdata=[]
     listdata.append(hum)
     print(listdata)
     csvWriter.writerow(listdata)
     f.close()
     sense.set_pixels(mage)
      


sense.set_pixels(mage)


sense.stick.direction_up = ue
sense.stick.direction_down = migi
sense.stick.direction_left = hidari
sense.stick.direction_right = sita
sense.stick.direction_middle = osikomi

while True:
        sleep(1)
