import unittest

class TestStringOperations(unittest.TestCase):
    """Test cases for string operations"""
    
    def test_uppercase(self):
        """Test string to uppercase conversion"""
        text = "hello world"
        result = text.upper()
        self.assertEqual(result, "HELLO WORLD")
        print("Uppercase test passed")
    
    def test_lowercase(self):
        """Test string to lowercase conversion"""
        text = "HELLO WORLD"
        result = text.lower()
        self.assertEqual(result, "hello world")
        print("Lowercase test passed")
    
    def test_string_length(self):
        """Test string length calculation"""
        text = "Testing"
        result = len(text)
        self.assertEqual(result, 7)
        print(f"String length test passed: {result}")
    
    def test_string_split(self):
        """Test string splitting"""
        text = "Hello World Testing"
        result = text.split()
        self.assertEqual(len(result), 3)
        self.assertEqual(result, ["Hello", "World", "Testing"])
        print(f"String split test passed")
    
    def test_string_contains(self):
        """Test substring search"""
        text = "Jenkins automation testing"
        self.assertTrue("automation" in text)
        self.assertFalse("manual" in text)
        print("String contains test passed")
    
    def test_string_replace(self):
        """Test string replacement"""
        text = "Hello World"
        result = text.replace("World", "Jenkins")
        self.assertEqual(result, "Hello Jenkins")
        print(f"String replace test passed: '{text}' -> '{result}'")

if __name__ == '__main__':
    unittest.main()