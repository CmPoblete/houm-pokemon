import re
import pokemon_fetcher
from requests.exceptions import HTTPError

fetcher = pokemon_fetcher.PokemonFetcher()

def count_pokemon_by_name_filter(regex_pattern: str) -> int:
    try:
        filter_count = 0
        pokemon_names = fetcher.get_all_pokemon_names()
        for pokemon in pokemon_names:
            name_match = re.match(regex_pattern, pokemon["name"])
            if name_match is not None : filter_count += 1
        
        return filter_count
    
    except HTTPError as err:
        print("The followig error raised when fetching data: ", err)
        return -1
