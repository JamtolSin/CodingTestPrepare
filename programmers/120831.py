def solution(n):
    # n을 반으로 나눈 값
    mid_n = n // 2
    
    answer = 0
    
    for i in range(1,mid_n+1):
        answer += (2 * i)
    
    return answer