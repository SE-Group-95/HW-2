"""
Module for generating random arrays.
"""

import secrets

def random_array(arr):
    """Fills an array with random integers between 1 and 20."""
    for index, _ in enumerate(arr):
        arr[index] = secrets.randbelow(20) + 1
    return arr
