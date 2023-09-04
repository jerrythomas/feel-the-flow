import os
from multiprocessing import Pool, cpu_count, freeze_support
from utils.measure import measure_elapsed_time
from utils.pokemon import get_pokemon_urls, get_pokemon_info
from utils.data import write_file
from shared import parse_args

@measure_elapsed_time
def process_data_mp(data):
		pokemons = []

		pool = Pool(cpu_count())
		pokemons = pool.map(get_pokemon_info, data)
		pool.close()
		pool.join()

		return pokemons

if __name__ == '__main__':
		args = parse_args()
		freeze_support()
		urls = get_pokemon_urls(args.count)
		pokemons = process_data_mp(urls)
		write_file(os.path.join(os.environ['DATA_DIR'], 'output','pokemons.json') , pokemons)