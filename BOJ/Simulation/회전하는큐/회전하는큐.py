from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
targets = list(map(int, input().split()))
temp = list()
for i in range(1, n+1):
    temp.append(i)
queue = deque(temp)

def moveLeft(queue : deque):
    queue.append(queue.popleft())
    return queue

def moveRight(queue : deque):
    queue.appendleft(queue.pop())
    return queue

count = 0

for i in range(m):
    target = targets[i]
    left_move_count = queue.index(target)
    right_move_count = len(queue) - queue.index(target)
    while target != queue[0]:
        if left_move_count < right_move_count:
            for _ in range(left_move_count):
                queue = moveLeft(queue)
                count += 1
        else:
            for _ in range(right_move_count):
                queue = moveRight(queue)
                count += 1
    queue.popleft()

print(count)