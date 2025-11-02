# 1. return sorted(s) == sorted(t)   # little slower approach TC: O(n logn)

# 2. TC: O(n) 
# SC: O(1) since the size of the count dictionary will be at most 26 for lowercase letters

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         count = {}

#         for c in s:
#             count[c] = count.get(c, 0) + 1

#         for c in t:
#             if c not in t:
#                 return False
            
#             count[c] -= 1

#             if count[c] < 0:
#                 return False
        
#         return True


# TC: O(n) using collections.Counter
# SC: O(1) since the size of the counter will be at most 26 for lowercase letters
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
