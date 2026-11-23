class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list) # if non-existent key is accessed, a new empty list is assigned to that key 
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord("a")] += 1
            map[tuple(arr)].append(string)
        return list(map.values())