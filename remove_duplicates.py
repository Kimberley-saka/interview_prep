"""
remove duplicates from sorted array
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    remove duplicate values
    """
    left_pointer = 1

    for right_pointer in range(1, len(nums)):
        if nums[right_pointer] != nums[right_pointer-1]:
            nums[left_pointer] = nums[right_pointer]
            left_pointer += 1
    return left_pointer


nums = [1, 1, 2, 2, 2, 2, 3, 3, 4]

print(remove_duplicates(nums=nums))
