## 217. Contains Duplicate

[문제 링크](https://leetcode.com/problems/contains-duplicate)

### 구분

Array, Hash, Set

### 풀이 요약

Hash table에 각 원소를 저장하고 이미 저장된 원소가 다시 불리면 True를 반환하고, 끝까지 순회를 마쳤다면 중복되는 원소가 없기 때문에 False를 반환한다.

### 나의 풀이

```python
# Hash
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] = 1
        return False

# set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

### 배운 점

중복되는 원소를 구할 때 Hash를 이용하지 않고도 set 함수를 이용해서 풀이하는 법도 알게 되었다.

Hash와 set 풀이의 효율성 비교

Hash
Time Complexity: for loop을 1번 사용하므로 O(n)
Space Complexity: hash table에 저장하므로 최대 O(n)

Set
Time Complexity: set 만드는데 O(n)
Space Complexity: 추가 메모리 필요 없으므로 O(1)

### 문제 설명

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

<h4>Example 1</h4>

> Input: nums = [1,2,3,1]
> Output: true

<h4>Example 2</h4>

> Input: nums = [1,2,3,4]
> Output: false

<h4>Constraints</h4>

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
