import requests
from time import sleep


try:
    response = requests.get('https://www.xcccss.sw')

except BaseException as moshe:
    print (f"Unable to connect to the server {moshe.args}")



time_to_sleep = input ("time_to_s;leep: ")
sleep(time_to_sleep)
for i in range(1,14):
    print ("hello")

a = int(input("Enter first   number: "))
b = int(input("Enter second number: "))

res = (a/b)
print (res)
print ("moshe")
print ("shay")
print("a")


