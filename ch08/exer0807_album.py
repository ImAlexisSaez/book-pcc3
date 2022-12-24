def make_album(artist_name, album_title, number_songs=None):
    """Devuelve diccionario de un álbum."""
    if number_songs:
        album = {
            'artist': artist_name,
            'title': album_title,
            'songs': number_songs,
        }
    else:
        album = {
            'artist': artist_name,
            'title': album_title,
        }
    return album

print(make_album('Beatles', 'White Album'))
print(make_album('Beatles', 'White Album', 27))