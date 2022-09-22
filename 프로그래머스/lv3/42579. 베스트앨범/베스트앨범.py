def solution(genres, plays):
    answer = []
    genre_dict = {}
    count_dict = {}
    for i in range(len(genres)):
        if genre_dict.get(genres[i]):
            genre_dict[genres[i]] += [[plays[i], i]]
            count_dict[genres[i]] += plays[i]
        else:
            genre_dict[genres[i]] = [[plays[i], i]]
            count_dict[genres[i]] = plays[i]
    genre_list = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    print(genre_list)
    for genre in genre_list:
        tmp = genre_dict[genre[0]]
        print(tmp)
        tmp.sort(key=lambda x:(-x[0], x[1]))
        for music in tmp[:2]:
            answer.append(music[1])
    
    return answer