import random
import time
class Sorter:
    def __init__(self):
        self._runtime = 0.0
    
    def get_runtime(self):
        return self._runtime

    def sorter_timsort(self, input_list):
        start = time.time()
        result = sorted(input_list)
        self._runtime = time.time() - start
        return result
    
    def sorter_shuffle(self, input_list):
        start = time.time()
        target = input_list.copy()
        while not self.list_in_order(target):
            random.shuffle(target)
        self._runtime = time.time() - start
        return target

    # Merge sort
    # O(nlogn) - the logn comes from the max height of binary tree
    # Divide and conquer
    def sorter_merge(self, input_list):
        raise NotImplementedError()

    def list_in_order(self, input_list):
        for i in range(0, len(input_list)):
            if i > 0 and input_list[i] < input_list[i-1]:
                return False
        return True
    
    # Helpers