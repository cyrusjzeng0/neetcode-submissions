class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        letter_map = {}

        for a, b in zip(s, t):
            letter_map[a] = letter_map.get(a, 0) + 1
            letter_map[b] = letter_map.get(b, 0) - 1

        return all(val == 0 for val in letter_map.values())