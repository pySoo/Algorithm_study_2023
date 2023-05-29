from collections import defaultdict

def solution(survey, choices):
    answer = ''
    character_type = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    character_score = defaultdict(int)
    
    for survey_type, choice in zip(survey, choices):
        type_a, type_b = survey_type[0], survey_type[1]
        if choice < 4:
            character_score[type_a] += 4 - choice
        elif choice > 4:
            character_score[type_b] += choice - 4
        
    for type_a, type_b in character_type:
        if character_score[type_a] >= character_score[type_b]:
            answer += type_a
        else:
            answer += type_b
    return answer