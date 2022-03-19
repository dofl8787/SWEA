import sys
sys.stdin = open('5105.txt')
from collections import deque

dr = [0,0,1,-1] #우하좌상
dc = [1,-1,0,0]

T = int(input())

for tc in range(T):

    N = int(input())

    maze = [input() for _ in range(N)]

    #출발점, 도착점 찾기
    sr = sc = er = ec = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sr,sc = i,j #시작점
            if maze[i][j] == '3':
                er, ec = i,j #끝점


    # =====================================================
    # maze = []
    # sr = sc = er = ec = 0
    # for i in range(N):
    #     maze.append(list(map(int, input().split())))
    #     for j in range(N):
    #         if maze[i][j] == '2':
    #             sr,sc = i,j
    #         if maze[i][j] == '3':
    #             er, ec = i,j
    #

    visit = [[0] * N for _ in range(N)]
    Q = deque()
    #시작점을 방문표시하고 큐에 삽입
    visit[sr][sc] = 1
    Q.append((sr,sc))

    while Q: #빈 큐가 아닐 동안
        r, c = Q.popleft() #튜플형은 좌항이 r,c (두 개 이상)일 때, 언패킹해서 나타내줌
        #인접 정점을 찾는다.
        for i in range(4): #dr, dc 4방향 탐색
            nr = r + dr[i]
            nc = c + dc[i]
            #경계 체크
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            if maze[nr][nc] == '1' or visit[nr][nc]: continue

            visit[nr][nc] = visit[r][c] + 1
            Q.append((nr,nc))

    if visit[er][ec]:
        visit[er][ec] -= 2

    print(f'#{tc+1} {visit[er][ec]}')


# -----------------------
# while Q:
#     r,c = Q.popleft()
#     if r == er and c == ec:
#         break