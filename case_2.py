import random
from datetime import timedelta

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""


playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One" : 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)
def parse_playlist(playlist):
    songs = []
    if isinstance(playlist, str):
        for line in playlist.strip().split("\n"):
            parts = line.rsplit(" ", 1)
            if len(parts) == 2 and ":" in parts[1]:
                song_name = parts[0]
                minutes, seconds = map(int, parts[1].split(":"))
                duration = minutes * 60 + seconds
                songs.append(duration)
            elif len(parts) == 2 and "." in parts[1]:
                song_name = parts[0]
                minutes, seconds = map(int, parts[1].split("."))
                duration = minutes * 60 + seconds
                songs.append(duration)
    elif isinstance(playlist, tuple) and all(isinstance(item, dict) for item in playlist):
        for song_dict in playlist:
            for duration in song_dict.values():
                minutes, seconds = map(int, str(duration).split("."))
                duration = minutes * 60 + seconds
                songs.append(duration)
    return songs

def get_duration(playlist, n):
    song_durations = parse_playlist(playlist)
    if n > len(song_durations):
        raise ValueError(f"Недостаточно песен в плейлисте! Доступно: {len(song_durations)}.")
    random_durations = random.sample(song_durations, n)
    total_seconds = sum(random_durations)
    total_time = timedelta(seconds=total_seconds)
    return total_time

if __name__ == "__main__":
    n_songs = 3
    playlist_1 = playlist_e
    playlist_2 = playlist_f
    duration_1 = get_duration(playlist_1, n_songs)
    print(f"Общее время звучания {n_songs} случайных песен из первого плейлиста: {duration_1}")
    duration_2 = get_duration(playlist_2, n_songs)
    print(f"Общее время звучания {n_songs} случайных песен из второго плейлиста: {duration_2}")

