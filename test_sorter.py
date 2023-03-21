from sorter import Sorter
import my_constants
import pytest

class TestSorter():

    sorter = Sorter()

    # Initial example comparing two methods doing the same thing    
    @pytest.mark.parametrize("test_input,expected", my_constants.LISTS)
    def test_sorter_timsort(self, test_input: tuple[list[int], list[int]], expected: tuple[list[int], list[int]]):
        #self.sorter = Sorter()
        assert self.sorter.sorter_timsort(test_input) == expected

    # Define specifications for 'Sorter'
    
    # Timsort returns an ordered list for each item in test list
    @pytest.mark.parametrize("test_input,expected", my_constants.LISTS)
    def test_timsort_in_order(self, test_input: tuple[list[int], list[int]],expected: tuple[list[int], list[int]]):
        #sorter = Sorter()
        assert self.sorter.sorter_timsort(test_input) == expected
    
    # Timsort returns empty from empty input
    def test_timsort_empty(self):
        #sorter = Sorter()
        assert self.sorter.sorter_timsort(my_constants.EMPTY) == []

    # Shuffle sort returns an ordered list
    # Use a short list to test because it would take too long normally
    def test_shuffle_unsorted_short(self):
        sorter = Sorter()
        assert sorter.sorter_shuffle(my_constants.UNSORTED_SHORT) == sorted(my_constants.UNSORTED_SHORT)

    # Shuffle sort returns empty from empty input
    def test_shufflesort_empty(self):
        sorter = Sorter()
        assert sorter.sorter_shuffle(my_constants.EMPTY) == []

    # Merge sort returns an ordered list for each list in tests list
    @pytest.mark.parametrize("test_input,expected", my_constants.LISTS)
    def test_mergesort_in_order(self, test_input: tuple[list[int], list[int]], expected: tuple[list[int], list[int]]):
        #sorter = Sorter()
        assert self.sorter.sorter_merge(test_input) == expected

    # Merge sort returns empty from empty input
    def test_mergesort_empty(self):
        #sorter = Sorter()
        assert self.sorter.sorter_merge(my_constants.EMPTY) == []

    # Bubble sort returns an ordered list for each list in tests list
    @pytest.mark.parametrize("test_input,expected", my_constants.LISTS)
    def test_bubblesort_in_order(self, test_input: tuple[list[int], list[int]], expected: tuple[list[int], list[int]]):
        #sorter = Sorter()
        assert self.sorter.sorter_bubble(test_input) == expected

    # Bubble sort returns empty from empty input
    def test_bubblesort_empty(self):
        #sorter = Sorter()
        assert self.sorter.sorter_bubble(my_constants.EMPTY) == []

    # TBD: future implementation
    """
    # Runtime is updated after timsort
    @pytest.mark.parametrize("test_input,expected", my_constants.LISTS)
    def test_sorter_timsort_runtime_updates(self, test_input, expected):
        #sorter = Sorter()
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_timsort(test_input)
        assert self.sorter.get_runtime() != initial_runtime
    
    # Runtime is updated after shuffle sort
    def test_sorter_shuffle_runtime_updates(self):
        #sorter = Sorter()
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_shuffle(my_constants.UNSORTED)
        assert self.sorter.get_runtime() != initial_runtime

    # Runtime is updated after bubble sort
    def test_sorter_bubble_runtime_updates(self, test_input, expected):
        #sorter = Sorter()
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_bubble(my_constants.UNSORTED)
        assert self.sorter.get_runtime() != initial_runtime

    # Runtime is type: afloat
    def test_sorter_runtime_is_float(self):
        self.sorter = Sorter()
        self.assertIsInstance(self.sorter.get_runtime(), float)
    """