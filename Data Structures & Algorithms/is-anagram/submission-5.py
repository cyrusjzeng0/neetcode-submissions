class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,
                  43,47,53,59,61,67,71,73,79,83,89,97,101]

        product_s = product_t = 1

        for c_s,c_t in zip(s,t):
            product_s *= primes[ord(c_s)-ord('a')]
            product_t *= primes[ord(c_t)-ord('a')]

        return product_s == product_t