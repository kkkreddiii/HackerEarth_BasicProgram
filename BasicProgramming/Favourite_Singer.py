def count_favorite_songs(playlist, songs):
    songs_count = {}
    for song in songs:
        if song in songs_count:
            songs_count[song] += 1
        else:
            songs_count[song] = 1

    # Find the maximum count of songs by any singer
    max_songs = max(songs_count.values())

    # Count how many singers have songs equal to max_songs
    favorite_song_count = sum(1 for count in songs_count.values() if count == max_songs)

    return favorite_song_count


# Reading input
playlist = int(input().strip())
songs = list(map(int, input().strip().split()))

# Counting favorite singers
result = count_favorite_songs(playlist, songs)

# Output the result
print(result)
