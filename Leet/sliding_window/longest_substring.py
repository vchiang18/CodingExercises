# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# solution 1 - with set. O(n) time & memory.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        letterSet = set()
        l = 0
        output = 0

        for r in range(len(s)):
            while s[r] in letterSet:  #removes all letters from left up til duplicate at r pointer
                letterSet.remove(s[l])
                l += 1
            letterSet.add(s[r])
            output = max(output, len(letterSet))

        return output


# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
