import sys

def solution(s):
    answer = []
    tempStr = s
    removeCnt = 0
    convertCnt = 0

    while True:
        if tempStr == '1': break
        
        tempArr = []
        check = 0

        for ch in tempStr:
            if ch == '0': removeCnt += 1
            elif ch == '1': tempArr.append(ch)

        tempStr = "".join(tempArr)
        tempStr = str(bin(len(tempStr)))[2:]
        convertCnt += 1


    answer.append(convertCnt)
    answer.append(removeCnt)
    return answer

s = sys.stdin.readline().strip()
print(solution(s))