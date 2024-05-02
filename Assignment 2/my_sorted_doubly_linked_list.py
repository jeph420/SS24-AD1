from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        # TODO
        if index not in range(self._size):
            raise ValueError("Index is not in range.")
        elif type(index) != int:
            raise ValueError("Index must be an integer.")
        else:
            current_node = self._head
            i = 0
            while i != index:
                next_item = current_node.next_node
                current_node = next_item
                i += 1
            else:
                return current_node.elem

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        if type(val) != int:
            raise ValueError("The searchable value must be an integer")
        else:
            current_node = self._head
            index = 0
            while current_node.elem != val:
                next_item = current_node.next_node
                current_node = next_item
                index += 1
            return index

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        inserted_node = MyListNode(val)
        current_node = self._head
        while current_node.elem < inserted_node.elem:
            next_item = current_node.next_node
            current_node = next_item
        else:
            current_node.prev_node.next_node = inserted_node
            inserted_node.prev_node = current_node.prev_node
            inserted_node.next_node = current_node
            current_node.prev_node = inserted_node
            self._size += 1
            #print(self)

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        if type(val) != int:
            raise ValueError("The specified value must be an integer")
        else:
            current_node = self._head
            while current_node != None:
                if current_node.elem != val:
                    next_item = current_node.next_node
                    current_node = next_item
                else:
                    current_node.next_node.prev_node = current_node.prev_node
                    current_node.prev_node.next_node = current_node.prev_node
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    return True
            else: 
                return False

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        current_node = self._head
        if type(val) != int:
            raise ValueError("The specified value must be of integer type")
        while current_node != None:
            if current_node.elem == val:
                if current_node.next_node != self._tail:
                    next_item = current_node.next_node
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    current_node = next_item
                else:
                    current_node.prev_node.next_node = self._tail
                    self._tail.prev_node = current_node.prev_node
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    return True
            elif current_node.next_node != self._tail:
                next_item = current_node.next_node
                current_node = next_item
            else:
                return True
        else:
            return False

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        # TODO
        current_node = self._head
        original = current_node
        #### Regular Search ####
        while original != None and original.next_node != None:
            ### Duplicate Search ###
            next_item  = original.next_node
            switch = True
            while switch == True:
                if next_item.elem == original.elem:
                    future_node = next_item.next_node
                    original.next_node = future_node
                    future_node.prev_node = original
                    ######## Cleaning up ########
                    next_item.elem = None
                    next_item.next_node = None
                    next_item.prev_node = None
                    #############################
                    self._size -= 1
                    next_item = future_node
                switch = False
            next_item = original.next_node
            original = next_item

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        # TODO
        if type(n) != int:
            raise ValueError("The specified value must be an integer")
        elif n < 1 or n > self._size:
            raise ValueError(f"{n} is out of range")
        else:
            index = 0
            current_node = self._head
            while index != self._size-n:
                if current_node.next_node != None:
                    next_item = current_node.next_node
                    next_item.prev_node = current_node.prev_node
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._head = next_item
                    current_node = self._head
                    index += 1    

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        # TODO
        current_node = self._head
        switch = True
        while switch == True:
            if current_node.next_node != None:
                if current_node.elem % 2 == 0:
                    if current_node.prev_node != None:
                        next_item = current_node.next_node
                        current_node.prev_node.next_node = next_item
                        next_item.prev_node = current_node.prev_node
                        ######## Cleaning up ########
                        current_node.prev_node = None
                        current_node.next_node = None
                        current_node.elem = None
                        #############################
                        self._size -= 1
                        current_node = next_item
                    else: 
                        next_item = current_node.next_node
                        next_item.prev_node = current_node.prev_node
                        ######## Cleaning up ########
                        current_node.prev_node = None
                        current_node.next_node = None
                        current_node.elem = None
                        #############################
                        self._size -= 1
                        current_node = next_item
                else: 
                    next_item = current_node.next_node
                    current_node = next_item
            else:
                next_item = current_node.next_node
                current_node.prev_node.next_node = next_item
                ######## Cleaning up ########
                current_node.prev_node = None
                current_node.next_node = None
                current_node.elem = None
                #############################
                self._size -= 1
                switch = False

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        # TODO
        current_node = self._head
        switch = True
        while switch != False:
            if current_node.elem % 2 != 0:
                if current_node.prev_node == None:
                    next_item = current_node.next_node
                    next_item.prev_node = None
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    self._head = next_item
                    current_node = self._head

                elif current_node.next_node == None:
                    current_node.prev_node.next_node = None
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    switch = False
                else: 
                    next_item = current_node.next_node
                    current_node.prev_node.next_node = next_item
                    next_item.prev_node = current_node.prev_node
                    ######## Cleaning up ########
                    current_node.prev_node = None
                    current_node.next_node = None
                    current_node.elem = None
                    #############################
                    self._size -= 1
                    current_node = next_item
            else: 
                if current_node.next_node != None:
                    next_item = current_node.next_node
                    current_node = next_item
                else: 
                    switch = False

