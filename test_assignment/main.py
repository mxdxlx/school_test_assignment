import argparse
from typing import List, Tuple, Union


def findSubarrayWithMaxSum(array: List[int]) -> Union[Tuple[int, int], Tuple]:
    """
    Finds start and end indexes of a subarray containing the maximum possible
    sum of elements in array of integers.

    :param list array: array of positive and negative integers
    :return: tuple of start and end indexes of subarray if given array is
    a non-empty array of integers, or an empty tuple otherwise
    """
    if not array:
        return ()

    if not all((isinstance(i, int) for i in array)):
        return ()

    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(len(array)):
        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return start, end


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('array', nargs='*', default='')
    args = parser.parse_args()

    # Joining in case of an occasional space
    args_array = ''.join(args.array).split(',')

    # Casting to ints
    try:
        args_array = [int(i) for i in args_array]
    except Exception:
        args_array = []

    print('Input:', args_array)
    print('Output:', findSubarrayWithMaxSum(args_array))
