# Task https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        prefix = []
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != current_char:
                    return ''.join(prefix)
            prefix.append(current_char)
        return ''.join(prefix)