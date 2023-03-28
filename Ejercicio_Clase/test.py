import random
import string
from stack import Stack
from d_persistence import pickle_object, unpickle_object
from memory_profiler import profile


@profile
def create_stack(size: int) -> Stack:
    stack = Stack(size)
    while stack.memory_usage() < 100:
        element = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        stack.push(element)
    pickle_object(stack, 'random_stack.pkl')
    return stack


@profile
def read_stack_top(filename: str) -> None:
    stack = unpickle_object(filename)
    print('Top:', stack.top)


if __name__ == '__main__':
    stack = create_stack(100000)
    read_stack_top('random_stack.pkl')