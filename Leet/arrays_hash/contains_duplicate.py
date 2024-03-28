
# https://leetcode.com/problems/contains-duplicate/

# solution 1 - best time complexity w hash table. O(n). Space complexity: O(n).
class Solution(object):
    def containsDuplicate(self, nums):
        hashtable = {}

        for n in nums:
            if n in hashtable:
                return True
            hashtable[n] = 1
        return False

# solution 2 - sort and compare adj values. sorting time complexity: O(n logn)
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False



# Test cases
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
