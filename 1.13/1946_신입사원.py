import sys 
test_case = []

#입력받기 
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    score_list= []
    for n in range(N):
        a,b = map(int,sys.stdin.readline().split())
        score_list.append((a,b))
    test_case.append(score_list)
#입력받은 리스트 정렬 -> 점수 (a,b)중 a기준 정렬
for case in test_case:
    case.sort(key=lambda x : x[0])


total = []

for case in test_case:
    #각 테스트 케이스 중 첫번째(a점수가 가장작은 점수튜플)를 기준으로 
    employees = []
    employees.append(case[0])
    base = case[0]
    for i in range(len(case)):
        #a는 이미 정렬되어있으니(오름차순) b가 기준점수보다 작은 경우 리스트에 삽입
        #뒤 점수들은 새롭게 추가된 점수랑 비교해야하므로 추가된 점수를 기준점수로 변경
        if case[i][1] < base[1] :
            base = case[i]
            employees.append(base)
    total.append(employees)
for scores in total:
    print(len(scores))