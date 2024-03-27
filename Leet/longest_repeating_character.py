# https://leetcode.com/problems/longest-repeating-character-replacement/

# solution 1 - O(n *26) to scan for max in letter dict
class Solution(object):
    def characterReplacement(self, s, k):
        output = 0
        char_count = {}
        l = 0

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r],0)

            if (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1

            output = max(output, r-l+1 )

        return output

# solution 2 - O(n) optimization. Max freq doesn't need to be current to get correct output.
    def characterReplacement(self, s, k):
        output = 0
        char_count = {}
        l = 0
        max_freq = 0

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r],0)
            max_freq = max(max_freq, char_count[s[r]])

            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

            output = max(output, r-l+1 )

        return output

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too
