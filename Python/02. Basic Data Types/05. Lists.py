if __name__ == '__main__':
    N = int(input())
    
    list = []
    for _ in range(N):
        user_input = input()
        inputs = user_input.split()
        
        if inputs[0] == "insert":
          position = int(inputs[1])
          value = int(inputs[2])
          list.insert(position, value)
        elif inputs[0] == "append":
          list.append(int(inputs[1]))
        elif inputs[0] == "remove":
          list.remove(int(inputs[1]))
        elif inputs[0] == "sort":
          list.sort()
        elif inputs[0] == "reverse":
          list.reverse()
        elif inputs[0] == "pop":
          list.pop()
        elif inputs[0] == "print":
          print(list)