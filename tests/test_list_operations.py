import unittest

class TestListOperations(unittest.TestCase):
    """Test cases for list operations"""
    
    def test_list_append(self):
        """Test appending to a list"""
        my_list = [1, 2, 3]
        my_list.append(4)
        self.assertEqual(my_list, [1, 2, 3, 4])
        print("List append test passed")
    
    def test_list_remove(self):
        """Test removing from a list"""
        my_list = [1, 2, 3, 4]
        my_list.remove(3)
        self.assertEqual(my_list, [1, 2, 4])
        print("List remove test passed")
    
    def test_list_sort(self):
        """Test sorting a list"""
        my_list = [3, 1, 4, 2]
        my_list.sort()
        self.assertEqual(my_list, [1, 2, 3, 4])
        print("List sort test passed")
    
    def test_list_reverse(self):
        """Test reversing a list"""
        my_list = [1, 2, 3, 4]
        my_list.reverse()
        self.assertEqual(my_list, [4, 3, 2, 1])
        print("List reverse test passed")
    
    def test_list_index(self):
        """Test finding index in list"""
        my_list = ['apple', 'banana', 'cherry']
        index = my_list.index('banana')
        self.assertEqual(index, 1)
        print("List index test passed")
    
    def test_list_count(self):
        """Test counting elements in list"""
        my_list = [1, 2, 2, 3, 2, 4]
        count = my_list.count(2)
        self.assertEqual(count, 3)
        print("List count test passed: 2 appears 3 times")

if __name__ == '__main__':
    unittest.main()