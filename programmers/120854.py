def solution(strlist):
    answer = []

    for str in strlist:
        # str -> "We"
        answer.append(len(str)) # len(str) -> str의 문자 개수

    return answer
