from tmdbwrapper import TV

popular = TV.popular()

for idx, show in enumerate(popular['results'], start=1):
    print(f"{idx}. {show['name']} - {show['popularity']}")
