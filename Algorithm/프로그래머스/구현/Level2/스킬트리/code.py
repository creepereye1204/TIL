def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        a=''.join([skill_ for skill_ in skill_tree if skill_ in skill])
        if not a:
            answer+=1
        elif skill.find(a)!=-1 and a[0]==skill[0]:
            answer+=1
        
    return answer