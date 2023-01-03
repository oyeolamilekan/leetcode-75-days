from typing import List


def check_contains_duplicate_using_brute_force(nums: List[int]):
    for num1 in nums:
        index = nums.index(num1) 
        for num2 in nums[index + 1:]:
            if num1 == num2:
                return True
    return False

def check_contains_duplicate_using_sorting(nums: List[int]):
    nums.sort()
    for index, number in enumerate(nums):
        next_index = index + 1
        current_next_index = index+1 if next_index < len(nums) else None
        if not current_next_index:
            return False
        if number == nums[current_next_index]:
            return True
    return False

def check_contains_duplicate_using_set(nums: List[int]):
    number = set()
    for num in nums:
        if num in number:
            return True
        number.add(num)
    return False

print(check_contains_duplicate_using_set([1, 1, 5]))