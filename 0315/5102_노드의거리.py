import sys
sys.stdin = open('5102.txt')
from collections import deque

T = int(input())

for tc in range(T):
    V,E = map(int, input().split())

    G = [[] for _ in range(V + 1)]


    for _ in range(E):
        u, v = map(int, input().split())
        #무향그래프이니까 서로 저장, 유향이라면 흐르는 곳만 체크하기
        G[u].append(v)
        G[v].append(u)

    # # 인접 리스트 확인하기
    # for i in range(1,v+1):
    #     print(i, '---->', G[i])

    s,g = map(int, input().split())

    def BFS(s,g):
        visit = [0] * (V+1)
        Q = deque()

        #출발점을 방문표시하고 큐에 삽입
        visit[s] = 1
        Q.append(s)

        # 빈 큐가 아닐 동안 반복
        while len(Q) > 0: # == while Q:
            v = Q.popleft() #큐에서 정점을 하나 꺼내온다.
            if v == g:
                return visit[v] - 1

            for w in G[v]: # 해당 v의 인접 정점을 찾는다.
                if not visit[w]: #방문하지 않았다면(0이라면)
                    visit[w] = visit[v] + 1 #방문표시와 거리계산을 둘 다 동시에 하고 있! 헷갈리지 말기
                    Q.append(w)
        return 0


    print(f'#{tc+1} {BFS(s,g)}')



