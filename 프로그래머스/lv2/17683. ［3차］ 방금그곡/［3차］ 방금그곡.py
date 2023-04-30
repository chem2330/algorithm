def solution(m, musicinfos):
    answer = ''
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for musicinfo in musicinfos:
        s, e, A, B = musicinfo.split(',')
        hh, mm = map(int, e.split(':'))
        time = hh * 60 + mm
        hh, mm = map(int, s.split(':'))
        time -= (hh * 60 + mm)
        B = B.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        music = (B * (time // len(B) + 1))[:time]
        if m in music:
            print(1)
            print(answer)
            if not answer or answer[0] < time or (answer[0] == time and answer[1] > s):
                answer = (time, s, A)
    if answer:
        return answer[2]
    return "(None)"