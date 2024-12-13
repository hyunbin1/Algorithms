import sys

# 
# 입력: 
# 첫 줄 - 테스트 케이스 T개
# 다음 줄 - 각각의 테스트 케이스 정수 a, b (1<=a<100, 1<= b < 1,000,000)
input = sys.stdin.readline
T = int(input())
all_nodes = 10

# 원래라면 a**b % 10 하면 되는데, 이건 시간에서 문제일듯
# 1,         1,1,1,1,1,
# 2,4,8,6,   2,4,8,6,
# 3,9,7,1,   3,9,7,1,3
# 4, 6,      4,6,4,6, 4,6
# 5,         5,5,5,5
# 6,         6,6,6,6,
# 7,9,3,1,   7,9,3,1
# 8,4,2,6,   8
# 9,1,       9,1
# 0
# 풀이: 노드의 개수가 10개이기 때문에 어차피 일의 자리 수만 알면 된다. 
# 
for i in range(T):
    a, b = map(int, input().split())
    units = a % 10 # units = 일의 자리 

    if(units == 0): # 패턴 1: 노드가 10일 경우 = 가지고 있는 노드 다 사용
        print(all_nodes)

    elif(units == 0 or units == 1 or units == 5 or units == 6): # 패턴 2: 제곱해도 자기자신
        print(units)

    elif(units == 4 or units == 9): # 패턴 3: 제곱 패턴이 2개씩 반복됨
        cycle_per_2 = (b % 2)
        
        if(cycle_per_2 == 0):
            result = (a**2) % 10
        else: 
            result = (units ** cycle_per_2) % 10
        print(result)
        
    elif(units == 2 or units == 3 or units == 7 or units == 8): # 패턴 4: 제곱 패턴이 4개씩 반복 됨 1 2 3 0 1 2 3 0 
        cycle_per_4 = (b%4)
        if(cycle_per_4 == 0):
            result = (a**4) % 10
        else:
            result = (units ** cycle_per_4) % 10
        print(result)













