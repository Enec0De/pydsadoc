#!/urs/bin/env python

from typing import TypeVar, Any
from pydsadoc.sorting._iscomparable import Comparable

# Define the element type of the list to be sorted
# and the minimum run length.
T = TypeVar("T", bound=Comparable)
_MINRUN: int = 32


# Calculate the suitable MINRUN for the arr.
# The function just like the math function ceil, for example:
# ceil(100.1) = 101 for binary.
def _calc_minrun(length: int) -> int:
    remainder = 0
    while length >= _MINRUN:
        remainder |= length & 1
        length >>= 1
    return length + remainder


# Calculate and return the end index of the run.
# If the run is Descending, reverse it.
# It makes the run ordered.
def _find_runs(arr: list[T], start: int) -> int:
    lenght = len(arr)
    end = start + 1

    # Check wether the arr is ascending or not.
    if end < lenght and arr[start] > arr[end]:
        # Descending
        while end < lenght and arr[end - 1] > arr[end]:
            end += 1
        arr[start:end] = reversed(arr[start:end])
    else:
        # Ascending.
        while end < lenght and arr[end - 1] <= arr[end]:
            end += 1

    # Go to the end of the run.
    return end


# The insertion sorting for the given segment.
def _insertion(arr: list[T], left: int, right: int) -> None:
    # Insert arr[index] to the ordered list arr[left : index].
    index = left + 1
    while index < right:

        # arr[ptr] point to the element before the arr[index].
        temp = arr[index]
        ptr = index - 1

        # Note: I always make mistake here.
        # Note: The variable temp should no be arr[index].
        while ptr >= left and arr[ptr] > temp:
            arr[ptr + 1] = arr[ptr]
            ptr -= 1
        arr[ptr + 1] = temp

        # Insertion of the next element.
        index += 1


# Merte the arr[left:mid] and arr[mid:right].
# Need a temp array to stores the elements of the array.
def _merge(arr: list[T], left: int, mid: int, right: int, temp: list[Any]):
    left_ptr = temp_ptr = left
    right_ptr = mid

    # Merge two array until one of them is empty.
    while left_ptr < mid and right_ptr < right:
        if arr[left_ptr] <= arr[right_ptr]:
            temp[temp_ptr] = arr[left_ptr]
            left_ptr += 1
        else:
            temp[temp_ptr] = arr[right_ptr]
            right_ptr += 1
        temp_ptr += 1

    # Process the rest of the array.
    while left_ptr < mid:
        temp[temp_ptr] = arr[left_ptr]
        temp_ptr += 1
        left_ptr += 1
    while right_ptr < right:
        temp[temp_ptr] = arr[right_ptr]
        temp_ptr += 1
        right_ptr += 1

    arr[left:right] = temp[left:right]


# Check the runs meet the conditions:
#     X > Y + Z and Y > Z
# This makes the stack increase with the speed of Fibonacci.
def _merge_collapse(arr: list[T], runs: list[tuple[int, ...]], temp: list[Any]) -> None:
    # The runs stores the tuple element comprised of:
    #     (run_length, run_left, run_right)
    # It means that runs[n][0] is the length of the run.

    # The top 4 runs runs[-4], runs[-3], runs[-2], runs[-1] represented
    # by W, X, Y, Z respectively.
    while len(runs) > 1:

        condition_1 = len(runs) > 2 and runs[-3][0] <= runs[-2][0] + runs[-1][0]
        condition_2 = len(runs) > 3 and runs[-4][0] <= runs[-3][0] + runs[-2][0]
        # Do not meet the condition: X > Y + Z,
        # or the condition: W > X + Y.
        if condition_1 or condition_2:
            _, mid_l, mid_r = runs[-2]

            # For the case that length of X < length of Z.
            if runs[-3][0] < runs[-1][0]:
                start = runs[-3][1]
                _merge(arr, start, mid_l, mid_r, temp)
                runs[-3:-1] = [(mid_r - start, start, mid_r)]
            # For the case that length of X >= length of Z.
            else:
                end = runs[-1][2]
                _merge(arr, mid_l, mid_r, end, temp)
                runs[-2:] = [(end - mid_l, mid_l, end)]

        # Do not meet the condition: Y > Z.
        elif runs[-2][0] <= runs[-1][0]:
            _, _, end= runs[-1]
            _, start, mid= runs[-2]
            _merge(arr, start, mid, end, temp)
            runs[-2:] = [(end - start, start, end)]

        # All conditions is checked ok.
        else:
            return


def tim_sort(arr: list[T]) -> None:
    """Sort a list of numbers in ascending order."""
    length = len(arr)
    MINRUN = _calc_minrun(length)
    temp = [None] * length
    runs = []

    # Calculate the runs and push them into the stack.
    run_start = run_end = 0
    while run_start < length:
        run_end = _find_runs(arr, run_start)
        run_len = run_end - run_start

        # Insertion sorting for the runs that shorter than MINRUN.
        if run_len < MINRUN:
            run_end = min(run_start + MINRUN, length)
            _insertion(arr, run_start, run_end)
        runs.append((run_end - run_start, run_start, run_end))
        run_start = run_end

        # Collapse and optimize the runs.
        _merge_collapse(arr, runs, temp)

    # The final merge of the sorting.
    while len(runs) > 1:
        _, left, _ = runs[-2]
        _, mid, right = runs[-1]
        _merge(arr, left, mid, right, temp)
        runs[-2:] = [(right - left, left, right)]
