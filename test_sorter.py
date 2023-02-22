import unittest
from sorter import Sorter

UNSORTED: list = [4,2,1,6,9,3,7,5,8,0]
EMPTY: list = []

class TestSorter(unittest.TestCase):

    # setUp()
    def setUp(self):
        self.sorter = Sorter()

    # just an example    
    def test_sorter_timsort(self):
        sorter = Sorter()
        self.assertEqual(sorter.sorter_timsort(UNSORTED),sorted(UNSORTED))

    """ define specifications for 'Sorter' """
    # timsort returns an ordered list
    def test_timsort_in_order_unsorted(self):
        sorter = Sorter()
        result = sorter.sorter_timsort(UNSORTED)
        for i in range(0,len(result)):
            if i > 0:
                curr = result[i]
                self.assertGreater(curr,prev)
            prev = result[i]
    
    # timsort returns empty from empty input
    def test_timsort_empty(self):
        sorter = Sorter()
        self.assertEqual(sorter.sorter_timsort(EMPTY),sorted(EMPTY))

    # object variable runtime is afloat
    def test_sorter_runtime_is_float(self):
        sorter = Sorter()
        self.assertIsInstance(sorter.get_runtime(), float)
    
    # runtime is updated after sort
    def test_sorter_runtime_updates(self):
        sorter = Sorter()
        initial_runtime = sorter.get_runtime()
        sorter.sorter_timsort(UNSORTED)
        self.assertNotEqual(sorter.get_runtime(), initial_runtime)

if __name__ == '__main__':
    unittest.main()