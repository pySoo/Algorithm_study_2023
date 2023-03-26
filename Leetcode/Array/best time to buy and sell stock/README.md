## 121. Best time to buy and sell stock

[문제 링크](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

### 구분

Array, DP, Kadane's Algorithm

### 풀이 요약

브루트 포스로 계산하면 이중 for문으로 인해 O(n^2)으로 시간 초과가 발생하기 때문에 O(n)의 방법으로 풀어야 하는 문제. DP 방법 중 하나이며 최대 부분합을 구하는 카데인 알고리즘을 이용한다.

"가장 저점에서 사서 가장 고점에서 판다"라는 것만 기억하면 된다. 인덱스를 우측으로 이동하면서 이전 상태의 가장 저점을 기준으로 이익을 계산하고, 이익이 클 경우 최댓값을 교체해나가는 방식이다.

### 나의 풀이

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
```

### 배운 점

단순 구현이 목적이 아닌 효율성을 고려한 풀이 방법에 대해 고민할 수 있었다. 효율성을 높이기 위해서는 적절한 알고리즘을 사용하는 것이 필요하다. 위 풀이에 적합한 개념은 Dynamic Programming(DP)이었다.

---

### Dynamic Programming(동적 계획법)

큰 문제를 작은 문제로 쪼개어 해결하고, 한 번 풀었던 문제는 저장해두었다가 같은 문제가 나왔을 경우 반복하여 풀지 않고 저장했던 것을 이용하여 계산하는 방법이다.

예시)

종이에 "1+1+1+1="을 쓰고 아이에게 답이 무엇이냐 묻는다.

아이: (숫자를 하나씩 센 후) 4!

문제의 왼쪽에 1+를 붙인 후, 아이에게 다시 답을 묻는다.

아이: (빠르게) 5!

어떻게 5인지 알았냐고 묻는다면 아이는 "그냥 1을 더했어요!"라고 말할 것이다.

왜냐면 4를 기억했다가 1을 더했을 뿐 1부터 5까지 다시 셀 필요가 없는 것이다!

> 다이나믹 프로그래밍을 한 마디로 정의하자면,<strong> "시간을 절약하기 위해 어떤 것을 기억하는 것"</strong> 이라고 말할 수 있다.

---

### Kadane’s Algorithm(카데인 알고리즘)

그렇다면 카데인 알고리즘이란 무엇이고, 위 풀이에서 왜 이 방법을 썼을까?

> 카데인 알고리즘이란 최대 부분 합을 O(n)의 시간복잡도로 구하는 알고리즘이다.

arr = [1,-6,4,7,3]의 배열이 있다.

i번째 인덱스를 마지막 값으로 하는 부분배열들의 최대 부분합을 M[i]라고 한다면, M[i+1]은 M[i]+arr[i+1] 또는 arr[i+1]중 더 큰 값이다.

- M[i+1] = max(M[i]+arr[i+1], arr[i+1])

  <table>
  <thead><tr>
  <th>i</th>
  <th>M[i-1]</th>
  <th>arr[i]</th>
  <th>비교</th>
  <th>M[i]</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>0</td>
  <td>-</td>
  <td>[1]</td>
  <td>-</td>
  <td>M[0] = [1]</td>
  </tr>
  <tr>
  <td>1</td>
  <td>M[0] = [1]</td>
  <td>[-6]</td>
  <td>max(M[0] + arr[1], arr[1]) </td>
  <td>M[0] + arr[1] = [1, -6]</td>
  </tr>
  <tr>
  <td>2</td>
  <td>M[1] = [1, -6]</td>
  <td>[4]</td>
  <td>max(M[1] + arr[2], arr[2]) </td>
  <td>arr[2] = [4]</td>
  </tr>
  </tbody>
  </table>

쉽게 생각하면, i번째 인덱스를 마지막 값으로 하는 부분배열에서 최대 부분합이 음수라면, 굳이 더하지 않고 i+1번째 인덱스부터 새로 시작하는게 이득이다.

이 개념을 문제에서 적용하려면 인덱스를 날짜로 치환하고, 최대 부분합을 최대 수익으로 치환하면 된다.

> 인덱스를 계속 증가시키면서 최대 부분합을 구하는 것이 곧 날짜를 이동시키면서 최대 이익을 계산하는 개념과 같다.

---

### 문제 설명

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

<h4>Example 1</h4>

> Input: prices = [7,1,5,3,6,4]
> Output: 5
> Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
> Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

<h4>Example 2</h4>

> Input: prices = [7,6,4,3,1]
> Output: 0
> Explanation: In this case, no transactions are done and the max profit = 0.

<h4>Constraints</h4>

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
