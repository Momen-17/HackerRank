import re
import email.utils

for _ in range(int(input())):
    user_name, user_email = input().split()
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', user_email[1:-1]):
        print(user_name, user_email)
