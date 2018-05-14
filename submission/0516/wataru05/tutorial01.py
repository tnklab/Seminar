from sense_hat import SenseHat
import csv
sense = SenseHat()

red = (128,0,0)
green = (0,255,0)



t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

t = round(t,1)
p = round(p,1)
h = round(h,1)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

if t>18.5 and t < 26.9:
    bg = red
else:
    bg = green

def abc():
    sense.clear(0,255,0)
    
sense.show_message(message,scroll_speed = 0.05,back_colour = bg)
sense.stick.direction_middle = abc
 #温度センサから温度情報を取得
temperature = sense.get_temperature()
    
    #小数点第１位で四捨五入する
temperature = round(temperature, 1)
    
    #表示させる文字の列の生成
msg = "temperature=%s" % temperature

    #ファイルを開く
f = open('Data.csv','a')

csvWriter = csv.writer(f)


    #温度センサから取得したデータをファイルに１行ずつ書き込む
listdata = []
listdata.append(temperature)
print(listdata)
csvWriter.writerow(listdata)


f.close()#ファイルを閉じる

while True:
    pass
