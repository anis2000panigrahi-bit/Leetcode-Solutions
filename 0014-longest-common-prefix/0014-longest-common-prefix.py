
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(len(prefix)):
            for s in strs:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]

        return prefix
