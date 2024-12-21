# 유기농 배추 - bfs
import sys
from collections import deque
input = sys.stdin.readline



def bfs(x,y):
    queue = deque([(x,y)])
    ground[x][y] = 0 # 현재 위치 방문 처리

    while queue:
        currentX, currentY = queue.popleft()
        # 상, 하, 좌, 우 탐색
        for deltaX, deltaY in [(-1,0),(1,0),(0,-1),(0,1)]:
            nextX, nextY = currentX+deltaX, currentY+deltaY # 다음 좌표
            if 0<= nextX < N and 0 <= nextY < M and ground[nextX][nextY] == 1: # 경계를 벗어나지 않고 다음 좌표에 배추가 있을 경우
                queue.append((nextX,nextY))
                ground[nextX][nextY] = 0
    


T = int(input())
results = []

while(T>0):
    T -= 1
    M, N, K = map(int, input().split()) # 가로, 세로, 테스트케이스 개수
    ground = [[0 for _ in range(M)] for _ in range(N)]
    
    # 배추 위치
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1 # 첫번재 인덱스가 세로.

    count = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                bfs(i,j)
                count += 1
    
    results.append(count)

for result in results:
    print(result)



