import sys
from collections import deque

# 값 입력
M, N, K = map(int, sys.stdin.readline().split())


# 2차원 리스트를 생성해서 직사각형이 그려지는 영역들을 1 로 지정 , 그외 영역은 0
graph = [[0]*N for _ in range(M)]
    
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2):
        for y in range(M-y2,M-y1):
            graph[y][x] = 1


def bfs(y,x): 
    # 상, 하, 좌, 우를 표시하기 위한 move 리스트 
    move_x = [0, -1, 0, 1]
    move_y = [1, 0, -1, 0]
    visited = []
    q = deque()
    # queue에는 2차원 리스트의 좌표값 [y,x] append
    q.append(list((y,x)))
    visited.append((y,x))
    # while q -> (y,x)에서 시작해서 더 이상 상하좌우에 0이 없는 경우 반복문 끝 
    while q:
        start = q.popleft() 
        #start 위치에서 상하좌우 제자리 좌표를 h,w 변수에 할당 
        for i in range(4):
            h = start[0] + move_y[i]
            w = start[1] + move_x[i]
            # 방문하지 않았고, M, N 사이 값이며 이중 리스트 값이 0일때(직사각형 영역이 아닐때)
            if (h,w) not in visited and 0<=h<M and 0<=w<N and graph[h][w] == 0 : 
                visited.append((h,w))
                # 이미 방문한 영역은 1로 바꿔 줘서 for문 돌 때 다시 검사할 필요 없게 
                graph[h][w] = 1 
                # 직사각형 영역이 아닌 좌표  h,w를 queue에 추가해서 해당 좌표의 상하좌우 검사
                q.append(list((h,w)))
        
    return len(visited)
    

count = 0 # 분리되는 영역 변수
area = [] # 각 영역의 넓이 저장 리스트
for y in range(M):
    for x in range(N):
        if graph[y][x] == 0: # 직사각형에 포함되지 않은 좌표들에 대해서 함수 실행 
            area.append(bfs(y,x)) 
            #직사각형에 포함되지 않아도 이미 방문한 영역은 bfs함수에서 1로 바뀌므로 영역 구분 가능
            count += 1 
print(count)
area.sort()    
for i in area:
    print(i, end = ' ')
