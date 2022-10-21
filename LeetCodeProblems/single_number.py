# Works but not very fast

# class Solution(object):
#     @staticmethod
#     def singleNumber(nums):
#         for n in range(len(nums)):
#             curr = nums.pop(n)
#             if curr in nums:
#                 nums.insert(n, curr)
#             else:
#                 return curr

# That is even slower SMH

# class Solution(object):
#     def singleNumber(self, nums):
#         for n in nums:
#             if nums.count(n) == 1:
#                 return n


# Fastest one, but using a set, not just editing the given list
class Solution(object):
    @staticmethod
    def singleNumber(nums):
        occurs = set()
        for n in nums:
            if n in occurs:
                occurs.remove(n)
            else:
                occurs.add(n)
        return list(occurs)[0]


s = Solution()
print(s.singleNumber([1, 1, 2, 2, 4, 4, 6, 5, 6, 5, 7, 3, 7, 5, 9, 9]))
