import sys
from collections import deque
 
N = int(input())
x, y = map(int, sys.stdin.readline().split())
M = int(input())

# 주어진 부모 자식들 간의 관계의 개수를 dictinary 형태로 저장 
graph = dict() 
for i in range(1,N+1):
    graph[i] = list()
# 두 사람 간의 관계를 쌍방 관계로 저장     
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 촌수를 계산하기 위해서는 node의 level을 계산 
# level 계산을 위해서 bfs(같은 레벨의 노드 먼저 탐색) 활용 
def bfs(graph, start, end): # 촌수를 계산해야하는 노드를 각각 start, end로 
    visited = []
    queue = deque()
    queue.append(start)
    level = 0 
    while queue:
        size = len(queue)
        # 같은 레벨의 노드들 탐색을 반복문으로 구현 -> 탐색 완료시 깊이 +1 해서 레벨 구하기 
        for _ in range(size):
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                # 해당 노드와 연결된 노드들 추가 
                for i in graph[n]:
                    queue.append(i)
        # 촌수를 구하고자 하는 노드가 추가되면 break
        if end in visited:
            break
        level += 1
    # 촌수를 구하고자 하는 노드를 탐색하지 못하면 -1 return
    if end not in visited:
        return -1
    return level
print(bfs(graph, x, y))