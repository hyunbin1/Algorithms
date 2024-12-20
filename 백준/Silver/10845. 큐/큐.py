import sys

inputs = sys.stdin.readline
queue = []

def queue_push(x):
    queue.append(x)

def queue_size():
    print(len(queue))

def is_queue_empty():
    if len(queue) == 0:
        print(1) # 비어있는 경우
    else:
        print(0)

def queue_command(command, queue):
    if len(queue) == 0:
        print(-1)
    elif command[0] == "front":
        print(queue[0])
    elif command[0] == "back":
        print(queue[-1])
    elif command[0] == "pop":
        print(queue.pop(0))


test_case_count = int(input())

for _ in range (test_case_count):
    command = input().split()


    if len(command)==2:
        queue_push(command[-1])

    elif command[0] == "size":
        queue_size()
    
    elif command[0] == "empty":
        is_queue_empty()
    else:
        queue_command(command, queue)

        
    
    




    

