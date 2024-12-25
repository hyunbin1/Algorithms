import sys, math
# 아이디어: DP라고 해서 모든 값을 다 계산에서 저장할 필요는 없다. 
# 이전에 계산된 값 중 전반적인 데이터의 합 등을 고려할 필요 없다면 dic으로 풀어보기 

input = sys.stdin.readline
N, P, Q = map(int, input().split())

dp = {0: 1}    

def calculate(n):
    if n in dp:
        return dp[n] # 만약 계산된 값이 있다면 이것 반납
    
    dp[n] = calculate(n//P) + calculate(n//Q)
    return dp[n]
print(calculate(N))
    
