import sys

# 수열 수식: an = (b-a) + b
# 공차: d = b-a
# 3 4

inputs = sys.stdin.readline
test_count = int(input())

stack_list = []
result = []
is_stack = True
current_number = 1

for _ in range(test_count):
    target_number = int(input())  # 4
    while target_number >= current_number:
        stack_list.append(current_number)
        result.append("+")
        current_number += 1 
    
    if stack_list[-1] == target_number:
        stack_list.pop()
        result.append("-")
    else:
        print("NO")
        is_stack = False
        break

if is_stack is True:
    for i in result:
        print(i)



