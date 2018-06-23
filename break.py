def loopy(items):
    for it in items:
        if it == 'stop':
            break
        else:
            print(it)
            
list =["apple", "red", "stop", "blue", "green"]

loopy(list)