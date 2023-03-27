## 238. Product of array except self

[문제 링크](https://leetcode.com/problems/product-of-array-except-self/description)

### 구분

Array, DP

### 풀이 요약

전체 곱에서 자기 자신을 나누는 방법을 쓰지 않고, 자신을 제외한 나머지 요소의 곱셈 결과를 출력해야 한다.

O(n)의 방법으로 풀어야 하기 때문에, DP의 방법인 누적 배열을 만들어서 해결한다. 누적 곱셈을 이용하여 자신을 제외한 왼쪽 곱 배열과 오른쪽 곱 배열을 저장해두고 서로 곱하면 된다.

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

이전 best time to buy and sell stock 문제에서 DP를 사용했었는데, 이번 문제로 DP 적용에 대한 감을 익힐 수 있었던 것 같다.이전 문제에서는 누적합을 통해 최대 이익을 구하는 것이었고 이번에는 누적합이라는 개념을 누적곱으로 치환하는 문제였다.

  <table>
  <thead><tr>
  <th>nums</th>
  <th>자신을 제외한 왼쪽 곱</th>
  <th>자신을 제외한 오른쪽 곱</th>
  <th>누적 곱</th>
  </tr>
  <tr>
  <th>[1,2,3,4]</th>
  <th>[1,1,2,6]</th>
  <th>[24,12,4,1]</th>
  <th>[24,12,8,6]</th>
  </tr>
  </thead>
  </table>

<br>

### 문제 설명

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

<h4>Example 1</h4>

> Input: nums = [1,2,3,4]
> Output: [24,12,8,6]

<h4>Example 2</h4>

> Input: nums = [-1,1,0,-3,3]
> Output: [0,0,9,0,0]

<h4>Constraints</h4>

- 1 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
