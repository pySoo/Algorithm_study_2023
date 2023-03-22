import math

def get_parking_time(time_list):
    start = list(map(int, time_list[0].split(':')))
    end = '23:59' if len(time_list) == 1 else time_list[1]
    end = list(map(int, end.split(':')))
    
    return (end[0] - start[0]) * 60 + end[1] - start[1]
    
def solution(fees, records):
    answer = []
    record_dict = {}
    min_time, min_pay, part_time, part_pay = fees
    
    for record in records:
        time, car_num, state = record.split(' ')
        if state == 'IN':
            if car_num not in record_dict:
                record_dict[car_num] = [[time]]
            else:
                record_dict[car_num].append([time])
        else:
            record_dict[car_num][-1].append(time)
    
    
    for key in sorted(record_dict):
        parking_time = 0
        for time_list in record_dict[key]:
            parking_time += get_parking_time(time_list)
        
        if parking_time <= min_time:
            pay = min_pay
        else:
            pay = min_pay + math.ceil((parking_time - min_time) / part_time) * part_pay
        
        answer.append(pay)
        
    return answer