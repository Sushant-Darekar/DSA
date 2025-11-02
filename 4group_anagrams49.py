# TC: O(n * k log k) where n is the number of strings and k is the maximum length of a string
# SC: O(n * k) for the output list and the hashmap
from typing import List
# class Solution:
#     def groupAnagrams(strs):
#         anagram_map = {}

#         for s in strs:
#             key = ''.join(sorted(s))  # sorted string used as dictionary key
#             if key not in anagram_map:
#                 anagram_map[key] = []
#             anagram_map[key].append(s)

#         return list(anagram_map.values())



# TC: O(n * k) where n is the number of strings and k is the maximum length of a string
# SC: O(n * k) for the output list and the hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        return list(hashmap.values())
        
        