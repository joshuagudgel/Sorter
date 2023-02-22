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
        self.assertEqual(self.sorter.sorter_timsort(UNSORTED),sorted(UNSORTED))

    """ define specifications for 'Sorter' """

    """ timsort """
    # timsort returns an ordered list
    def test_timsort_in_order_unsorted(self):
        result = self.sorter.sorter_timsort(UNSORTED)
        for i in range(0,len(result)):
            if i > 0:
                curr = result[i]
                self.assertGreater(curr,prev)
            prev = result[i]
    
    # timsort returns empty from empty input
    def test_timsort_empty(self):
        self.assertEqual(self.sorter.sorter_timsort(EMPTY),sorted(EMPTY))

    # object variable runtime is afloat
    def test_sorter_runtime_is_float(self):
        self.assertIsInstance(self.sorter.get_runtime(), float)
    
    # runtime is updated after sort
    def test_sorter_runtime_updates(self):
        initial_runtime = self.sorter.get_runtime()
        self.sorter.sorter_timsort(UNSORTED)
        self.assertNotEqual(self.sorter.get_runtime(), initial_runtime)

if __name__ == '__main__':
    unittest.main()