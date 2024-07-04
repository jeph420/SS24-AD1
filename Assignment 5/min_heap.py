from typing import Optional

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def parent(self, index):
        if self.heap[index] == self.get_min():
            return None
        return self.heap[int((index-1)/2)]
    
    def left_child(self, index):
        try:
            return self.heap[(2*index + 1)]
        except IndexError:
            return None

    def right_child(self, index):
        try:
            return self.heap[(2*(index + 1))]
        except IndexError:
            return None
        
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def up_heap(self, index):
        current_value = self.heap[index]
        parent_index = int((index-1)/2)
        parent = self.heap[parent_index]
        if parent != None and current_value < parent:
            self.swap(index, parent_index)
            self.up_heap(parent_index)

    def down_heap(self, index):
        current_value = self.heap[index]
        left_child = self.left_child(index)
        right_child = self.right_child(index)
        if left_child != None and left_child < current_value: 
            child_index = self.heap.index(left_child)
            self.swap(index, child_index)
            self.down_heap(child_index)
        elif right_child != None and right_child < current_value:
            child_index = self.heap.index(right_child)
            self.swap(index, child_index)
            self.down_heap(child_index)

    def get_size(self) -> int:
        """
        @return number of elements in the min heap
        """
        return self.size

    def is_empty(self) -> bool:
        """
        @return True if the min heap is empty, False otherwise
        """
        if self.size == 0:
            return True
        else: 
            return False

    def insert(self, integer_val: int) -> None:
        """
        inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None or not an int
        """
        # TODO
        if integer_val == None or type(integer_val) != int:
            raise ValueError(f"{integer_val} must be an integer")
        
        self.heap.append(integer_val)
        self.size += 1

        self.up_heap(self.size-1)


    def get_min(self) -> Optional[int]:
        """
        returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        # TODO
        if self.size == 0:
            return None
        else: 
            return self.heap[0]

    def remove_min(self) -> Optional[int]:
        """
        removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        # TODO
        if self.size == 0:
            return None
        elif self.size == 1:
            removed_value = self.heap[0]
            self.heap.pop()
            self.size -= 1
            return removed_value
        else: 
            try:
                self.swap(0, -1)
                removed_value = self.heap.pop()
                self.size -= 1
                self.down_heap(0)
                return removed_value
            except IndexError:
                return None