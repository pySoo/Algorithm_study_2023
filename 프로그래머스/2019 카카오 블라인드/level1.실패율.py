def solution(N, stages):
    people = len(stages)
    fail_dict = {}
    for i in range(1, N + 1):
        if people != 0:
            fail_dict[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            fail_dict[i] = 0

    return sorted(fail_dict, key=lambda i: fail_dict[i], reverse=True)
