import sys


password = input("Please enter the super secret password: ")
attempt_count =1
while password != "opensesame":
    if attempt_count > 3:
        sys.exit("Too many invalid password attmepts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town!")