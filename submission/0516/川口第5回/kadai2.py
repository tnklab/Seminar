import sys
import time
import datetime
import csv
from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes
 
print("Press Ctrl-C to quit")
time.sleep(1)
 
sense = SenseHat()
sense.clear()  # Blank the LED matrix
 
found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
  if dev.name == 'Raspberry Pi Sense HAT Joystick':
    found = True;
    sense.show_message('Start!')
    break
if not(found):
  print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
  exit()
 
# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]
 
MODE_TYPES = ['t', 'p', 'h', 'd']
mode_index = 0
 
def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])
 
def handle_code(code, colour, mode_index):
    if code == ecodes.KEY_DOWN:
        mode_index -= 1
        if mode_index < 0:
            mode_index = len(MODE_TYPES) - 1
        sense.show_letter(MODE_TYPES[mode_index])
    elif code == ecodes.KEY_UP:
        mode_index += 1
        if mode_index >= len(MODE_TYPES):
            mode_index = 0
        sense.show_letter(MODE_TYPES[mode_index])
    elif code == ecodes.KEY_LEFT:
        set_pixels(LEFT_PIXELS, colour)
    elif code == ecodes.KEY_RIGHT:
        set_pixels(RIGHT_PIXELS, colour)
    elif code == ecodes.KEY_ENTER:
        value = get_value(MODE_TYPES[mode_index])
        sense.show_message(value)
 
    return mode_index
 
def get_value(mode):
    if mode == MODE_TYPES[0]:
        value = sense.get_temperature()
        value = str(round(value, 1))
        f = open('data.csv','a')

        csvWriter = csv.writer(f)
        
        listdata=[]
        listdata.append(value)
        print(listdata)
        csvWriter.writerow(listdata)
    elif mode == MODE_TYPES[1]:
        value = sense.get_pressure()
        value = str(round(value, 1))
        f = open('data.csv','a')

        csvWriter = csv.writer(f)
        
        listdata=[]
        listdata.append(value)
        print(listdata)
        csvWriter.writerow(listdata)
    elif mode == MODE_TYPES[2]:
        value = sense.get_humidity()
        value = str(round(value, 1))
        f = open('data.csv','a')

        csvWriter = csv.writer(f)
        
        listdata=[]
        listdata.append(value)
        print(listdata)
        csvWriter.writerow(listdata)
    else:
        value = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f = open('data.csv','a')

        csvWriter = csv.writer(f)
        
        listdata=[]
        listdata.append(value)
        print(listdata)
        csvWriter.writerow(listdata)
    return value
 
WHITE = [255, 255, 255]
 
try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:  # key down
                mode_index = handle_code(event.code, WHITE, mode_index)
            if event.value == 0:  # key up
                sense.clear()
except KeyboardInterrupt:
    sys.exit()
       