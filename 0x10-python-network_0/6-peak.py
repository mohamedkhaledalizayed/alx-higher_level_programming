#!/usr/bin/python3

"""
This module contain one function
find_peak function
"""

def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid


    return list_of_integers[left] if list_of_integers else None
