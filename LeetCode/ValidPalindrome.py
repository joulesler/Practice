class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1
        while True:
            while (not s[start].isalnum()):
                start += 1
                if (end - start < 2 ):
                    return True

            while (not s[end].isalnum()):
                end -= 1
                if (end - start < 2 ):
                    return True
            # print(start, ":", s[start], end, ":", s[end])

            if s[start].lower() != s[end].lower():
                return False
            
            if (end - start < 2 ):
                return True
            else:
                start += 1
                end -= 1



tests = ["hiih", "hello", "s  s", "s   s", "s", "s s ", " s s", "s sh", " shs", "A man, a plan, a canal: Panama" ]
# tests = [ "0P" ]
# True, false, true, true, true, true, true, true, false, true, true

solution = Solution()
for i in range(len(tests)):
    print(solution.isPalindrome(tests[i]))
