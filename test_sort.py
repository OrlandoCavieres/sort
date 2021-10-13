import unittest
import sort

class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
        
    def test_quick_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.quick_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])
        
    def test_quick_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.quick_sort(a)
        self.assertEqual(a, [1])

    def test_selection_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [3, 5, 7, 4, 1]
        sort.selection_sort(a)
        self.assertEqual(a, [1, 3, 4, 5, 7])

    def test_selection_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [0, 8, 1, 2, 1, 7]
        sort.selection_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 7, 8])

    def test_selection_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [5]
        sort.selection_sort(a)
        self.assertEqual(a, [5])

    def test_bubble_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 10, 0, 5, 3]
        sort.bubble_sort(a)
        self.assertEqual(a, [0, 1, 3, 5, 10])

    def test_bubble_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [1, 1, 0, 25, 7, 12]
        sort.bubble_sort(a)
        self.assertEqual(a, [0, 1, 1, 7, 12, 25])

    def test_bubble_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [2]
        sort.bubble_sort(a)
        self.assertEqual(a, [2])

    def test_insertion_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [7, 9, 0, 2, 1]
        sort.insertion_sort(a)
        self.assertEqual(a, [0, 1, 2, 7, 9])

    def test_insertion_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [1, 0, 1, 10, 6, 20]
        sort.insertion_sort(a)
        self.assertEqual(a, [0, 1, 1, 6, 10, 20])

    def test_insertion_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [10]
        sort.insertion_sort(a)
        self.assertEqual(a, [10])


if __name__ == '__main__':
    unittest.main()