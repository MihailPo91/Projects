'''
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
    return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
'''


class Solution(object):
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return i + 1


s = Solution
print(s.searchInsert(nums=[1, 3, 5, 6], target=5))  # output: 2

