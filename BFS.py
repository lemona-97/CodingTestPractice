from collections import deque

def BFS(graph, start, visited):
    # 큐 구현을위한 덱 자료구조 사용
    queue = deque([start])

    visited[start] = True
    while queue:
        # 큐에서 하나 뽑기
        v = queue.popleft()
        # 큐에서 나올때 하나씩 출력
        print(v, end=" ")
        for i in graph[v]: # 뽑은 번호의 노드에 연결된 노드 목록을 순회하면서
            if not visited[i]: # 방문하지 않은곳이면?
                queue.append(i) # 큐에 순서대로 넣고
                visited[i] = True # 방문처리 함 (큐에 들어가는순간 방문처리)



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
BFS(graph, 1, visited)