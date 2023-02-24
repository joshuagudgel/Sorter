import random
class Sorter:
    def __init__(self):
        self._runtime = 0.0
    
    def get_runtime(self):
        return self._runtime

    def sorter_timsort(self, input_list):
        return sorted(input_list)
    
    def sorter_shuffle(self, input_list):
        target = input_list.copy()
        while not self.list_in_order(target):
            random.shuffle(target)
        return target

    def list_in_order(self, input_list):
        for i in range(0, len(input_list)):
            if i > 0 and input_list[i] < input_list[i-1]:
                return False
        return True