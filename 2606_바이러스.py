# dfs 알고리즘 사용 

import sys
 
N = int(input())
M = int(input())

graph = dict()
for i in range(1,N+1):
    graph[i] = list()

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(graph, start):
    visited = [] # 방문한 노드들 저장 리스트 
    route = [] #방문할 수 있는 루트들 저장 
    route.append(start) 
    while route: # 방문할 수 있는 루트가 남아있다면 
        v = route.pop() # 노드 pop -> 이미 방문한 노든지 확인 
        if v not in visited: # 방문하지 않았다면 visited에 추가하고 
            visited.append(v)
            for num in graph[v]: # 해당 노드와 연결 된 다른 노드들을 가능한 루트에 추가 
                route.append(num)
    return visited
print(len(dfs(graph,1))-1)