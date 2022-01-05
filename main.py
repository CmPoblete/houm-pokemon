from src.count_pokemon_by_name_filter import count_pokemon_by_name_filter
from src.pokemon_breeding import breeding_count
from src.type_weight import type_weight
#-----------------------------------------------------
# Count pokemon 

# This regex searches for every pokemon that have 'at' and exactly 2 'a's in their name (no more or less)
# below the line 10 there's a regex pattern that checks for every pokemon that have 'at' and al least 2 'a's in their name
pattern = "^(?=[^a]*a[^a]*?a)(?![^a]*a[^a]*?a[^a]*?a)(?=.*at).*"
# pattern = "^(?=[^a]*a[^a]*?a)(?=.*at).*"

count_pokemon = count_pokemon_by_name_filter(pattern)

print("Pokemon withtwo 'a's and 'at': ", count_pokemon)

#------------------------------------------------------
# Count of posible breedings of one species

raichu = breeding_count("raichu")
print("Number of posible breedings with this pokemon: ", raichu)

#------------------------------------------------------
# Min and Max weight of a Pokemon type

weights = type_weight("fighting", min_id=1, max_id=151)
print("Max and min weight of fighting pokemons from 1'st generation: ", weights)

#------------------------------------------------------