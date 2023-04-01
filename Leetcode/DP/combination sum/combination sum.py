class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                calc = i - num
                if calc >= 0:
                    dp[i] += dp[calc]
        return dp[target]