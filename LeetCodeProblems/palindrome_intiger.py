class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        list_x = list(x)
        reversed_list_x = reversed(list_x)
        for m, n in zip(list_x, reversed_list_x):
            if m != n:
                return False
        return True


s = Solution()
print(s.isPalindrome(121321))
