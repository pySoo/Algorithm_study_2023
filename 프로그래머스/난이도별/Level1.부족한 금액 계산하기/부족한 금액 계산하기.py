def solution(price, money, count):
    pay = sum([price * i  for i in range(1, count+1)])
    
    if money > pay:
        return 0
    else:
        return pay - money
