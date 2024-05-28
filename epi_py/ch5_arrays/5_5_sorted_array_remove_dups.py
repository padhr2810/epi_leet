"""
TRICK:
EDGE CASE, IF EMPTY ARRAY, RETURN 0
2 POINTERS, 'write_index' AND 'i' BOTH INIT = 1
ONLY NEED TO RETURN 'write_index' BECAUSE IT'S THE INT OF UNIQUE VALUES.
AT EVERY INCREMENT OF 'i', CHECK IF 'write_index' += 1
COMPARISON IS BETWEEN [write_index-1] = [i] ... I.E. NEED TO COMPARE THE 2 DIFFERENT POINTERS ... THIS ALLOWS WIDENING OF THE GAP FOR COMPARISON.
"""

import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
