import os

shopping_list = []

def clear_screen():
    os.system("Cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("What do you need from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
ENTER 'REMOVE' to remove item from your list.
""")
    
def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input(f"Where should I add {item}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ")
    else:
        position = 0
        
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
    show_list()

def show_list():
    clear_screen()
    print("Here's your list:")
    
    index = 1

    for item in shopping_list:
        print(f"{index}. {item}")
        index += 1
              
    print("-"*10)
        
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove? \n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()

while True:
    new_item = input("> ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT' or new_item.upper() == 'EXIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
        continue
    else:
        add_to_list(new_item)
              
show_list()
