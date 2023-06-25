from collections import deque

d = deque()
for _ in range(int(input())):
    action, *number = input().split()
    exec(f"d.{action}({str(*number)})")

print(*d)