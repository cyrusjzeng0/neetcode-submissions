from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in strs:
            char_map = [0] * 26
            for letter in word:
                idx = ord(letter) - ord('a')
                char_map[idx] += 1
            word_map[tuple(char_map)].append(word)

        return list(word_map.values())