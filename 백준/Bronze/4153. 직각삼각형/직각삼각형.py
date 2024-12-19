import sys

input = sys.stdin.readline

while(True):
    a,b,c = map(int, input().split())
    sort = sorted([a,b,c])
    
    if(a == 0 and b == 0 and c == 0) :
        break

    if(sort[2]**2 == sort[0]**2 + sort[1]**2):
        print("right")

    else:
        print("wrong")
        