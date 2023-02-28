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
        l, r = [], []
        # Call mergesort on left half and right half
        if len(input_list) > 1:
            l = self.sorter_merge(input_list[:len(input_list)//2])
            r = self.sorter_merge(input_list[len(input_list)//2:])
        # Merge the two sides efficiently
        return self.merge(l,r)
    
    # Helpers

    # Merge sort helper
    def merge(self, left_half, right_half):
        result = []
        # While both lists have elements
        while len(left_half) > 0 and len(right_half) > 0:
            if(left_half[0] > right_half[0]):
                result.append(right_half[0])
                right_half = right_half[1:]
            else:
                result.append(left_half[0])
                left_half = left_half[1:]
        # While elements remain in left half
        if len(left_half) > 0:
            result.append(left_half)
        # While elements remain in right half
        elif len(right_half) > 0:
            result.append(right_half)
        return result

    # Check if list is in order
    def list_in_order(self, input_list):
        for i in range(0, len(input_list)):
            if i > 0 and input_list[i] < input_list[i-1]:
                return False
        return True