import os

from utils.measure import measure_elapsed_time
from utils.pokemon import get_pokemon_urls, get_pokemon_info
from utils.data import write_file
from shared import parse_args

@measure_elapsed_time
def process_data_sequentially(data):
		pokemons = []

		for entry in data:
				pokemons.append(get_pokemon_info(entry))

		return pokemons

if __name__ == '__main__':
		args = parse_args()
		urls = get_pokemon_urls(args.count)
		pokemons = process_data_sequentially(urls)
		write_file(os.path.join(os.environ['DATA_DIR'], 'output','pokemons.json') , pokemons)