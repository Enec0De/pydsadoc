#!/usr/bin/env python

from typing import TypeVar, Any

from pydsadoc._abc_and_protocol import final_class_and_no_instance

T = TypeVar("T", bound=float)
_MINRUN: int = 32


@final_class_and_no_instance
class SortComponents:

    @staticmethod
    def calc_minrun(length: int) -> int:
        """Calculate the appropriate MINRUN for a given length.

        The parameter length is the length of the corresponding array.
        And the return value is the result MINRUN.

        The summary of the operation is as follows.  First, reduce the
        length of the array until it is less than _MINRUN.  Then, the
        remaining operation is similar to the ceil function in the math
        module.  For example, in binary, ceil(100.1) = 101.
        """
        remainder = 0
        while length >= _MINRUN:
            remainder |= length & 1
            length >>= 1
        return length + remainder

    @staticmethod
    def find_runs(array: list[T], start: int) -> int:
        """Calculate and return the end index of the run.

        The parameter start represents the start index of the run within
        the array.  If the run is in descending order, reverse it.
        """
        length = len(array)
        end = start + 1

        # Descending order.
        if end < length and array[start] > array[end]:
            end += 1
            while end < length and array[end - 1] > array[end]:
                end += 1
            
            # Reverse the run.
            array[start:end] = reversed(array[start:end])

        # Ascending order.
        elif end < length and array[start] <= array[end]:
            end += 1
            while end < length and array[end - 1] <= array[end]:
                end += 1

        return end


    @staticmethod
    def insertion(array: list[T], left: int, right: int) -> None:
        """"""
        for index in range(left + 1, right):
            temp = array[index]
            ptr = index - 1

            while left <= ptr and array[ptr] > temp:
                array[ptr + 1] = array[ptr]
                ptr -= 1
            array[ptr + 1] = temp


@final_class_and_no_instance
class MergeComponents:

    @staticmethod
    def merge(array: list[T], left: int, right: int, end: int, temp: list[Any]) -> None:
        temp_ptr = left_ptr = left
        right_ptr = right

        while left_ptr < right and right_ptr < end:
            if array[left_ptr] <= array[right_ptr]:
                temp[temp_ptr] = array[left_ptr]
                left_ptr += 1
            else:
                temp[temp_ptr] = array[right_ptr]
                right_ptr += 1
            temp_ptr += 1

        while left_ptr < right:
            temp[temp_ptr] = array[left_ptr]
            temp_ptr += 1
            left_ptr += 1

        while right_ptr < end:
            temp[temp_ptr] = array[right_ptr]
            right_ptr += 1
            temp_ptr += 1

        array[left:end] = temp[left:end]

    @staticmethod
    def merge_collapse(
        array: list[T], runs: list[tuple[int, int, int]], temp: list[Any]
    ) -> None:
        """Collapse the runs to obtain a favorable property.
        
        Suppose the last three runs in the stack are X, Y, Z from
        the top to the bottom respectively.  These three runs should
        satisfy the condition: len(Z) + len(Y) <= len(X), this ensures
        that the runs in the stack follow a sequence similar to the
        Fibonacci sequence, making the merge operation more efficient.
        """
        merge = MergeComponents.merge
        merge_runs = MergeComponents.merge_runs

        # The loop of maintaining the property of the runs.
        while (length := len(runs)) > 1:

            # Maintain the condition: Z + Y >= X.
            if (length > 3 and runs[-4][0] < runs[-3][0] + runs[-2][0]) or (
                length > 2 and runs[-3][0] < runs[-2][0] + runs[-1][0]
            ):
                # Get the merge point.
                if runs[-3][0] > runs[-1][0]:
                    merge_at = merge_runs(runs, -1)
                else:
                    merge_at = merge_runs(runs, -2)

                # Merge at the point merge_at.
                merge(array, *merge_at, temp)
                continue

            # Maintain the condition: Y >= Z.
            elif runs[-2][0] < runs[-1][0]:
                # Get the merge point.
                merge_at = merge_runs(runs, -1)

                # Merge at the point merge_at.
                merge(array, *merge_at, temp)
                continue

            # Meet all conditions and return.
            else:
                return

    @staticmethod
    def merge_runs(
        runs: list[tuple[int, int, int]], index: int = -1
    ) -> tuple[int, int, int]:
        """Merge the two runs and return a tuple.

        The parameter runs is a list of the runs.  The index points to
        the logical top element of the runs.  That is, if the index is
        -1 (the default), runs[-1] and runs[-2] will be merged; if the
        index is -2, runs[-2] and runs[-3] will be merged, while 
        runs[-1] remains unchanged.

        The return value is the tuple (left, right, end).  The merge
        function can use these values to merge the two runs within the
        given array.
        """
        len_a, left_a, right_a = runs.pop(index)
        len_b, left_b, _ = runs.pop(index)

        result = (len_a + len_b, left_b, right_a)
        runs.insert(index, result)
        return left_b, left_a, right_a

def insertion_sort(array: list[T]) -> None: ...


def merge_sort(array: list[T]) -> None: ...


def tim_sort(array: list[T]) -> None:
    length = len(array)
    temp = [None] * length
    MINRUN = SortComponents.calc_minrun(length)
    runs: list[tuple[int, int, int]] = []

    # The functions to be used.
    fund_runs = SortComponents.find_runs
    insertion = SortComponents.insertion
    merge = MergeComponents.merge
    merge_collapse = MergeComponents.merge_collapse
    merge_runs = MergeComponents.merge_runs

    # Calculate all the runs present within the array.
    run_start = run_end = 0
    while run_start < length:
        run_end = fund_runs(array, run_start)
        run_len = run_end - run_start

        # Handle the run whose length is less than MINRUN.
        if run_len < MINRUN:
            run_end = min(run_start + MINRUN, length)
            run_len = run_end - run_start
            insertion(array, run_start, run_end)

        # Append the tuple (length, start, end) of the run to the runs
        # stack.  Then, update run_start for the next loop. 
        runs.append((run_len, run_start, run_end))
        run_start = run_end

        # Collapse and optimize the runs stack.
        merge_collapse(array, runs, temp)

    # Merge all the runs in the runs stack.
    while len(runs) > 1:
        merge_at = merge_runs(runs)
        merge(array, *merge_at, temp)
