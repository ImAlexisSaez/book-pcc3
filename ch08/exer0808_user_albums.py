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

while True:
    artist = input("\nIntroduce artista del álbum (o 'q' para terminar): ")
    if artist == 'q':
        break

    title = input("Introduce título del álbum (o 'q' para terminar): ")
    if title == 'q':
        break

    print(make_album(artist, title))