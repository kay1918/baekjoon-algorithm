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
    
friend_list = [] # 친구 리스트 
result = [] # 친구 + 친구의 친구 리스트 

for i in graph[1]: 
    friend_list.append(i)

for i in friend_list: 
    result.append(i) # 친구 리스트에 있는 숫자들 result에 추가  
    for j in graph[i]: # 친구의 친구 리스트 중 
        if j !=1 : #본인 제외하고 추가 
            result.append(j)
print(len(set(result))) # 양방향 그래프라 중복 제거 