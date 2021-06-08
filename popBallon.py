import sys
def solution(a):
    answer = 0
    start = a[0]
    for e in a:
        if e<=start:
            answer+=1
    return answer

numbers = list(map(int, sys.stdin.readline().strip().split()))
print(numbers)
print(solution(numbers))