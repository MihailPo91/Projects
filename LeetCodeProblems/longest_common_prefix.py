from collections import deque


class Solution:

    def longestCommonPrefix(self, strs):
        prefix = ''
        min_len_word = len(min(strs))
        for i in range(min_len_word):
            if all(x[i] == strs[0][i] for x in strs):
                prefix += strs[0][i]
            else:
                break
        return prefix


s = Solution()
print(s.longestCommonPrefix(['ab', 'a']))
