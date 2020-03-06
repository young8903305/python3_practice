class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        string1 = min(strs)
        string2 = max(strs)
        for index, char in enumerate(string1):
            if char != string2[index]:
                return string1[:index]
        return string1