import threading
from .pokemon_fetcher import PokemonFetcher
from requests.exceptions import HTTPError

fetcher = PokemonFetcher()

lock = threading.Lock()

def type_weight(pokemon_type: str, min_id: int=1, max_id: int=999999) -> list:
    try:
        max_min_weight = [0, 999999]
        def get_and_compare_weights(pokemon_name: str):
            pokemon_data = fetcher.get_pokemon_data(pokemon_name)
            lock.acquire()
            if pokemon_data["weight"] > max_min_weight[0] : max_min_weight[0] = pokemon_data["weight"]
            if pokemon_data["weight"] < max_min_weight[1] : max_min_weight[1] = pokemon_data["weight"]
            lock.release()

        type_data = fetcher.get_pokemon_type(pokemon_type)
        threads = []
        for pokemon in type_data["pokemon"]:
            pokemon_url = pokemon["pokemon"]["url"].strip("/").split("/")
            pokemon_id = int(pokemon_url[-1])
            if max_id < pokemon_id or pokemon_id < min_id:
                break
            fetch_thread = threading.Thread(target=get_and_compare_weights, args=(pokemon["pokemon"]["name"],))
            fetch_thread.start()
            threads.append(fetch_thread)

        for thread in threads:
            thread.join()
        return max_min_weight
    
    except HTTPError as err:
        print("The followig error raised when fetching data: ", err)
        return [None, None]
