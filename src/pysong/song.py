import random

def suggest_song(genre_code):
    songs={
        1: ["Song1", "Song2", "Song3"],
        2: ["Song4", "Song5", "Song6"],
        3: ["Song7", "Song8", "Song9"]
    }
    if genre_code in songs:
        return random.choice(songs[genre_code])
    else:
        return "No songs available for this genre"