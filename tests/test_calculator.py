import unittest

class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations"""
    
    def test_addition(self):
        """Test addition operation"""
        result = 2 + 3
        self.assertEqual(result, 5)
        print("Addition test passed: 2 + 3 = 5")
    
    def test_subtraction(self):
        """Test subtraction operation"""
        result = 10 - 4
        self.assertEqual(result, 6)
        print("Subtraction test passed: 10 - 4 = 6")
    
    def test_multiplication(self):
        """Test multiplication operation"""
        result = 3 * 4
        self.assertEqual(result, 12)
        print("Multiplication test passed: 3 * 4 = 12")
    
    def test_division(self):
        """Test division operation"""
        result = 20 / 4
        self.assertEqual(result, 5.0)
        print("Division test passed: 20 / 4 = 5.0")
    
    def test_division_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0
        print("Division by zero test passed")

if __name__ == '__main__':
    unittest.main()