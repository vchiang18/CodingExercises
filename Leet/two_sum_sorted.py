# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# solution 1 - pointers, O(n)
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return [l+1, r+1]

# solution 2 - dictionary
    def twoSum(self, numbers, target):
        hashtable = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hashtable:
                return[hashtable[diff]+1, i+1]
            hashtable[n] = i

#solution 3 - binary search, O(log n)
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i, len(numbers)-1
            diff = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == diff:
                    return [i+1, mid+1]
                elif numbers[mid] < diff:
                    l = mid+1
                else:
                    r = mid-1

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
