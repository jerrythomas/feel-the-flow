import requests

def get_names_for_attribute(data, attribute):
		if data[attribute]:
				return [i['name'] for i in data[attribute]]
		return []

def get_pokemon(url):
		response = requests.get(url)
		result = response.json()
		return result

def get_forms(data):
		return get_names_for_attribute(data, 'forms')

def get_abilities(data):
		abilities = [data['abilities'][i]['ability']['name'] for i in range(len(data['abilities']))]
		return abilities

def get_species(data):
		return data['species']['name']

def get_name(data):
		return data['name']

def get_versions(data):
		version_names = []
		if data['game_indices']:
				version_names = [i['version']['name'] for i in data['game_indices']]
		return version_names

def get_moves(data):
		moves = []
		if data['moves']:
				moves = [i['move']['name'] for i in data['moves']]
		return moves

def get_pokemon_info(url):
		data = get_pokemon(url)
		abilities = get_abilities(data)
		forms = get_forms(data)
		versions = get_versions(data)
		moves = get_moves(data)
		return {
				'name': get_name(data),
				'height': data['height'],
				'weight': data['weight'],
				'moves': len(moves),
				'abilities': len(abilities),
				'forms': len(forms),
				'versions': len(versions),
				'species': get_species(data)
		}

def get_pokemon_list(pages=20):
		pokemons = []
		count = 0
		url = 'https://pokeapi.co/api/v2/pokemon'

		while count < pages:
				response = requests.get(url)
				result = response.json()

				url = result['next']
				pokemons.extend(result['results'])
				count += len(result['results'])
				if (pages > result['count']):
						pages = result['count']

		return pokemons

def get_pokemon_urls(count):
		urls = [ "https://pokeapi.co/api/v2/pokemon/{}".format(i+1) for i in range(count)]
		return urls

if __name__ == '__main__':
		url = 'https://pokeapi.co/api/v2/pokemon/1/'
		data = get_pokemon_list()
		print(get_pokemon_urls(20))