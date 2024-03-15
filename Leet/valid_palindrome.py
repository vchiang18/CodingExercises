# https://leetcode.com/problems/valid-palindrome/

# solution 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        converted = ''.join(l for l in s if l.isalnum()).lower()
        last_index = len(converted)

        for i in range(len(converted)//2):
            if converted[i] != converted[last_index - 1 - i]:
                return False
        return True

#solution 2
class Solution(object):
    def isPalindrome(self, s):
        reversed = ""
        for l in s:
            if l.isalnum():
                reversed += l.lower()
        return reversed == reversed[::-1]

# solution w pointers (better memory)
class Solution(object):
    def isAlpaNum(self, c):
        return (ord('A') < ord(c) < ord('Z') or
                ord('a') < ord(c) < ord('z') or
                ord('0') < ord(c) < ord('9'))

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlpaNum(s[l]):
                l + 1
            while l < r and not self.isAlpaNum(s[r]):
                r - 1
            if s[l].lower != s[r].lower:
                return False
            l += 1
            r += 1

        return True




print(isPalindrome("race a car")) #returns False
print(isPalindrome("A man, a plan, a canal: Panama")) #returns True
