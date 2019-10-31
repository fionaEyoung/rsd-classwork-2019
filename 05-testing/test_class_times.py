from times import *

def test_given_input():
    # Create two datetime ranges
    large = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    short = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    # Compute overlap
    result = overlap_time(large,short) 
    # result should be the same as short
    expected = short
    assert result == expected
