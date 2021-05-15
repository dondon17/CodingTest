import sys

def solution(n):
    answer = []
    temp = [[0]*n for _ in range(n)]

    direction = 1
    
    cnt = 1
    r, c = -1, 0
    
    for i in range(n):
        for j in range(i, n):
            # 방향은 3가지(down, right, up) 이므로 mod 3 연산 수행
            if i % 3 == 0:
                r += 1
            elif i % 3 == 1:
                c += 1
            elif i % 3 == 2:
                r -= 1
                c -= 1
            temp[r][c] = cnt
            cnt += 1


    '''    
    아래 코드로 작성 시, n=7일 때까지 정상 동작, 8이후로 시간 초과
    쓸데 없는 비교연산이 많이 수행됨
    
    while cnt <= n*(n+1)//2:
        
        if direction == 1:
            nr = r + 1
            if nr >= 0 and nr < n and temp[nr][c] == 0:
                r = nr
                temp[r][c] = cnt
            else:
                cnt -= 1 
                direction = 2

        elif direction == 2:
            nc = c + 1
            if nc >= 0 and nc < n and temp[r][nc] == 0:
                c = nc
                temp[r][c] = cnt
            else:
                cnt -= 1 
                direction = 3
        
        elif direction == 3:
            nc = c - 1
            nr = r - 1
            if nc < n and nr < n and nc >= 0 and nr >=0 and temp[nc][nr] == 0:
                r, c = nr, nc
                temp[r][c] = cnt
            else:
                cnt -=1 
                direction = 1

        cnt += 1
    '''

    for row in temp:
        print(row)
        for col in row:

            if col != 0:
                answer.append(col)
    return answer

n = int(sys.stdin.readline().strip())
print(solution(n))
