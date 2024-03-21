# https://leetcode.com/problems/top-k-frequent-elements/


# solution 1 - bucket sort, best time complexity, O(n + k)
# n is no of elements, and k to extract elements

class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        # loop and create hashmap
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        # loop and add hashmap values to freq
        for key, v in hashmap.items():
            freq[v].append(key)

        # loop over freq map backward
        output = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output


# solution 2 - O(nlogn) from sort
class Solution(object):
    def topKFrequent(self, nums, k):
        output = []
        nums_freq = {}

        for n in nums:
            nums_freq[n] = 1 + nums_freq.get(n, 0)

        nums_sorted = sorted(nums_freq.items(), key= lambda x:x[1], reverse=True)

        for key, _ in nums_sorted[:k]:
            output.append(key)

        return output

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
