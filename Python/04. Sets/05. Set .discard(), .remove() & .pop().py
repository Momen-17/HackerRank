n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    action = input().split()
    
    if action[0] == "pop":
        s.pop()
    elif action[0] == "remove":
        s.remove(int(action[1]))
    elif action[0] == "discard":
        s.discard(int(action[1]))

print(sum(s))