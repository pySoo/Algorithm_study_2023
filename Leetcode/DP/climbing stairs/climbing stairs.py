class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array = [0,1,2]

        if n < len(dp_array):
            return dp_array[n]

        for i in range(3, n+1):
            ith_way = dp_array[i-1] + dp_array[i-2]
            dp_array.append(ith_way)

        return dp_array[n]
