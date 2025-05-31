weather = input("What's the weather like today? (sunny/rainy/cold)")
advise = ""

if weather == "sunny":
    advise = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    advise = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    advise = "Make sure to wear a warm coat and a scarf."
else:
    advise = "Sorry, I don't have recommendations for this weather."

print(advise)