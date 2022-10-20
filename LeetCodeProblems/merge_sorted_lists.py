class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged = []
        for i in list1:
            merged.append(i)
        for i in list2:
            merged.append(i)
        sorted_merged = sorted(merged)

        return sorted_merged


s = Solution()
print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))
