def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = 0
        for s in skill_tree:
            if s in skill:
                if skill.index(s) > tmp:
                    break
                else:
                    tmp = skill.index(s) + 1
        else:
            answer += 1
    return answer