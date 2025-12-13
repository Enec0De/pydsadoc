#!/usr/bin/env python

from typing import TypeVar

# Define ElementType
T = TypeVar("T", bound=float)


# Elements in arr should be a decimal that 0 < 1.
def bucket_sort(arr: list[T]) -> None:
    """Sort a list of numbers in ascending order.

    Worst Case Time Complexity: :math:`O(n^2)`.
    Best Case Time Complexity : :math:`O(n + k)`.

    Auxiliary Space: :math:`O(n+k)`.
    """
    length = len(arr)
    buckets = [[] for _ in range(length)]

    # Put array elements in different bucket.
    for item in arr:
        id = int(item * length)
        buckets[id].append(item)

    # Sort every bucket.
    for list in buckets:
        list.sort()

    # Concatente all buckets into arr.
    index = 0
    for bucket in buckets:
        for item in bucket:
            arr[index] = item
            index += 1


def main() -> None:
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    bucket_sort(arr)
    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]
    print(arr)

    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucket_sort(arr)
    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]
    print(arr)


if __name__ == "__main__":
    main()
