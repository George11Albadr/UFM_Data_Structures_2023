import random
class Song:
    def __init__(self, ID: str, name: str, artist: str, album: str):
        self.ID = ID
        self.name = name
        self.artist = artist
        self.album = album
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return "| Data: {} |".format(self.name)

class Playlist:
    def __init__(self):
        self.start = None
        self.end = None
        self.current_song = None
        
    def __iter__(self):
        song = self.start
        
        while song is not None:
            yield song
            song = song.next
        
    def __repr__(self):
        songs = ["START"]
        
        for song in self:
            songs.append(song.name)
            
        songs.append("END")
        return "-->".join(songs)
    
    def insert_at_back(self, new_song: Song):
        if self.start is None:
            new_song.next = self.start
            self.start = new_song
        else:
            new_song.prev = self.end
            self.end.next = new_song
            self.end = new_song
        
    def insert_at_front(self, new_song: Song):
        if self.start is None:
            self.start = new_song
            self.end = new_song
        else:
            for current_song in self:
                pass
            new_song.next = self.start
            self.start.prev = new_song
            self.start = new_song
            
    def insert_before(self, reference_song: str, new_song: Song):
        
        if self.start is None:
            print("Empty playlist...")
            return
        
        if self.start.ID == reference_song:
            return self.insert_at_beginning(new_song)
        
        previous_song = self.start
        
        for current_song in self:
            
            if current_song.ID == reference_song:
                previous_song.next = new_song
                new_song = current_song
                return
            
            previous_song = current_song
            
        print("Reference song {} not found in playlist...".format(reference_song)) 
     
    def print_playlist(self):
        current_song = self.start
        print("--Play list--")
        while current_song is not None:
            print("ID: " + current_song.ID + "  - Song: " + current_song.name + " -  artist: " + current_song.artist + " -  Album: " + current_song.album)
            current_song = current_song.next
            
    def play(self):
        self.current_song = self.start
        if self.current_song is None:
            print("Playlist is empty")
        else:
            print("Playing Song: " + self.current_song.name)
            
    def play_next(self):
        if self.current_song is None:
            print("Playlist is empty")
        elif self.current_song.next is None:
            print("no more songs")
        else:
            self.current_song = self.current_song.next
            print("Playing next song: " + self.current_song.name) 
            
    def play_prev(self):
        if self.current_song is None:
            print("Playlist empty")
        elif self.current_song.prev is None:
            print("Beginning of playlist")
        else:
            self.current_song = self.current_song.prev
            print("Playing previous song: " + self.current_song.name) 
            
    def show_details(self):
        current_song = self.current_song
        print("ID: " + current_song.ID + "  - Song: " + current_song.name + " -  artist: " + current_song.artist + " -  Album: " + current_song.album)
        
    def search_by_name(self, name):
        current_song = self.start
        while current_song is not None:
            if current_song.name == name:
                return print("Searched Song:" + name + " - Currently playing: " + current_song.name)
            current_song = current_song.next
        return print("No artist in the album")
    
    def search_by_artist(self, artist):
        current_song = self.start
        while current_song is not None:
            if current_song.artist == artist:
                return print("Searched Artist: " + artist + " -  Songs in playlist: " + current_song.name)
            current_song = current_song.next
        return print("No songs by: " + artist)
    
    def playlist_len(self):
        current_song = self.start
        count = 0
        while current_song is not None:
            count += 1
            current_song = current_song.next
        return count
    
    def play_shuffle(self):
        if self.start is None:
            return None
            
        song_count = self.playlist_len()
        random_index = random.randint(0, song_count - 1)
    
        current_song = self.start
        index = 0
        while current_song is not None:
            if index == random_index:
                return current_song
            current_song = current_song.next
            index += 1
                    