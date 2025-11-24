#converts temperature
temp = input("enter the unit of measurement(celsius or fahrenheit)")
FAHRENHEIT_TO_CELSIUS_FACTOR = (f -32) * 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = (c * 5/9) + 32

def convert_to_celsius(fahrenheit):
    f = input("enter the temperature in fahrenheit")
    answer =FAHRENHEIT_TO_CELSIUS_FACTOR #(f - 32 ) * 5/9

def convert_to_fahrenheit(celsius):
    c = input("enter the temperature in celsius")
    answer = CELSIUS_TO_FAHRENHEIT_FACTOR#(c * 5/9) + 32

if temp == "celsius":
    convert_to_fahrenheit
elif temp == "fahrenheit":
    convert_to_celsius
else :
    print("invalid temprature. Please enter a numeric value")