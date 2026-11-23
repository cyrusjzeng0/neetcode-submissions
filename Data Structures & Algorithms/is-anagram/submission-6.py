class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        letter_map = {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            letter_map[char_s] = letter_map.get(char_s, 0) + 1
            letter_map[char_t] = letter_map.get(char_t, 0) - 1

        for key in letter_map:
            if letter_map[key] != 0:
                return False
        
        return True