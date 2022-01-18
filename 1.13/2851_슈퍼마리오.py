import sys 

mushroom = []
for i in range(10):
    N = int(sys.stdin.readline())
    mushroom.append(N)

    num_sum = 0 #리스트에 있는 숫자 하나씩 더해줄 변수 
    for num in mushroom:
        num_sum += num
        # 100넘은 합 <= 100 넘기 직전까지 합 비교
        if num_sum >= 100:
            prev = num_sum -num 
            if num_sum-100 <= 100-prev: 
                return num_sum
            else:
                return prev
    return num_sum
print(mario())