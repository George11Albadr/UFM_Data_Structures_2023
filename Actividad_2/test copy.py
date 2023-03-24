from linked_list import LinkedList, Node
from data_persistence import Recursion
from memory_profiler import profile
import sys
import pickle

original_list = LinkedList(data=None)
size_multiplier = 49
elements = ['1', '33', '14', '16', '4'] * size_multiplier

@profile
def create():
    for element in elements:
        _node = Node(element)
        original_list.insert_at_end(_node)


def save_list_to_file(ll, filename):
    with open(filename, 'wb') as f:
        pickle.dump(ll, f)
@profile
def load_list_from_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
@profile    
def traverse(original_list):
    for node in original_list:
        pass
    

@profile
def main():
    create()
    original_list = LinkedList(data = None)
    for element in elements:
        _node = Node(element)
        original_list.insert_at_end(_node)
    traverse(original_list)
    sys.setrecursionlimit(1000000)
    print(sys.getrecursionlimit())
    save_list_to_file(original_list, 'list.pkl')
    original_list_from_file = load_list_from_file('list.pkl')
    traverse(original_list_from_file)

if __name__ == '__main__':
    main()

print(original_list)