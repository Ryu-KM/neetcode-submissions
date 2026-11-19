class Solution:
    def isAnagram(self, s: str, t: str) -> str:
        
        if len(s) != len(t):
            return False

        countS,countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        print(countS)
        for count in countS:
            if countS[count] != countT.get(count,0):
                return False
        return True