## 53. Maximum Subarray

[문제 링크](https://leetcode.com/problems/maximum-subarray)

### 구분

Array, DP

### 풀이 요약

가장 큰 부분합을 구하는 DP 문제. DP 개념을 이용하여 이전 배열까지의 최대합을 저장하고 현재 값과 비교하여 최대 값을 갱신해나가면 된다.

> dp[i] = max(dp[i-1]+nums[i], nums[i])

### 나의 풀이

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1

        for i in range(len(nums)):
            answer.append(product)
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer
```

### 배운 점

누적합을 이용하여 최대 누적합을 구하는 전형적인 DP 문제였다. DP 문제 유형을 파악하고 적용하는 법에 익숙해진 것 같다.

### 문제 설명

Given an integer array nums, find the subarray with the largest sum, and return its sum.

<h4>Example 1</h4>

> Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
> Output: 6
> Explanation: The subarray [4,-1,2,1] has the largest sum 6.

<h4>Example 2</h4>

> Input: nums = [1]
> Output: 1
> Explanation: The subarray [1] has the largest sum 1.

<h4>Constraints</h4>

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
