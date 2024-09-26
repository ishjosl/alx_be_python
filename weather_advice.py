weather = ["sunny", "rainy", "cold"]
weather = input("what's the weather outside? (sunny/rainy/cold):").lower()
if weather == "sunny":
    recommendation = "wear T-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."

else:
    recommendation = "Sorry, I don't have recommendations for this weather."

print(recommendation)


