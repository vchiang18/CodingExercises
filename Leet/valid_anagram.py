# https://leetcode.com/problems/valid-anagram/description/

# solution 1: time complexity: O(s, t)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  #.get allows value to not exist and defaults value to 0
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True

# solution 2
    return Counter(s) == Counter(t)

# solution 3 - no extra memory needed
    return sorted(s) == sorted(t)


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
