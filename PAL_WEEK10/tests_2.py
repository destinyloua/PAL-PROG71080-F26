# USING PYTHON TESTING FRAMEWORK (BETTER)
# Run 'pip install pytest' in terminal first if you don't have pytest yet 
# This way is more flexible and scaleable. 

import unittest
import functions as f

# 1. Define your test class. 
class TestFunctions(unittest.TestCase): 

    def test_calculate_total(self): 
        """Checks that the total of 3 items is calculated correctly."""
        self.assertEqual(f.calculate_total(10, 20, 30), 60)

# TODO: Create more tests here.     

# Run the tests. 
if __name__ == "__main__": 
    unittest.main()
    # Look at the output in your terminal 