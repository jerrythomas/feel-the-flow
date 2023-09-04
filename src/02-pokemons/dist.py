import os
from multiprocessing import Pool, cpu_count, freeze_support
from utils.measure import measure_elapsed_time
from utils.pokemon import get_pokemon_urls, get_pokemon_info
from utils.data import write_file
from shared import parse_args
from prefect import task, flow

@task
def get_pokemon_data(url):
		return get_pokemon_info(url)

@task
def write_pokemon_data(pokemons):
	write_file(os.path.join(os.environ['DATA_DIR'], 'output','pokemons.json') , pokemons)

@measure_elapsed_time
@flow
def process_data_flow(data):
		pokemons = get_pokemon_data.map(data)
		return pokemons

if __name__ == '__main__':
		args = parse_args()
		freeze_support()
		urls = get_pokemon_urls(args.count)
		pokemons = process_data_flow(urls)
