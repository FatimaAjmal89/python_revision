import json

cities = {
    "Karachi" : "20million",
    "Lahore" : "14million",
    "Islamabad": "1.2million"

}
# Save to JSON file
with open("cities.json", "w") as f:
    json.dump(cities , f)

#load
with open("cities.json", "r") as f :
    data = json.load(f)

for city,population in data.items():
    print(city , ":" ,population)

# Update JSON file
city = input("city input : ")
population = input("population input : ")

cities[city] = population

with open("cities.json", "w") as f:
    json.dump(cities , f)


