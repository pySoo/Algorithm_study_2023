# dfs 풀이
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer


# bfs 풀이
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1 * numbers[0],0]]
    n = len(numbers)
    
    while queue:
        result, idx = queue.pop()
        idx += 1
        if idx == n:
            if result == target:
                answer += 1
        else:
            queue.append([result+numbers[idx], idx])
            queue.append([result-numbers[idx], idx])
    return answer