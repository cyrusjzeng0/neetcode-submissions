class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        for char in t:
            if char in map:
                if map[char] == 1:
                    map.pop(char, None)
                else:
                    map[char] -= 1
            else:
                return False
        return not map