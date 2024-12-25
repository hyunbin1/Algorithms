import sys
# 아이디어: DP - 이전 비용까지를 합쳐서 저장후 그 최소 비용과 다음 집에 대한 비교를 진행한다. 
input = sys.stdin.readline
test_count = int(input()) 
rgb = [list(map(int, input().rstrip().split())) for _ in range(test_count)]
 
dp =  [[0]*3 for _ in range(test_count)]
dp[0] = rgb[0]

for i in range(1, test_count):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[-1]))
