class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        for i,j in enumerate(nums):
            if target == j:
                answer.append(i)
        return answer
