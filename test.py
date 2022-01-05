from src.count_pokemon_by_name_filter import count_pokemon_by_name_filter
from src.pokemon_breeding import breeding_count
from src.type_weight import type_weight
#-----------------------------------------------------
#Count pokemon 

pattern = "^(?=[^a]*a[^a]*?a)(?![^a]*a[^a]*?a[^a]*?a)(?=.*at).*"

count_pokemon = count_pokemon_by_name_filter(pattern)

print("Pokemon withtwo 'a's and 'at': ", count_pokemon)

#------------------------------------------------------
#Count of posible breedings of one species

raichu = breeding_count("raichu")
print("Number of posible breedings with this pokemon: ", raichu)

#------------------------------------------------------
#Min and Max weight of a Pokemon type

weights = type_weight("fighting", min_id=1, max_id=151)
print("Max and min weight of fighting pokemons from 1'st generation: ", weights)

#------------------------------------------------------