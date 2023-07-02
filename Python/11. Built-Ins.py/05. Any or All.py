N = int(input())
numbers = input().split()
print(all(int(n) > 0 for n in numbers) and any(n == n[::-1] for n in numbers))