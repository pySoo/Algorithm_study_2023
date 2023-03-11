from collections import deque

def solution(cache_size, cities):
    answer = 0
    cache_list = deque()
    
    if cache_size == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache_list:
            answer += 1
            cache_list.remove(city)
        else:
            answer += 5
            if len(cache_list) == cache_size:
                cache_list.popleft()
        cache_list.append(city)
            
    return answer