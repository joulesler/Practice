class Solution(object):
    # Memory Optimised
    def reverseWords(self, st):
        
        lastSpace = -1
        rStr = ""
        i = 0
        while i < len(st):
            if st[i] == ' ':
                j = i-1
                while j != lastSpace:
                    rStr += st[j]
                    j-=1
                rStr += " "
                lastSpace = i  
                
            elif i == len(st)-1:
                j = i
                while j != lastSpace:
                    rStr += st[j]
                    j-=1
            i+=1
        return rStr

    #Time Optimised
    def reversingWords(self, st):
        s = st.split(" ")
        rStr = []
        for i in s:
            rStr.append(i[::-1])
        return " ".join(rStr)