# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict


# solution 1 - best time complexity, O(m*n) - length of input array * length of each string.
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] += 1
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

#solution 2 - similar, but using sorted has O(n log n) time complex = O(N * m * log(m))
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_word = ''.join(sorted(s))
            anagram_map[sorted_word].append(s)

        return list(anagram_map.values())

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
