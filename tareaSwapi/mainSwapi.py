import requests
import json


def getData(url):
    request = requests.get(url).json()
    data = request["results"]

    while request["next"]:
        request = requests.get(request["next"]).json()
        data += request["results"]
    return data


allPeople = getData("https://swapi.dev/api/people/")
count = 0
wookies = []
for people in allPeople:
    if len(people["species"]) > 0:
        if people["species"][0] == "https://swapi.dev/api/species/3/":
            wookies.append((people["name"]))
            for film in people["films"]:
                if film == "https://swapi.dev/api/films/6/":
                    count += 1

print(f"El total de Wookies en Star Wars 6 es de {count} y se llaman {wookies[0]} y {wookies[1]}")


planets = requests.get("https://swapi.dev/api/planets/").json()

aridos = 0
for planet in planets["results"]:
    if (planet["climate"] == "arid"):
        aridos += len(planet["films"])

print(f'Películas en las que hay climas áridos: {aridos}')

naves_all = getData("https://swapi.dev/api/starships/")
i = 0
allSizes = []
for nave in naves_all:
    try:
        if nave["length"] != "unknown":
            allSizes.append(float(nave["length"]))
    except ValueError:
        pass

target = (max(allSizes))

for nave in naves_all:
    try:
        if nave["length"] != "unknown":
            if float(nave["length"]) == target:
                granNave = nave["name"]
                size = nave["length"]
    except ValueError:
        pass

print(f'La aeronave más grande de Star Wars es {granNave} y mide {size}')
