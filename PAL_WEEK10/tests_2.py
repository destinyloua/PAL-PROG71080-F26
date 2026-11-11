# USING PYTHON TESTING FRAMEWORK (BETTER)
# Run 'pip install pytest' in terminal first if you don't have pytest yet 
# This way is more flexible and scaleable. 

import unittest
import functions as f

# 1. Define your test class. 
class TestFunctions(unittest.TestCase): 

    def test_calculate_total(self): 
        """Checks that the total of 3 items is calculated correctly."""
        # Arrange 
        a = 10
        b = 20 
        c = 30 
        expected = 60
        # Act 
        actual = f.calculate_total(a, b, c) 
        # Assert 
        self.assertEqual(actual, expected)

# TODO: Create more tests here.     

# Run the tests. 
if __name__ == "__main__": 
    unittest.main()
    # Look at the output in your terminal 