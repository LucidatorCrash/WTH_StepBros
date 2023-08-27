import serial 
import time 
import requests

ip = '192.168.80.239'

data = "hello from china"
while True: 
    try:
        response = requests.post(f"http://{ip}", data=data)
    except:
        print("exploded")



# arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) 
# def write_read(x): 
#     arduino.write(bytes(x, 'utf-8')) 
#     time.sleep(0.05) 
#     data = arduino.readline() 
#     return data 
# while True: 
#     num = input("Enter a number: ") # Taking input from user 
#     value = write_read(num) 
#     print(value) # printing the value 
