weather = input("What's the weather like today? (sunny/rainy/cold):")
advise = ""

if weather == "sunny":
    advise = "Wear a t-shirt and sunglasses"
if weather == "rainy":
    advise = "Don't forget your umbrella and a raincoat"
if weather == "cold":
    advise = "Make sure to wear a warm coat and a scarf"

if advise == "":
    print("Sorry, I don't have recommendations for this weather")