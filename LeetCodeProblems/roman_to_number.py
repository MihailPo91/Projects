class Solution(object):

    def romanToInt(self, s):
        output = 0
        for n in range(len(s)):
            if s[n] == 'M':
                if n == len(s)-1:
                    if s[n - 1] == 'C':
                        output += 900
                        break
                    else:
                        output += 1000
                        break
                if n == 0:
                    output += 1000
                elif s[n-1] == 'C':
                    output += 900
                else:
                    output += 1000

            elif s[n] == 'D':
                if n == len(s)-1:
                    if s[n - 1] == 'C':
                        output += 400
                        break
                    else:
                        output += 500
                        break
                if n == 0:
                    output += 500
                elif s[n-1] == 'C':
                    output += 400
                else:
                    output += 500

            elif s[n] == 'C':
                if n == len(s)-1:
                    if s[n - 1] == 'X':
                        output += 90
                        break
                    else:
                        output += 100
                        break
                if s[n+1] in 'DM':
                    continue
                if n == 0:
                    output += 100
                elif s[n-1] == 'X':
                    output += 90

                else:
                    output += 100

            elif s[n] == 'L':
                if n == len(s)-1:
                    if s[n - 1] == 'X':
                        output += 40
                        break
                    else:
                        output += 50
                        break
                if n == 0:
                    output += 50
                elif s[n-1] == 'X':
                    output += 40
                else:
                    output += 50

            elif s[n] == 'X':
                if n == len(s)-1:
                    if s[n - 1] == 'I':
                        output += 9
                        break
                    else:
                        output += 10
                        break
                if s[n+1] in 'LC':
                    continue
                if n == 0:
                    output += 10

                elif s[n-1] == 'I':
                    output += 9

                else:
                    output += 10

            elif s[n] == 'V':
                if n == len(s)-1:
                    if s[n - 1] == 'I':
                        output += 4
                        break
                    else:
                        output += 5
                        break
                if n == 0:
                    output += 5
                elif s[n-1] == 'I':
                    output += 4
                else:
                    output += 5

            elif s[n] == 'I':
                if n == len(s)-1:
                    output += 1
                    break
                if s[n+1] in 'VX':
                    continue
                if n == 0:
                    output += 1
                else:
                    output +=1

        return output


solution = Solution()
s = 'MCMXCIV'
print(solution.romanToInt(s))