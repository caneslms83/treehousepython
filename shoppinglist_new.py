shopping_list=[]

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to show the list.
""")
    

def add_to_list(item):
    shopping_list.append(item)
    print(f"{item} was added to the list. You now have {len(shopping_list)} items.")
    
#def a function named show_list that prints all the items of the list
def show_list():
    print("Your shopping list: ")
    for item in shopping_list:
        print(f"* {item} ")
    
show_help()


while True:
    new_item =input("> ")
               
    if new_item == 'DONE':
        break
        
    elif new_item == 'HELP':
        show_help()
              
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    #Enable the SHOW command to show the list. Don't forget to update the HELP documentation
    #Hint: make sure to run it.
    add_to_list(new_item)
    
show_list()
    