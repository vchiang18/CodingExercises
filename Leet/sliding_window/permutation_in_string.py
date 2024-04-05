# https://leetcode.com/problems/permutation-in-string/description/

# solution 1 - O(26)+ O(n) optimization. Can use either hashmaps or arrays.
    #loop through len(s1) and add to freq maps
    #initialize matches variable and loop through freq map fully (26 letters)
    #sliding window: l pointer after len(s1), r pointer loops through rest of s2
    #add and remove matches as window slides (check R added + and L letter removed)

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_map = [0] * 26
    s2_map = [0] * 26
    for i in range(len(s1)):
        s1_map[ord(s1[i])-ord('a')] += 1
        s2_map[ord(s2[i])-ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1_map[i] == s2_map[i]:
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2_map[index] += 1  #adds new letter to freq map

        if s1_map[index] == s2_map[index]:  #adjusts matches
            matches += 1
        elif s1_map[index] + 1 == s2_map[index]:  #only decrement matches if changed by 1 (allow for repeats)
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2_map[index] -= 1

        if s1_map[index] == s2_map[index]:
            matches +=1
        elif s1_map[index] - 1 == s2_map[index]:  #only decrement matches if changed by 1 (allow for repeats)
            matches -= 1
        l += 1

    return matches == 26


# solution 2 - hashmap, O(n*k), k as length of subarray.

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    freq_s1 = {}
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1

    k = len(s1)
    for i in range(len(s2) - k + 1):
        sub = s2[i:i+k]

        freq_sub = {}
        for char in sub:
            freq_sub[char] = freq_sub.get(char, 0) + 1

        if freq_s1 == freq_sub:
            return True

    return False









# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
