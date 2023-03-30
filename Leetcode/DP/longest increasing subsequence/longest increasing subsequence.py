class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        answer = [1] * N
        
        for i in range(1, N):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, answer[j])
                    
            answer[i] = maxi + 1
        
        return max(answer)
