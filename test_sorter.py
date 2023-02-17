import unittest
from sorter import Sorter

UNSORTED: list = [4,2,1,6,9,3,7,5,8,0]

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter.merge_sort(UNSORTED)

    # just an example    
    def test_sorter_merge(self):
        self.assertEqual(Sorter.sorter_merge(UNSORTED),sorted(UNSORTED))

    """ define specifications for 'Sorter' """

    # mergesort global variable runtime is afloat
    def test_merge_sort_updates_runtime_float(self):
        self.assertIsInstance(Sorter.runtime, float)
    
    # merge sort returns an ordered list

    # merge sort updates a global variable: 'runtime' 

if __name__ == '__main__':
    unittest.main()