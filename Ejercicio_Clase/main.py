import pickle
from memory_profiler import profile
from copy import deepcopy
from d_persistence import pickle_object, unpickle_object
from stack import Stack
from linked_list import LinkedList, Node

import pickle
from memory_profiler import profile
from copy import deepcopy
from d_persistence import pickle_object, unpickle_object
from stack import Stack
from linked_list import LinkedList, Node


# Saving object 
original_list = LinkedList()
size_multiplier = 100
elements = ['1', '33', '14', '16', '4'] * size_multiplier
value = [1]

@profile
def create_list():
    for size_multiplier in value:
        for element in elements:
            _node = Node(element)
            original_list.insert_at_end(_node)
            pickle_object(original_list, './test_list')

create_list()

@profile
def reverse_with_stack(original_list: LinkedList) -> LinkedList:

    aux_stack = Stack(len(original_list))

    # Push nodes of original list into stack
    for node in original_list:
        _node_copy = deepcopy(node)
        _node_copy.next = None
        aux_stack.push(_node_copy)

    new_list = LinkedList()
    print('New empty list:', new_list)
    print('Stack after pushing:', aux_stack)
    pickle_object(aux_stack, './test_stack')

    # Pop nodes into new list
    while aux_stack.top > -1:
        _popped_node = aux_stack.pop()
        new_list.insert_at_end(_popped_node)

    #print('Stack after pupopping:', aux_stack)
    
    return new_list

# Reverse with stack
reversed_list = reverse_with_stack(original_list)
print('Reversed with stack:', reversed_list)




 

    



# Retrieving object
#s_2 = unpickle_object('./Ejercicio_Clase/saved_stack')

#print(s_2)
#print(id(s_2))

