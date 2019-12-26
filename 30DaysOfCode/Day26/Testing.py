#Problem Statement Available at: https://www.hackerrank.com/challenges/30-testing/
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [1,3,5,6]

    @staticmethod
    def get_expected_result():
         return 0

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [1,1,3,4]

    @staticmethod
    def get_expected_result():
        return 0
