# MANUAL TESTING
# This would be okay for very SIMPLE functions or if you can't get unittest to work.
# Requires more coding but you can more easily follow the testing process here. 

import functions as f 

# 1. Define tests
def test_calculate_total():
    """Checks that the total of 3 items is calculated correctly."""
    assert f.calculate_total(10, 20, 30) == 60  

# TODO: Create more tests here.     

# 2. Run tests
if __name__ == "__main__": 

    # Create a list of tests (functions) so it is easy to add more test functions later.
    # If you added more tests, you need to add them to this list. 
    tests = [
        test_calculate_total
        ]

    # Run all tests in your tests list.
    for test in tests:
        try:
            # Run the test and it should print PASSED.
            test()
            print(f"{test.__name__}: PASSED") 

        except AssertionError:
            # If the assert fails, it should show FAILED.
            print(f"{test.__name__}: FAILED")

        finally:
            # Indicate the test was run successfully. 
            print("Test completed.\n")