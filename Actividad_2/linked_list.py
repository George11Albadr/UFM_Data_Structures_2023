
class Node:
    
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None
        self.c_node = None
        
    def repr(self):
        return '|{}]'.format(self.data)

my_instance = Node("some data")
class LinkedList:
    
    def __init__(self, data: Node):
        self.data = data
        self.start = None
        self.count = 0

    def __iter__(self):
        node = self.start

        while node is not None:
            # print("while iter")
            yield node
            node = node.next
    
    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> ".join(nodes)
    
    def __len__(self):

        length = 0

        for _ in self:
            length += 1

        return length

    def traverse(self):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node
        self.count += 1


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''
        self.count += 1
        if self.start is None:
            self.start = new_node
            return


        for current_node in self:
            pass
    
        current_node.next = new_node
        new_node.last = current_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                new_node.last = previous_node
                current_node.last = new_node
                self.count += 1
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            self.start.last = None
            self.count -= 1
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                self.count -= 1
                if current_node.next != None:
                    current_node.next.last = previous_node
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))
        

     
          



    
    
    