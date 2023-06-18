if __name__ == '__main__':
    s = input()
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase_characters = False
    uppercase_characters = False
    for char in s:
      if char.isalnum():
        alphanumeric = True
      if char.isalpha():
        alphabetical = True
      if char.isdigit():
        digits = True
      if char.islower():
        lowercase_characters = True
      if char.isupper():
        uppercase_characters = True
    
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase_characters)
    print(uppercase_characters)
