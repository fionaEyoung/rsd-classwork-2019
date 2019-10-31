from times import *

def test_given_input():
    large = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    short = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    result = overlap_time(large,short) 
    expected = short
    assert result == expected
