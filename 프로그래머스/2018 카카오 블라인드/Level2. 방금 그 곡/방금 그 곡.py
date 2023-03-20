def replace_sharp(music):
    music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return music
    
def get_diff_time(start, end):
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))
    
    return (end_hour - start_hour) * 60 + end_min - start_min
    
def solution(m, musicinfos):
    answer = []
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        play_time = get_diff_time(start, end)
        
        music = replace_sharp(music)
        music_time = len(music)
        
        play_music = music * (play_time // music_time) + music[:play_time % music_time]
        
        if replace_sharp(m) in play_music:
            answer.append([play_time, title])

    if len(answer) == 0:
        return "(None)"
    
    else:
        answer = sorted(answer, key = lambda x: (-x[0]))
        return answer[0][1]