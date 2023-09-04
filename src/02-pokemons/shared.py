import argparse

def parse_args():
		parser = argparse.ArgumentParser(description='Process pokemons.')
		parser.add_argument('--count', type=int, default=20, help='Number of pokemons to process')
		return parser.parse_args()