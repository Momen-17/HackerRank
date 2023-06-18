def merge_the_tools(string, k):
    n = len(string)
    s = round(n / k)
    
    subsequences = []
    
    for i in range(s):
      sub_string = ""
      for c in string[i * k: (i + 1) * k]:
        if c not in sub_string:
          sub_string += c
      subsequences.append(sub_string)
    
    for subsequence in subsequences:
      print(subsequence)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)