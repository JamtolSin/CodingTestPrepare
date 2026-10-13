def solution(my_string, n):
    answer = ''

    for m_str in my_string:
        multi_str = m_str * n
        answer += multi_str

    return answer
