candy = ["twix","caramel","snickers"]
soda = ["coca-cola", "sprite", "Dr. Pepper",]
chips = ["doritos", "fritos", "lays",]

while True:
    choice = input("Would you like SODA, CANDY, or CHIPS? ").lower()
    
    try:
        if choice == 'soda':
            snack = soda.pop()
        elif choice == 'candy':
            snack = candy.pop()
        elif choice == 'chips':
            snack = chips.pop()
        else:
            print("Sorry, I didn't get that.")
            continue
    except IndexError:
        print(f"Sorry we are all out of {choice}! Pick again.")
    print(f"Here's your {choice}: {snack}.")
    