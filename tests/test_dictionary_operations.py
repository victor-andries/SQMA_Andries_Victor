import unittest

class TestDictionaryOperations(unittest.TestCase):
    """Test cases for dictionary operations"""
    
    def test_dict_get(self):
        """Test getting value from dictionary"""
        my_dict = {'name': 'Jenkins', 'type': 'CI/CD'}
        value = my_dict.get('name')
        self.assertEqual(value, 'Jenkins')
        print("Dictionary get test passed")
    
    def test_dict_keys(self):
        """Test getting dictionary keys"""
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        keys = list(my_dict.keys())
        self.assertEqual(sorted(keys), ['a', 'b', 'c'])
        print("Dictionary keys test passed")
    
    def test_dict_values(self):
        """Test getting dictionary values"""
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        values = list(my_dict.values())
        self.assertEqual(sorted(values), [1, 2, 3])
        print("Dictionary values test passed")
    
    def test_dict_update(self):
        """Test updating dictionary"""
        my_dict = {'name': 'Jenkins'}
        my_dict.update({'version': '2.0'})
        self.assertIn('version', my_dict)
        self.assertEqual(my_dict['version'], '2.0')
        print("Dictionary update test passed")
    
    def test_dict_pop(self):
        """Test removing key from dictionary"""
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        value = my_dict.pop('b')
        self.assertEqual(value, 2)
        self.assertNotIn('b', my_dict)
        print("Dictionary pop test passed")
    
    def test_dict_length(self):
        """Test dictionary length"""
        my_dict = {'python': 3.11, 'jenkins': 2.528, 'git': 2.51}
        length = len(my_dict)
        self.assertEqual(length, 3)
        print("Dictionary length test passed: 3 items")

if __name__ == '__main__':
    unittest.main()