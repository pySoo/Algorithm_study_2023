def convert_date_to_int(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        term_type, month = term.split()
        term_dict[term_type] = int(month) * 28
    
    for i in range(len(privacies)):
        date, term_type = privacies[i].split()
        due_date = convert_date_to_int(date) + term_dict[term_type]
        if due_date <= convert_date_to_int(today):
            answer.append(i+1)
        
    return answer