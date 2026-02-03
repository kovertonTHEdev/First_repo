games = [
    {"id": 101, "title": "Cyberpunk 2077"},
    {"id": 102, "title": "The Witcher 3"},
    {"id": 103, "title": "SWAT 4"},
    {"id": 104, "title": "Metro 2033"},
]

owned_ids = {102, 103}
installed_ids = {103}

for game in games:
    if game ["id"] in owned_ids:
        status = "INSTALL"
        if game ["id"] in installed_ids:
                status = "PLAY"
    else: 
        status = "BUY"
    print(f'{game["title"]}: {status}')



catalog = {
    101: "Cyberpunk 2077",
    102: "The Witcher 3",
    103: "SWAT 4",
}

cart_ids = [103, 999, 101, 103]

for game_id in cart_ids:
    if game_id in catalog:
        print(f"OK: {catalog[game_id]}")
    else:
        print(f"MISSING: {game_id}")



profile = {
    "username": "andrewn",
    "email": "andrew@gmail.com",
    "age": 24,
    "country": "Ukraine"
}


for key, value in profile.items():
     print(f"{key} : {value}")
