def song_decoder(song):
    words = song.replace("WUB", " ").split()
    song = " ".join(words)
    return song
