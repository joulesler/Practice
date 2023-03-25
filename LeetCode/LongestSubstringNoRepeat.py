class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        length = 0
        max = 0

        # to deal with sequential repeating characters
        for i in range(len(s)):
            if record.get(s[i]) == None:
                length += 1
                record[s[i]] = i
            else: 
                # # Reset to 1 if the chars are neighbours
                # if s[i] == s[i-1]:
                #     length = 1
                #     record = {}
                #     record[s[i]] = i
                # else:
                #     record[s[i]] = i
                # # record.pop(s[i])
                newStart = record[s[i]]
                length = i - newStart
                record = {}
                for j in range(newStart, i):
                    record[s[j]] = j
                record[s[i]] = i
            if length > max:
                max = length
        return max
    
sol = Solution()

cases = ["abcabcbb", "bbbbb", "pwwkew", " r e r", "r  e", "eraaabcd"]
# cases = [" r e r"]
#Corner Cases:
# Sequential
# Blank Strings
# 3, 1, 3, 3 "e r", 2, 4

for i in cases:
    print(sol.lengthOfLongestSubstring(i))