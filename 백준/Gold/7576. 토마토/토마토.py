import sys 
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())
metrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

# 익은 토마토 큐에 초기화
for x in range(N):
    for y in range(M):
        if metrix[x][y] == 1:
            queue.append((x,y,0))

def bfs():
    direction = [(-1,0), (1,0), (0,1) ,(0,-1)]

    date_count = 0 
    while queue:

        # 익은 토마토를 기준으로 dfs 하기
        x, y, day = queue.popleft()
        date_count = max(date_count, day)

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N  and 0 <= ny < M and metrix[nx][ny] == 0: # 안익은거 찾기 
                metrix[nx][ny] = 1 # 익게 만들기
                queue.append((nx, ny, day+1))

    return date_count


max_day = bfs()

# 탐색 종료 후 익지 않은 토마토가 있는지 확인
for row in metrix:
    if 0 in row:
        max_day = -1  # 익지 않은 토마토가 있음

print(max_day)
    