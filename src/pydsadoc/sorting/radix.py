#!/usr/bin/env python

from typing import TypeVar

# Define ElementType
T = TypeVar("T", bound=int)


def _count_sort(arr: list[T], digits: int) -> None:
    cntarr = [0] * 10

    for item in arr:
        item //= digits
        index = item % 10
        cntarr[index] += 1

    for cnt_id in range(1, len(cntarr)):
        cntarr[cnt_id] += cntarr[cnt_id - 1]

    copy = arr.copy()
    for index in range(len(arr) - 1, -1, -1):
        cnt_id = copy[index] // digits % 10
        arr[cntarr[cnt_id] - 1] = copy[index]
        cntarr[cnt_id] -= 1


def radix_sort(arr: list[T]) -> None:
    """Sort a list of numbers in ascending order(TBD).

    Stable.  Time Complexity: :math:`O(d * (n + b))`.

    Auxiliary Space: :math:`O(n + b)`.
    """
    max_item = max(arr)
    exp = 1
    while max_item // exp != 0:
        _count_sort(arr, exp)
        exp *= 10


def main() -> None:
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]
    print(arr)


if __name__ == "__main__":
    main()
