import sys

input = sys.stdin.readline
test_count = int(input())

for _ in range(test_count):
    x,y = input().split()
    x = int(x,2)
    y = int(y,2)
    
    result = bin(x+y)
    print(result[2:])