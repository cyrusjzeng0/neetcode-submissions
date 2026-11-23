class Solution:

    def encode(self, strs: List[str]) -> str: # O(n) time, O(n) space
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}#{word}") # tell decoder how many characters each string is
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        idx, decoded = 0, []
        while idx < len(s):
            length = ""
            while s[idx] != "#":
                length += s[idx]
                idx += 1
            length = int(length)
            idx += 1 # skip the '#' delimiter
            string = s[idx:idx+length] # catch the string
            idx += length # move idx forward
            decoded.append(string)
        
        return decoded