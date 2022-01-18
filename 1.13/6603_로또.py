import sys 
import itertools

# case 입력받기 
total = []
while True:
    case = sys.stdin.readline().split()
    K = int(case[0])
    case = case[1:]
    if K == 0: 
        break;
    total.append(case)
#combinations 사용해서 로또 값 출력    
for i in range(len(total)):
    lotto = list(itertools.combinations(total[i], 6))
    if i < len(total)-1:
        for num in lotto:
            print(' '.join(list(num)))
        print()
    else:
        for num in lotto:
            print(' '.join(list(num)))