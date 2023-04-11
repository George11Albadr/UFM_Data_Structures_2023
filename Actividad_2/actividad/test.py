from playlist import Node, PlayList, Song
from memory_profiler import profile
import time
import sys

@profile
def insert_nodes(ll):
    for i in range(400):
        song_a = Song('A',"Tears in Heaven", "Eric Clapton", "Heaven")
        song_b = Song('B', "Ophelia", "The Lumineers", "Cleopatra")
        song_c = Song('C', "Quesadilla", "Tortolala", "Hits de progra")
        song_d = Song('D', "Hamburguesa", "Tortolala", "Hits de progra")

        node_a = Node(song_a)
        node_b = Node(song_b)
        node_c = Node(song_c)
        node_d = Node(song_d)

        ll.insert_at_beginning(node_c)
        ll.insert_at_beginning(node_b)
        ll.insert_at_beginning(node_a)
        ll.insert_at_beginning(node_d)
    return ll

@profile
def traverse(ll):
    tiempo = time.time()
    for node in ll:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo
    print("Tardo ", total ,'segundos sin el pickle')

@profile
def traverse_with_pickle(ll,filename):
    sys.setrecursionlimit(1000000)
    ll.persist_data(filename)
    loaded_linked_list = ll.load_data(filename)
    tiempo = time.time()
    for node in loaded_linked_list:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo
    print("Tardo ", total ,'segundos con el pickle')
    # cargar pickle
    pass


@profile
def traverse_with_pickle(ll,filename):
    sys.setrecursionlimit(1000000)
    ll.persist_data(filename)
    loaded_linked_list = ll.load_data(filename)
    tiempo = time.time()
    for node in loaded_linked_list:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo
    print("Tardo ", total ,'segundos con el pickle')
    # cargar pickle
    pass

@profile
def main():
    ll = PlayList()
    ll = insert_nodes(ll)
    traverse(ll)
    sys.setrecursionlimit(1000000)
    traverse_with_pickle(ll,'poop')
    # guardar en pickle

main()