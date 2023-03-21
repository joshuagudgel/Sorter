import random
import timeit
class Sorter:
    def __init__(self):
        self._runtime = 0.0
    
    def get_runtime(self):
        return self._runtime

    def sorter_timsort(self, input_list):
        result = sorted(input_list)
        return result
    
    # Shuffle sort
    # Randomly rearrange the list using python's random.shuffle
    # until all elements are in order
    def sorter_shuffle(self, input_list):
        target = input_list.copy()
        while not self.list_in_order(target):
            random.shuffle(target)
        return target

    # Bubble sort
    # O(n^2)
    # Cycle through list over and over
    # pushing the largest number to the end until list is in order
    def sorter_bubble(self, input_list):
        result = input_list.copy()
        swap_made = True
        # Continue bubbling high values along the list as long as at least one swap is made
        while swap_made:
            swap_made = False
            for i in range(0,len(result)):
                # Swap value with adjacent value in list if left > right
                if i < len(result)-1 and result[i] > result[i+1]:
                    temp = result[i]
                    result[i] = result[i+1]
                    result[i+1] = temp
                    swap_made = True
        return result

    # Merge sort
    # O(nlogn) - the logn comes from the max height of binary tree
    # Divide and conquer
    def sorter_merge(self, input_list):
        sort_type = "Merge  Sort"
        if len(input_list) <= 1:
            return input_list
        l, r = [], []
        # Call mergesort on left half and right half
        if len(input_list) > 1:
            l = self.sorter_merge(input_list[:len(input_list)//2])
            r = self.sorter_merge(input_list[len(input_list)//2:])
        # Merge the two sides efficiently
        result = self.merge(l,r)
        self.write_to_log(input_list, result, sort_type)
        return result
    
    # Helpers

    # Write output to log file
    def write_to_log(self, input_list, output_list, sort_type):
        with open("sorter.log", "a") as log:
            log.write("Sort type: " + sort_type + "\n")
            log.write("Input list: " + str(input_list) + "\n")
            log.write("Output list: " + str(output_list) + "\n")
            log.write("\n")

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