# def is_palindromic_number(number):
#     number_str = str(number)
#     return number_str == number_str[::-1]

# N = int(input())
# print(any(is_palindromic_number(number) for number in list(map(int, input().split())) if number > 0))
N = int(input())
numbers = input().split()
print(all(int(n) > 0 for n in numbers) and any(n == n[::-1] for n in numbers))