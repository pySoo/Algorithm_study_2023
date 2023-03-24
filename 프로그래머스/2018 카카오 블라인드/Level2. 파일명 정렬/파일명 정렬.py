"""
head 기준 정렬, 대소문자 구분 x
number 기준, 숫자 앞 0은 무시
주어진 순서 유지
"""

def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''

        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
            elif not number:  
                head += file[i]
            else:               
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(s) for s in answer]