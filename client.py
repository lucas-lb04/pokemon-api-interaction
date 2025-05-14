import requests

url = 'http://127.0.0.1:5000/api/pokemon'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Liste des Pokémon :")

    for pokemon in data["pokemon1"]:
        print(f"- {pokemon['reference']} ({pokemon['color']})")

    for pokemon in data["pokemon2"]:
        print(f"- {pokemon['reference']} ({pokemon['color']})")
else:
    print(f"Erreur : {response.status_code}")

