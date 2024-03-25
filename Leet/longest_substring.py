# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# solution 1 - with set. O(n) time & memory.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        letterSet = set()
        l = 0
        output = 0

        for r in range(len(s)):
            while s[r] in letterSet:
                letterSet.remove(s[l])
                l += 1
            letterSet.add(s[r])
            output = max(output, len(letterSet))

        return output
