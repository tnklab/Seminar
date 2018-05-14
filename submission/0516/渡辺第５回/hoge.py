from sense_hat import SenseHat
import csv
sense = SenseHat()

g=[0,255,0]
r=[255,0,0]
b=[0,0,255]
y=[255,255,0]
e=[0,0,0]

image1=[
    e,e,e,e,r,r,e,e,
    e,r,r,r,e,e,e,e,
    r,e,e,r,e,e,e,e,
    e,e,e,r,e,e,e,e,
    e,e,r,e,r,r,r,r,
    e,r,e,e,e,e,e,e,
    r,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
]

image2=[
    e,e,e,e,y,e,e,e,
    y,y,y,y,e,e,e,e,
    e,e,y,e,e,e,e,e,
    y,y,y,y,y,e,e,e,
    e,e,y,e,e,y,y,y,
    e,e,y,e,e,e,e,e,
    e,y,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
]

image3=[
    e,e,e,e,e,b,e,e,
    e,e,e,e,b,e,b,e,
    e,b,e,b,e,b,e,e,
    e,b,e,b,e,e,e,e,
    e,b,e,b,e,b,b,b,
    e,b,e,e,b,e,e,e,
    b,e,e,e,e,b,e,e,
    e,e,e,e,e,e,e,e
]


temp = sense.get_temperature()

temp =round(temp, 1)



msg = "temp=%s" %temp

sense.show_message(msg,scroll_speed = 0.07)

f = open('temperaturedata.csv','a')
csvWriter = csv.writer(f)

listdata = []
listdata.append(temp)
print(listdata)
csvWriter.writerow(listdata)
f.close()

if (temp > 25 and temp < 35):
        sense.show_message("hot",text_colour=r,scroll_speed=0.05)
elif (temp > 20 and temp == 25):
        sense.show_message("Just",text_colour=g,scroll_speed=0.05)
elif (temp > 15 and temp == 20):
        sense.show_message("litle cold",text_colour=y,scroll_speed=0.05)
else:
        sense.show_message("cold",text_colour=b,scroll_speed=0.05)


def janken():
    sense.show_message("Ja-n Ke-n",text_colour=g,scroll_speed=0.05)   
def guu():
    sense.set_pixels(image1)
def choki():
    sense.set_pixels(image2)
def par():
    sense.set_pixels(image3)
def aiko():
    sense.show_message("A-i ko-de",text_colour=g,scroll_speed=0.05)
sense.stick.direction_up = janken
sense.stick.direction_down = choki
sense.stick.direction_left = par
sense.stick.direction_right = guu
sense.stick.direction_middle = aiko

sense.clear()
while True:
    pass
