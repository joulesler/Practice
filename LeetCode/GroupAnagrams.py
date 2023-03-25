import hashlib

class Solution:
    # Return List(List())
    def groupAnagrams(self, strs):
        dict = {}
        sortedWords = []
        for i in strs:
            sig = 0
            for letter in i:
                # hash = hashlib.sha256(letter.encode('utf-8'))
                # sig += int.from_bytes(hash.digest(), 'big')
                
                sig+=hash(letter)
            if dict.get(sig) == None:
                dict[sig] = [i]
                sortedWords.append(sig)
            else:
                dict[sig].append(i)
            # sortword = list(i[]).sort()
            # if dict.get(sortword) == None:
            #     dict[sortword] = [i]
            #     sortedWords.append(sortword)
            # else:
            #     dict[sortword].append(i)

        words = []
        for sortedWord in sortedWords:
            words.append(dict.get(sortedWord))

        return words

            
sol = Solution()

cases = [["eat","tea","tan","ate","nat","bat"]]

for i in cases:
    print(sol.groupAnagrams(i))