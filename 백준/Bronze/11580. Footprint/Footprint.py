import sys

input = sys.stdin.readline

test_count = int(input().strip())
steps = input().strip()

current_step = [0, 0]
before_step = set()  # set 사용으로 중복 좌표 제거

# 초기 위치 추가
before_step.add(tuple(current_step))

for i in steps:
    if i == "W":
        current_step[0] -= 1
    elif i == "E":
        current_step[0] += 1
    elif i == "S":
        current_step[1] -= 1
    elif i == "N":
        current_step[1] += 1
    
    # 현재 좌표를 set에 추가
    before_step.add(tuple(current_step))

print(len(before_step))
