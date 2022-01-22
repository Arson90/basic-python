num_A = 5
num_B = 10

city_A = "Warsaw"
city_B = "Paris"

# If and Else statments
if num_A > num_B:
    print(f"City {city_A}")
else:
    print(f"City {city_B}")

# If, Elif and Else statments
if city_A == city_B:
    print("City", city_A)
elif city_A != city_B:
    print("City", city_B)
else:
    print("something else")

# Using function
def myFunction(var: str):
    print("City", var)

if not (city_A == city_B):
    myFunction(city_A)
else:
    myFunction(city_B)


