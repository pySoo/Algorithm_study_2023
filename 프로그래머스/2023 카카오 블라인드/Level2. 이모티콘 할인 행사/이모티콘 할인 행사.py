
from itertools import product

def solution(users, emoticons):
    answer = []
    discount_list = [40, 30, 20, 10]
    discount_product = list(product(discount_list, repeat = len(emoticons)))
    
    for discount_tuple in discount_product:
        total_buy = 0
        total_pay = 0
        for min_discount, max_pay in users:
            user_pay = 0
            for discount, emoticon_pay in zip(discount_tuple, emoticons):
                if discount >= min_discount:
                    user_pay += int(emoticon_pay * (100 - discount) * 0.01)
            if user_pay >= max_pay:
                total_buy += 1
            else:
                total_pay += user_pay
        answer.append([total_buy, total_pay])
    
    return sorted(answer, key = lambda x: (x[0], x[1]))[-1]
