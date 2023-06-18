def print_rangoli(size):
    # Create the upper part of the pattern
    upper_part = []
    for i in range(size):
        if i == 0:
            pattern = chr(96 + size)
        elif i > 0:
            pattern = pattern[:(len(pattern) // 2) + 1] + "-" + chr(96 + size - i) + "-" + (pattern[:(len(pattern) // 2) + 1])[::-1]
        upper_part.append(pattern.center((size * 4) - 3, "-"))
    
    # Print the upper part of the pattern
    for pattern in upper_part:
        print(pattern)
    
    # Print the lower part of the pattern
    lower_part = upper_part[:-1][::-1]
    for pattern in lower_part:
        print(pattern)
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)