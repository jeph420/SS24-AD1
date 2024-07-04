class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array to be sorted
        @returns a sorted list
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting

        largest_num_size = 0
        for i in input_array:
            if len(str(i)) > largest_num_size:
                largest_num_size = len(str(i))
        
        startingIndex = -1
        for _ in range(8):
            bucket = [[],[],[],[],[],[],[]]
            for i in input_array:
                index = self.get_digit(i, startingIndex)
                bucket[(len(bucket)-1)-index].append(i)
            self._add_bucket_list_to_history(bucket)
            input_array = self.merges(bucket)
            startingIndex -= 1
        return input_array

    # Helper functions

    def get_digit(self, val, pos):
        try:
            return int(str(val)[pos])
        except IndexError:
            return int(0)

    def merges(self, bucket):
        bucketCombi = []
        for i in bucket:
            bucketCombi += i
        return bucketCombi

    ##################

    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list is your current bucket list, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)
        self.bucket_list_history.append(arr_clone)