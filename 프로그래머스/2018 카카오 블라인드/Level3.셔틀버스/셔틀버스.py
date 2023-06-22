from collections import defaultdict

def caculate_bus_time(index, t):
    time_int = 9 * 60 + index * t
    return convert_int_to_time(time_int)

def convert_time_to_int(time):
    hour, minute = list(map(int, time.split(':')))
    return hour * 60 + minute

def convert_int_to_time(time_int):
    hour, minute = divmod(time_int, 60)
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)

def is_before_time(prev, after):
    prev = convert_time_to_int(prev)
    after = convert_time_to_int(after)
    if after >= prev:
        return True
    else:
        return False

def solution(n, t, m, timetable):
    answer = ''
    bus_dict = defaultdict(list)
    timetable.sort()
    
    for index in range(n):
        bus_time = caculate_bus_time(index, t)
        bus_dict[bus_time] = []
        pop_index = -1
        for time_index,time in enumerate(timetable):
            if is_before_time(time, bus_time):
                if len(bus_dict[bus_time]) < m:
                    bus_dict[bus_time].append(time)
                    pop_index = time_index
        if pop_index > -1:
            timetable = timetable[pop_index+1:]
    
    bus_key = list(bus_dict.keys())
    if bus_key:
        final_bus = bus_dict[bus_key[-1]]
        if len(final_bus) == m:
            time_int = convert_time_to_int(final_bus[-1]) - 1
            return convert_int_to_time(time_int)
        else:
            return bus_key[-1]
    
    return answer