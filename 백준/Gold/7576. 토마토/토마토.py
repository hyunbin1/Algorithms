from collections import deque

def bfs_tomatoes(grid, n, m):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 익은 토마토의 위치를 큐에 추가
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # 익은 토마토
                queue.append((i, j, 0))  # (x, y, day)
    
    max_day = 0
    while queue:
        x, y, day = queue.popleft()
        max_day = max(max_day, day)  # 최대 날짜 업데이트

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 익게 만듦
                queue.append((nx, ny, day + 1))
    
    # 탐색 종료 후 익지 않은 토마토가 있는지 확인
    for row in grid:
        if 0 in row:
            return -1  # 익지 않은 토마토가 있음
    return max_day

# 입력 처리
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# BFS 실행
result = bfs_tomatoes(grid, n, m)
print(result)
