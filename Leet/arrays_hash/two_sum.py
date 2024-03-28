# https://leetcode.com/problems/two-sum/description/


#solution 1 - better time complexity O(n), w hash table. Has retrieval is O(1)
class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {} #num : index
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[i] = n

#solution 2 - "brute force" by checking each sum combo
class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#solution 3
class Solution(object):
    def twoSum(self, nums, target):
        output = []

        for i in range(len(nums)):
            pointer = len(nums) - 1
            while pointer > i:
                if nums[i] + nums[pointer] == target:
                    output = [i, pointer]
                pointer -= 1

        return output


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
