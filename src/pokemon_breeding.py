from .pokemon_fetcher import PokemonFetcher
from requests.exceptions import HTTPError

fetcher = PokemonFetcher()

def breeding_count(pokemon: str) -> int:
    try:
        pokemon_name_set = set()
        pokemon_data = fetcher.get_pokemon_species_data(pokemon)

        for egg_group in pokemon_data["egg_groups"]:
            egg_group_data = fetcher.get_egg_group(egg_group["name"])
            for pokemon_species in egg_group_data["pokemon_species"]:
                pokemon_name_set.add(pokemon_species["name"])

        return len(pokemon_name_set) - 1
    except HTTPError as err:
        print("The followig error raised when fetching data: ", err)
        return -1
