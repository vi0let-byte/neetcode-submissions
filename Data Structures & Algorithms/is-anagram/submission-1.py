class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        for c, count in sDict.items():
            if count != tDict.get(c, 0):
                return False
        return True
        