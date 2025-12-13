#!/usr/bin/env python

from typing import TypeVar

# Define ElementType
T = TypeVar("T", bound=int)


# Element in arr should large than 0.
def count_sort(arr: list[T]) -> None:
    """Sort a list of numbers in ascending order(TBD).

    Stable.  Time Complexity: :math:`O(N+M)`.

    Auxiliary Space: :math:`O(N+M)`.
    """
    arr_range = max(arr) + 1
    cntarr = [0 for _ in range(arr_range)]

    for item in arr:
        cntarr[item] += 1

    for cnt_id in range(1, len(cntarr)):
        cntarr[cnt_id] += cntarr[cnt_id - 1]

    copy = arr.copy()
    for index in range(len(arr) - 1, -1, -1):
        item = copy[index]
        arr[cntarr[item] - 1] = copy[index]
        cntarr[copy[index]] -= 1


def main() -> None:
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    count_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
