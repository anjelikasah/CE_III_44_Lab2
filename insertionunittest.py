import unittest
from insertionsort import insertion

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        values=[5,3,6]
        sorteddata=[3,5,6]
        insertion(values)
        print(values)
        self.assertListEqual(values,sorteddata)

if(__name__=='__main__'):
    unittest.main()
