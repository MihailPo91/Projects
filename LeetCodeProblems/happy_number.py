class Solution(object):

    def isHappy(self, n):
        s = str(n)
        n = 0
        counter = 0
        while True:
            for ch in s:
                n += int(ch) * int(ch)
            if n == 1:
                return True
            s = str(n)
            n = 0
            counter += 1
            if counter == 100:
                return False


s = Solution()
print(s.isHappy(7))
