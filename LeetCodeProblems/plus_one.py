class Solution(object):
    def plusOne(self, digits):
        number = int(''.join(str(x) for x in digits))
        number += 1
        number = [int(x) for x in str(number)]
        return number


s = Solution()
print(s.plusOne([1,2,3]))
