#Approach 1:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lim = len(nums)//2
        maj = {}
        for i in nums:
            if i not in maj:
                maj[i] = 1
            else:
                maj[i]+= 1
        for key, value in maj.items():
            if value > lim:
                return key

#Time Complexity: O(n)
#Space Complexity: O(n)

########################################################

#Approach 2:
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

#Time Complexity: O(nlogn)
#Space Complexity: O(1)

########################################################

#Approach 3:
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

#Time Complexity: O(n)
#Space Complexity: O(1)