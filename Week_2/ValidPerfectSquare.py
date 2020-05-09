#Approach 1:
#Time Complexity- O(n) - Recruiter Bhaga dega turant
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i*i <=num:
            if i*i == num:
                return True
            else:
                i+=1
        


#Better Approach
#Time Complexity - O(log(n)) - Beta Salary kitna loge discuss kar lein?
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        low = 1
        high = num//2
        while low <= high:
            mid = low + (high-low)//2
            if mid*mid == num:
                return True
            elif mid*mid <num:
                low = mid+1
            else:
                high = mid-1
        return False
        