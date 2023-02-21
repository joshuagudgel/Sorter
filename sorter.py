class Sorter:
    def __init__(self):
        self._runtime = 0.0
    
    def get_runtime(self):
        raise NotImplementedError()

    def sorter_timsort(self, input_list):
        raise NotImplementedError()