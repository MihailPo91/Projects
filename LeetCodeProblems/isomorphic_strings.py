class Solution(object):
    def isIsomorphic(self, s, t):
        data = {}
        if len(s) != len(t):
            return False
        for i1, i2 in zip(s, t):
            if i1 not in data:
                data[i1] = i2
            else:
                if data[i1] != i2:
                    return False
        data = {}
        for i1, i2 in zip(s, t):
            if i2 not in data:
                data[i2] = i1
            else:
                if data[i2] != i1:
                    return False
        return True


s = Solution()
print(s.isIsomorphic("dodo", "baba"))