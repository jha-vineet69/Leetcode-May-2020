class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while(low<high):
            mid = (low+high)//2
            isEven = (high -mid)%2==0
            if nums[mid]==nums[mid-1]:
                if(isEven):
                    high = mid-2
                else:
                    low = mid+1
            elif nums[mid]==nums[mid+1]:
                if(isEven):
                    low = mid+2
                else:
                    high = mid-1
            else:
                return nums[mid]
        return nums[low]
