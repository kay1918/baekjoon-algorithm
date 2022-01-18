import sys 

N = int(sys.stdin.readline())

def findM(N):
    for num in range(1, N+1): # N 자체는 분해합이 될 수 있는  최대 숫자 
        M = num # M을 1~N+1중 하나씩 숫자 지정해서 찾기
        num = str(num)
        for n in num:
            M += int(n) # M = 해당 숫자 + 각 자리 수 합 
        if M == N : # M이 N과 같으면 분해합 
            return num
    return 0 # for문이 다 돌아도 분해합을 못찾으면 0 반환
print(findM(N))