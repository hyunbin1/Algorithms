import sys 


# 
# 입력: 
# 첫 줄 - 시험장 개수 N
# 두번째 줄- 응시자 수 Ai개
# 세번째 줄 - 총 감독 감시 가능 수 : B, 부 감독 감시가능 수 C
input = sys.stdin.readline

N = int(input())
A = list(map(int,sys.stdin.readline().split()))
B, C = map(int, input().split())

# 3. 3 - 1 2 3 - left_A 

supervisor_sum = 0

for i in range(N):
    left_A = A[i] - B
    supervisor_sum = supervisor_sum + 1
    if(left_A > 0):
        if(left_A % C == 0 ):
            sub_supervisor_count = left_A // C    
        else:
            sub_supervisor_count = left_A // C + 1
        supervisor_sum = supervisor_sum + sub_supervisor_count
    
print(supervisor_sum)

    
