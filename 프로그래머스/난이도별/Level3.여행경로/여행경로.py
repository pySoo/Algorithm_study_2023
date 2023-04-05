from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for (start, end) in tickets:
        graph[start].append(end)

    for airport in graph:
        graph[airport].sort(reverse=True)
    
    path = []
    stack = ["ICN"]
    while stack:
        route = stack[-1]
        if not graph[route]:
            path.append(stack.pop())
        else:
            next_route = graph[route].pop()
            stack.append(next_route)

    return path[::-1]