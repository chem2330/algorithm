def solution(s):
    s = list(s.lower())
    if 'a' <= s[0] <= 'z':
        s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and 'a' <= s[i] <= 'z':
            s[i] = s[i].upper()
    # words = list(map(lambda x: x.lower(), s.split()))
    # for i, word in enumerate(words):
    #     if 'a' <= word[0] <= 'z':
    #         words[i] = word.replace(word[0], word[0].upper(), 1)
            
            
        
    # print(words)
    # words = list(map(lambda x: x.title(), s.split()))
    answer = ''.join(s)
    return answer