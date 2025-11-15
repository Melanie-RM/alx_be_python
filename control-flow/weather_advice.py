#give advise on clothing based on the weather
today_weather = input("What's the weather like today?(sunny/rainy/cold):")

if today_weather == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif today_weather == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif today_weather == "cold":
    message = "Make sure to wear a warm coat and scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."
print(message)