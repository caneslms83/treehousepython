#add things to the list
shopping_list = []

#print out instructions
print("What do you need from the store?")
print("Enter 'DONE' to stop adding items.")

#ask for new items
while True:
    #ask for new items
    new_item = input("> ")
    #be able to quit the app
    if new_item == 'DONE':
        break

#add new items to our list
    shopping_list.append(new_item)

#print out the list
print("Here's your list:")

for item in shopping_list:
    print(item)

