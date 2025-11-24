FAHRENHEIT_TO_CELSIUS_FACTOR = 0
CELSIUS_TO_FAHRENHEIT_FACTOR  = 0
num = int(input("enter the temperature"))
unit = input("Is the tempetature in celsius or fahrenheit")

def convert_to_celsius(num):
    FAHRENHEIT_TO_CELSIUS_FACTOR = (num - 32) * 5/9
    print( FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(num):
    CELSIUS_TO_FAHRENHEIT_FACTOR = (num * 9/5) -32
    print( CELSIUS_TO_FAHRENHEIT_FACTOR)

if unit == 'celsius':
    convert_to_fahrenheit(num)
elif unit == 'fahrenheit':
    convert_to_celsius(num)
else :
    print("invalid temprature. Please enter a numeric value")