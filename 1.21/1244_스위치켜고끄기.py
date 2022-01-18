import sys

N = int(sys.stdin.readline())
bulb = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
student_list = []
for _ in range(M):
    student = list(map(int, sys.stdin.readline().split()))
    student_list.append(student)
   
def switch(num):
    if num == 0:
        num = 1
    elif num ==1:
        num = 0
    return num
    
for student in student_list:
    if student[0] == 1: # 학생이 남자면
        multiple = N // student[1] #배수가 몇개 인지 찾기
        for n in range(1, multiple+1):
            # n을 곱하여 얻은 배수는 0,1switch해주기 
            bulb[(n*student[1])-1] = switch(bulb[(n*student[1])-1]) 
    elif student[0] == 2: # 학생이 여자이면 
        center = student[1]-1 #학생이 받은 숫자를 중심으로 대칭찾기 
        bulb[center] = switch(bulb[center]) # 학생이 받은 숫자도 switch
        i = 1
        while True:
            #학생이 받은 숫자중심으로 좌우 대칭일 경우 switch
            #반목문을 통해 최대 대칭 거리까지 찾기
            if center-i>=0 and center+i <= N-1 and (bulb[center-i] == bulb[center+i]): 
                bulb[center-i] = switch(bulb[center-i])
                bulb[center+i]= switch(bulb[center+i])
                i+=1 
            else: 
                break
        
for i in range(0, len(bulb), 20):
    print(*bulb[i:i+20])