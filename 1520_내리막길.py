import sys
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().split())

travel_map = []
for _ in range(M):
    travel_map.append(list(map(int, sys.stdin.readline().split())))

# 이미 방문한 경로를 표시하기 위한 리스트 (-1-> 미방문 0-> 방문 0이상 값-> 경로)
visited = [[-1 for _ in range(N)] for _ in range(M)]
     
def path(y, x):
    # 시작점에 도달하면 1가지 루트를 구한것이므로 1 return
    if (y,x) == (0,0):
        return 1 
    # 상, 하, 좌, 우를 표시하기 위한 move 리스트 
    move_x = [0, -1, 0, 1]
    move_y = [1, 0, -1, 0]
    
    # 방문(확인)은 했으나 아직 경로가 아닌 경우 0으로 채워줌 
    if visited[y][x] == -1 :
        visited[y][x] = 0
        #상, 하, 좌,우를 확인했을 때 이전 값보다 크면 
        for i in range(4):
            h = y + move_y[i]
            w = x + move_x[i]
            #상,하,좌, 우 좌표까지 갈 수 있는 경우의 수를 더해줌
            if 0<=h< M and 0 <= w < N and travel_map[h][w] > travel_map[y][x]:
                visited[y][x] += path(h,w)  
    return visited[y][x]
       
  
print(path(M-1, N-1))