from play_list import Song, Playlist

#Songs instantation
song_1 = Song("1", "Night Prowler", "AC/DC", "Highway to Hell")
song_2 = Song("2", "Hey you", "Pink Floyd", "The Wall")
song_3 = Song("3", "Bohemian Rhapsody", "Queen", "A Night At The Opera")
song_4 = Song("4", "Comfortably Numb", "Pink Floyd", "Dark Side Of The Moon")
song_5 = Song("5", "Midnight Blues", "Gary Moore", "Still Got The Blues")
song_6 = Song("6", "Love of My Life", "Queen", "A Night At The Opera")

ll = Playlist()

ll.insert_at_front(song_1)
ll.insert_at_back(song_2)
ll.insert_at_back(song_3)
ll.insert_at_back(song_4)
ll.insert_at_back(song_5)
ll.insert_at_back(song_6)

print(ll)


#plays first song
ll.play()

#prev beginning of the playlist
ll.play_prev()

ll.play_next()
ll.play_prev()
#plays prev song
ll.play_next()
#song details comfortably numb
ll.show_details()

ll.play_next()
#song details bohemian rhapsody
ll.show_details()

ll.play_next()
ll.play_prev()

#next end of playlist
ll.play_next()
ll.play_next()
#last song scenario
ll.play_next()

ll.search_by_name("Bohemian Rhapsody")

ll.search_by_artist("Queen")

songs_count = ll.playlist_len()
print("Number of songs in playlist")
print(songs_count)

random_song = ll.play_shuffle()
print('Playing Shuffle:',random_song.name)