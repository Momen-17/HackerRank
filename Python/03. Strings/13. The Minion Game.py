def minion_game(string):
    s = len(string)
    Kevin, Stuart = 0, 0
    
    for i in range(s):
      if string[i].upper() in "AEIOU":
        Kevin += (s - i)
      else:
        Stuart += (s - i)
    
    if Stuart > Kevin:
      print(f"Stuart {Stuart}")
    elif Stuart < Kevin:
      print(f"Kevin {Kevin}")
    else:
      print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)