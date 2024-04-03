# https://leetcode.com/problems/3sum/description/

# solution 1 - O(n^2), and sorting also O(nlogn), w space complexity dependent on algo (O(1) or n)
    def threeSum(self, nums):
        # sort array - allows us to skip duplicate triplet combos
        # enumerate for first loop
        # second loop with two pointer

        output = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i -1]:
                continue
            l, r = i + 1 , len(nums)-1
            while l < r:
                #sum is too big, decrement r
                if nums[l] + nums[r] + n > 0:
                    r -= 1
                #sum is too small, incremement l
                elif nums[l] + nums[r] + n < 0:
                    l += 1
                else:
                    output.append([n, nums[l], nums[r]])
                    l += 1
                    #r pointer automatically shifts in rest of code
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1

        return output

# solution 2 - brute force with triple loop, time complex O(n^3)
