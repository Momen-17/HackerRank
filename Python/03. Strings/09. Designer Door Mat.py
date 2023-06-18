# Enter your code here. Read input from STDIN. Print output to STDOUT
height, width = map(int, input().strip().split())

# Top part
for row in range(height // 2):
  pattern = ".|." * (row * 2 + 1)
  print(pattern.center(width, "-"))
  
# WELCOME message
print("WELCOME".center(width, "-"))

# Bottom par
for row in range((height // 2) - 1, -1, -1):
  pattern = ".|." * (row * 2 + 1)
  print(pattern.center(width, "-"))