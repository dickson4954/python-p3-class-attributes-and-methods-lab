class Song:
    genres=set()
    artists=set()
    
    count = 0
    def __init__(self, name, artist, genre):
        self.name = name

        self.artist = artist
        self.genre = genre
        self.genres.add(genre)
        self.artists.add(artist)

        Song.count += 1


        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

        
        
      
        

       
        
    pass
