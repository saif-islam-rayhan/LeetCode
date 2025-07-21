class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Loop through characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # If index i is out of range or characters don't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
