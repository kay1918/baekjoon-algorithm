import sys

N = int(sys.stdin.readline())
time = []
pay= []
for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    time.append(T)
    pay.append(P)
result = [0 for _ in range(N+1)]
'''최대 금액을 구하는 것이므로 뒤 날짜부터 최대 값 채택
ex) 3일차 최대 금액은 앞 날짜 금액 or (3일차 금액) + (3일차+ 걸리는 상담기간 후 금액)'''
def counsel(day):
    if day + time[day-1] -1 <= N :
        result[day-1] = max(result[day], pay[day-1] + result[day-1 + time[day-1]])
    else:
        result[day-1] = result[day]
for day in range(N, 0,-1):
    counsel(day)
print(result[0])    