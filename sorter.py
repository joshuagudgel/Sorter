class Sorter:
    def __init__(self):
        self._runtime = 0.0
    
    def get_runtime(self):
        return self._runtime

    def sorter_timsort(self, input_list):
        return sorted(input_list)