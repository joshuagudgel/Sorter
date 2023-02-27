import unittest
from sorter import Sorter
import my_constants

class TestSorter(unittest.TestCase):

    # Unittest lib method to remove redundant set up code
    def setUp(self):
        self.sorter = Sorter()

    # Initial example comparing two methods doing the same thing    
    def test_sorter_timsort(self):
        self.assertEqual(self.sorter.sorter_timsort(my_constants.UNSORTED),sorted(my_constants.UNSORTED))

    # Define specifications for 'Sorter'
    
    # Timsort returns an ordered list
    def test_timsort_in_order_unsorted(self):
        result = self.sorter.sorter_timsort(my_constants.UNSORTED)
        for i in range(0,len(result)):
            if i > 0:
                curr = result[i]
                self.assertGreater(curr,prev)
            prev = result[i]
    
    # Timsort returns empty from empty input
    def test_timsort_empty(self):
        self.assertEqual(self.sorter.sorter_timsort(my_constants.EMPTY),sorted(my_constants.EMPTY))
    
    # Runtime is updated after timsort
    # TODO: Has a chance of having a false negative
    def test_sorter_timsort_runtime_updates(self):
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_timsort(my_constants.UNSORTED)
        self.assertNotEqual(self.sorter.get_runtime(), initial_runtime)

    # Shuffle sort returns an ordered list
    def test_shuffle_unsorted_short(self):
        result = self.sorter.sorter_shuffle(my_constants.UNSORTED_SHORT)
        for i in range(0,len(result)):
            if i > 0:
                curr = result[i]
                self.assertGreater(curr,prev)
            prev = result[i]

    # Shuffle sort returns empty from empty input
    def test_shufflesort_empty(self):
        self.assertEqual(self.sorter.sorter_shuffle(my_constants.EMPTY),sorted(my_constants.EMPTY))
    
    # Runtime is updated after shuffle sort
    # TODO: Has a chance of having a false negative
    def test_sorter_shuffle_runtime_updates(self):
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_shuffle(my_constants.UNSORTED)
        self.assertNotEqual(self.sorter.get_runtime(), initial_runtime)

    # Merge sort returns an ordered list
    def test_merge_unsorted_short(self):
        result = self.sorter.sorter_merge(my_constants.UNSORTED_SHORT)
        for i in range(0,len(result)):
            if i > 0:
                curr = result[i]
                self.assertGreater(curr,prev)
            prev = result[i]

    # Merge sort returns empty from empty input
    def test_mergesort_empty(self):
        self.assertEqual(self.sorter.sorter_merge(my_constants.EMPTY),sorted(my_constants.EMPTY))

    # Runtime is updated after merge sort
    # TODO: Has a chance of having a false negative
    def test_sorter_shuffle_runtime_updates(self):
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_merge(my_constants.UNSORTED)
        self.assertNotEqual(self.sorter.get_runtime(), initial_runtime)

    # Runtime is type: afloat
    def test_sorter_runtime_is_float(self):
        self.assertIsInstance(self.sorter.get_runtime(), float)

if __name__ == '__main__':
    unittest.main()