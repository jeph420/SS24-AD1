class MaxHeap:
    def __init__(self, input_array):
        """
        @param input_array from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up max heap in place.
        """
        self.heap = None
        self.size = 0
        # TODO
        if input_array == None:
            raise ValueError("Input List must have numbers in it!!")
        else:
            input_size = len(input_array)
            for i in range((input_size//2)-1, -1, -1):
                self.recursive_heap(input_array, input_size, i)
            self.heap = input_array
            self.size = input_size

    ########### HELPER FUNCTONS ###########
    def recursive_heap(self, input_array, input_size, current_node):

        root_index = current_node
        left_child_index = self.left_child(current_node)
        right_child_index = self.right_child(current_node)

        if left_child_index < input_size and input_array[left_child_index] > input_array[root_index]:
            root_index = left_child_index

        if right_child_index < input_size and input_array[right_child_index] > input_array[root_index]:
            root_index = right_child_index

        if root_index != current_node:
            input_array[current_node], input_array[root_index] = input_array[root_index], input_array[current_node]  # swap

            self.recursive_heap(input_array, input_size, root_index)

    def left_child(self, index):
        try:
            return (2*index + 1)
        except IndexError:
            return None

    def right_child(self, index):
        try:
            return (2*(index + 1))
        except IndexError:
            return None
        
    def parent(self, index):
        return self.heap[int((index-1)/2)]
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def down_heap(self, index):
        current_value = self.heap[index]
        left_child = self.left_child(index) 
        right_child = self.right_child(index) 
        if left_child in range(self.size) and self.heap[left_child] > current_value: 
            child_index = left_child
            self.swap(index, child_index)
            self.down_heap(child_index)
        elif right_child in range(self.size) and self.heap[right_child] > current_value:
            child_index = right_child
            self.swap(index, child_index)
            self.down_heap(child_index)

    def down_heap_sorting(self, arr, n, i):
        largest = i  
        left_child = (2*i) + 1  
        right_child = 2*(i + 1)  

        if left_child < n and arr[i] < arr[left_child]:
            largest = left_child

        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child

        if largest != i:
            self.swap(i, largest)
            self.down_heap_sorting(arr, n, largest)
    #######################################

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Does not search the entire array sequentially, but uses the
        properties of a heap.
        """
        # TODO
        if val == None:
            raise ValueError("Can't look for NoneType object! Please use a number.")
        else: 
            lowest_parent = self.heap[(self.size//2)-1]
            node_index = self.heap.index(lowest_parent)
            while True:
                if val == lowest_parent:
                    return True
                elif val > lowest_parent:
                    new_parent = self.parent(node_index)
                    lowest_parent = new_parent
                    node_index = (node_index-1)//2
                elif val < lowest_parent:
                    if (self.left_child(node_index) in range(self.size) and val == self.heap[self.left_child(node_index)]) or (self.right_child(node_index) in range(self.size) and val == self.heap[self.right_child(node_index)]):
                        return True
                    elif node_index == 0:
                        return False
                    else: 
                        new_parent = self.heap[node_index+1]
                        lowest_parent = new_parent
                        node_index += 1
        

    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        # TODO
        for i in range(self.size-1, 0, -1):
            self.swap(i, 0)
            self.down_heap_sorting(self.heap, i, 0)

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        # TODO
        if self.size == 0:
            return None
        elif self.size == 1:
            removed_max = self.heap[-1]
            self.heap.pop(-1)
            self.size -= 1
            return removed_max
        self.swap(0,-1)
        removed_max = self.heap[-1]
        self.heap.pop(-1)
        self.size -= 1
        self.down_heap(0)
        return removed_max
