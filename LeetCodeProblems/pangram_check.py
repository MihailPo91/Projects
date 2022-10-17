import string


class Solution(object):

    def checkIfPangram(self, sentence):
        is_pangram = True
        alphabet_dict = dict(zip(string.ascii_lowercase, [0]*26))
        for ch in sentence:
            if ch in alphabet_dict.keys():
                alphabet_dict[ch] += 1

        for key, value in alphabet_dict.items():
            if alphabet_dict[key] == 0:
                is_pangram = False
                break
        return is_pangram


test_string = "thequickbrownfoxjumpsoverthelazydog"
s = Solution()
print(s.checkIfPangram(test_string))