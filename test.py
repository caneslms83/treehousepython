first_name = input("What is your first name? ")
print("Hello," , first_name)
if first_name == "Craig":
    print(first_name, "is learning python")
elif first_name == "Luis":
    print(first_name, "is learning with fellow students!")
else:
    #this is to test young users
    age = int(input("How old are you? " ))
    if age <= 6:
        print(f"Wow you're {age}! If you're confident with your reading already...")
    print(f"You should totally learn python, {first_name}!") 
    
print (f'Have a great day {first_name}!')
