# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3

def solution(arrangement):
    parsed = []
    indexes = []
    idx = 0
    
    for i, k in enumerate(arrangement[:-1]):
        if k == arrangement[i+1] and k == "(":
            parsed.append(idx)
            indexes.append(idx)
            idx += 1
            
        elif k == arrangement[i+1] and k == ")":
            parsed.append(indexes.pop(-1))
            
        elif k + arrangement[i+1] == "()":
            parsed.append("laser")
        else:
            continue
            
    answer = []        
    for i in range(idx):
        count = 0 
        for j in parsed[parsed.index(i)+1:]:
            if j == "laser":
                count +=1 
            elif j == i:
                break 
                
        answer.append(count+1)
        
    return sum(answer)

answer = solution("()(((()())(())()))(())")
print(answer)
