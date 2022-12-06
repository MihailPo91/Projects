class Solution(object):
    def majorityElement(self, nums):
        uniques = {}
        for n in nums:
            if n in uniques:
                uniques[n] += 1
            else:
                uniques[n] = 1
        for n in uniques.keys():
            if uniques[n] > len(nums) / 2:
                return n


s = Solution()
print(s.majorityElement([3, 2, 3]))  # output: 3
