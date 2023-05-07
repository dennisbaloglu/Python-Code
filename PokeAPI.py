import csv
import requests

# specify the number of Pokémon to retrieve
num_pokemon = 1118

# make a request to the PokéAPI to retrieve data on the first 'num_pokemon' Pokémon
response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={num_pokemon}")

# parse the response JSON data
pokemon_data = response.json()

# create a list to hold the Pokémon data
pokemon_list = []

# iterate over the results and extract data for each Pokémon
for result in pokemon_data['results']:
    # make a request to the API for each Pokémon's data
    response = requests.get(result['url'])
    pokemon_data = response.json()
    
    # extract the data we're interested in
    name = pokemon_data['name']
    id = pokemon_data['id']
    type1 = pokemon_data['types'][0]['type']['name']
    if len(pokemon_data['types']) > 1:
        type2 = pokemon_data['types'][1]['type']['name']
    else:
        type2 = ""
    hp = pokemon_data['stats'][0]['base_stat']
    attack = pokemon_data['stats'][1]['base_stat']
    defense = pokemon_data['stats'][2]['base_stat']
    special_attack = pokemon_data['stats'][3]['base_stat']
    special_defense = pokemon_data['stats'][4]['base_stat']
    speed = pokemon_data['stats'][5]['base_stat']
    
    # append the data to the Pokémon list
    pokemon_list.append([id, name, type1, type2, hp, attack, defense, special_attack, special_defense, speed])

# write the Pokémon data to a CSV file
with open('pokemon_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed'])
    writer.writerows(pokemon_list)

print(f"{num_pokemon} Pokémon data saved to pokemon_data.csv")
