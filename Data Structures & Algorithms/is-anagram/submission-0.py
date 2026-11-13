class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        sArray = []
        tArray = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sArray.append(s[i])
            tArray.append(t[i])
        sArray.sort()
        tArray.sort()
        for i in range(len(s)):
            if sArray[i] != tArray[i]:
                return False
        return True
        