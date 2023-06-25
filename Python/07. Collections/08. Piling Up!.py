from collections import deque

for i in range(int(input())):
    size, block = int(input()), deque(map(int, input().split()))
    result = True
    
    for j in range(len(block) - 1):
        if block[0] >= block[1]:
            block.popleft()
        elif block[-1] >= block[-2]:
            block.pop()
        else:
            result = False
            break
    
    print("Yes" if result else "No")