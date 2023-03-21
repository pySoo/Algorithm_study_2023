import math

def convert_number(n, k):
    s = ''
    while n > k-1:
        s += str(n % k)
        n //= k
    s += str(n)
    return s[::-1]

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
    

def solution(n, k):
    answer = 0
    split_list = convert_number(n,k).split('0')
    for number in split_list:
        if number.isnumeric() and is_prime(int(number)):
            answer += 1
    return answer