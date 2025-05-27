player = {
    "name": "ROHIT",
    "team": "MI",
    "age": 37
}
print("Original dictionary:", player)

print("Keys:", player.keys())

print("Values:", player.values())

print("Items:", player.items())

print("Team (using get):", player.get("team"))

player.update({"score": 200, "age": 36}) 
print("\nAfter update:", player)

removed_score = player.pop("score")
print("Popped 'score':", removed_score)
print("After popping score:", player)


last_pair = player.popitem()
print("Popped last item (popitem):", last_pair)
print("After popitem:", player)


copied_player = player.copy()
print("Copied dictionary:", copied_player)

player.clear()
print("After clear():", player)

