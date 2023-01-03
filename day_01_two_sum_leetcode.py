"""
Problem Two Sum
"""

from time import time
from typing import List


def get_two_solution_using_hashmap_sum(values: List[int], target: int):
    """
    Implementing solution using hashmap
    """

    store = {}

    for index, value in enumerate(values):
        difference = target - value
        if difference in store:
            return [value, difference]
        store[value] = index
    return


def get_two_solution_using_bruteforce_sum(values: List[int], target: int):

    """
    Implement the solution using brute force
    """
    for first_value in values:
        for second_value in values:
            if (first_value + second_value) == target:
                return [second_value, first_value]
    return

start_time = time()

val = get_two_solution_using_hashmap_sum([1, 2, 3, 4, 10, 20, 55, 88, 92], 7)


total = (time() - start_time) * 1000



print(val, total)
# print(get_two_solution_using_bruteforce_sum([1, 2, 3, 4, 10, 20, 55, 88, 92], 7))