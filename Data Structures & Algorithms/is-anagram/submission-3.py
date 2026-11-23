class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_diff = {}

        for i in range(len(s)):
            count_diff[s[i]] = count_diff.get(s[i], 0) + 1
            count_diff[t[i]] = count_diff.get(t[i], 0) - 1

        for char in count_diff:
            if count_diff[char] != 0:
                return False

        return True