import random
import timeit
class Sorter:

    # Python's built-in sort
    # O(nlogn)
    # Uses Timsort, a hybrid of merge sort and insertion sort
    def sorter_timsort(self, input_list):
        sort_type = "Tim Sort"
        result = sorted(input_list)
        return result
    
    # Shuffle sort
    # Randomly rearrange the list using python's random.shuffle
    # until all elements are in order
    # This is should be tested on short lists
    def sorter_shuffle(self, input_list):
        sort_type = "Shuffle Sort"
        return NotImplementedError

    # Bubble sort
    # O(n^2)
    # Cycle through list over and over
    # pushing the largest number to the end until list is in order
    def sorter_bubble(self, input_list):
        sort_type = "Bubble Sort"
        return NotImplementedError

    # Merge sort
    # O(nlogn) - the logn comes from the max height of binary tree
    # Divide and conquer
    def sorter_merge(self, input_list):
        sort_type = "Merge  Sort"
        return NotImplementedError
    
    # Helpers

    # Write sort type/input/output to log file
    def write_to_log(self, input_list, output_list, sort_type):
        with open("sorter.log", "a") as log:
            log.write("Sort type: " + sort_type + "\n")
            log.write("Input list: " + str(input_list) + "\n")
            log.write("Output list: " + str(output_list) + "\n")
            log.write("\n")