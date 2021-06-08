import sys

def solution(arr):
    answer = []
    def quad(x, y, n):
        target = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != target:
                    quad(x, y, n//2)
                    quad(x+n//2, y, n//2)
                    quad(x, y+n//2, n//2)
                    quad(x+n//2, y+n//2, n//2)
                    return
        answer.append(target)

    quad(0, 0, len(arr))
    return [answer.count(0), answer.count(1)]


n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solution(arr))