class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total =sum (nums)
        
        right = total
        left=0
        
        for i in range (len(nums)):
            numb = nums[i]
            right -= numb
            if left == right:
                return i
            left += numb
        return -1
