import requests

class PokemonFetcher:

    def __init__(self) -> None:
        self.base_url = "https://pokeapi.co/api/v2"
    
    def get_all_pokemon_names(self, limit: int=500) -> list:
        endpoint_url = self._endpoint_url_builder("pokemon",limit=limit)
        names = self._get(endpoint_url)
        results = names["results"]
        while names["next"] is not None:
            names = self._get(names["next"])
            results += names["results"]
        return results
    
    def get_pokemon_data(self, pokemon: str) -> dict:
        endpoint_url = self._endpoint_url_builder("pokemon", id_name=pokemon)
        return self._get(endpoint_url)

    def get_pokemon_species_data(self, pokemon: str) -> dict:
        endpoint_url = self._endpoint_url_builder("pokemon-species", id_name=pokemon)
        return self._get(endpoint_url)

    def get_pokemon_type(self, pokemon_type: str) -> dict:
        endpoint_url = self._endpoint_url_builder("type", id_name=pokemon_type)
        return self._get(endpoint_url)

    def get_egg_group(self, egg_group: str) -> dict:
        endpoint_url = self._endpoint_url_builder("egg-group", id_name=egg_group)
        return self._get(endpoint_url)

    @staticmethod
    def _get(url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def _endpoint_url_builder(self, endpoint: str, id_name: str="", limit: int=20) -> str:
        if id_name == "":
            ending = f"?limit={limit}"
        else:
            ending = id_name
        endpoint_url = f"{self.base_url}/{endpoint}/{ending}"
        
        return endpoint_url