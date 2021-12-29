import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
total_box = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int,sys.stdin.readline().split())))
    total_box.append(box)


'''익은 토마토들에 대해서 우선적으로 주변탐색 -> 주변 토마토 익히기 해야하므로
큐 구현시 처음주어진 익은 토마토들을 우선 삽입
(특정 좌표만 넣는 경우 그 좌표에 대해서만 쭉 탐색해서 특정
좌표가 전체 상자를 익히는데 걸리는 시간이 구해짐) '''
def bfs(tomato_list): 
    level = 0 
    # 위층, 아래층, 왼, 오, 위, 아래 를 표시하기 위한 move 리스트 
    move_x = [0, 0, -1, 1, 0, 0]
    move_y = [0, 0, 0, 0, 1, -1]
    move_z = [1, -1, 0, 0 , 0, 0]
    q = tomato_list
    # q에는 익은 토마토의 좌표값[z,y,x]들을 리스트 append
    # while q -> 더 이상 상하좌우에 0이 없는 경우 반복문 끝 
    while q:
        # q의 사이즈 =  같은 날? 익혀져 있는 토마토들의 수
        size = len(q)
        for _ in range(size):
            start = q.popleft()
                #start 위치에서 위층아래층 상하좌우 제자리 좌표를 h,d,w 변수에 할당 
            for i in range(6):
                h = start[0] + move_z[i] 
                d = start[1] + move_y[i]
                w = start[2] + move_x[i]
                    # H,N,M 사이 값이며 안익혀진 토마토일 때 
                if 0<=h< H and 0<=d<N and 0<=w<M and total_box[h][d][w] == 0 : 
                        # 방문한 토마토는 1로 바꿔 줘서 익은 토마토라고 표시해줌
                    total_box[h][d][w] = 1 
                        # 좌표 h,d,w를 queue에 추가해서 해당 좌표의 상하좌우 검사
                    q.append(list((h,d,w)))
        # 같은 날 익어진 토마토들 (size) 반목문 끝나면 +1 해서 걸리는 날 구하기 
        level +=1
    return level-1  # 마지막 영향받은 토마토 리스트 후에도 +1 이되어서 결과값은 -1 해주기


def tomato(): 
    #이미 익은 토마토들을 tomato_list에 좌표값 저장
    tomato_list = deque()
    for z in range(H): 
        for y in range(N):
            for x in range(M):
                if total_box[z][y][x] == 1:
                    tomato_list.append(list((z,y,x))) 
                    
    days = bfs(tomato_list)
    #0 이 하나라도 있으면 -> 안익은 토마토가 있으면 -1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if total_box[z][y][x] == 0: 
                    return -1 
                # else문을 쓰면 0이 아닌 경우 바로 days값을 return하므로 틀렸음
    return days
print(tomato())

