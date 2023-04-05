from collections import defaultdict
def solution(tickets):
    path = []
    graph = defaultdict(list)
    
    for (start, end) in tickets:
        graph[start].append(end)

    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    stack = ["ICN"]
    
    while stack:
        x = stack.pop()
        if x not in graph or not graph[x]:
            path.append(x)
        else:
            stack.append(x)
            stack.append(graph[x].pop())

    return path[::-1]