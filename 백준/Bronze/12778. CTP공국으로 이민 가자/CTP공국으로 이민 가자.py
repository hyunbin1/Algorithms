import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    test_count, types = input().split()
    data = list(input().split())
    
    if types == "C":  # 알파벳을 숫자로 변환
        for i in range(int(test_count)):
            data[i] = ord(data[i]) - 64     

    else:
        for i in range(int(test_count)):
            data[i] = chr(int(data[i]) + 64)     

    for i in range(len(data)):
        print(data[i], end = ' ')
    print()