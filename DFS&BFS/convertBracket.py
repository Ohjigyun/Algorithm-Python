def balanced_index(p):
    #왼쪽 괄호의 개수
    count = 0 
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return 1

#올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -=1
    return True #쌍이 맞으면 True

def solution(p):
    answer =''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index +1]
    v = p[index+1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        #첫 번째와 마지막 문자 제거
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer