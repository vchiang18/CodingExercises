# https://leetcode.com/problems/product-of-array-except-self/description/

# solution 1 - O(n). multiply every before nums[i] with pre, and after
# nums[i] with post

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            answer[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= post
            post *= nums[j]

        return answer
