from unittest import TestCase

from .main import findSubarrayWithMaxSum


class FindSubarrayWithMaxSumTestCase(TestCase):

    def test_find_subarray_with_max_sum(self):
        self.assertTupleEqual(
            findSubarrayWithMaxSum([10, -3, -12, 8, 42, 1, -7, 0, 3]),
            (3, 5)
        )
        self.assertTupleEqual(findSubarrayWithMaxSum([]), ())
        self.assertTupleEqual(findSubarrayWithMaxSum([5]), (0, 0))
        self.assertTupleEqual(findSubarrayWithMaxSum([0, 0, 0, 0, 0]), (0, 0))
        self.assertTupleEqual(findSubarrayWithMaxSum(['asd', 'qwe']), ())
