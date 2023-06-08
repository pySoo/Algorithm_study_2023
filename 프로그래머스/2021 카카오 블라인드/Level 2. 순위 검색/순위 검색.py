from itertools import combinations
from collections import defaultdict


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        # 점수 앞에 있는 문자열
        key = info[:-1]
        # 점수
        val = int(info[-1])
        for i in range(5):
            # 하나의 info에서 경우의 수 16개 만들기 -> 항목이 4개이므로
            for combi in combinations(key, i):
                combi_key = ''.join(combi)
                info_dict[combi_key].append(val)

    for key in info_dict.keys():
        # lower bound 사용하기 위해 점수를 오름차순으로 정렬
        info_dict[key].sort()

    for query in queries:
        query = query.split()
        q_score = int(query[-1])
        query = query[:-1]

        # and와 -를 제거하고 하나의 문자열로 만듦 = backendjuniorpizza
        for i in range(3):
            query.remove('and')

        while '-' in query:
            query.remove('-')

        # 리스트를 문자열로
        q_key = ''.join(query)
        if q_key in info_dict:
            scores = info_dict[q_key]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - end)
        else:
            answer.append(0)
    return answer
