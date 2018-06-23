TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100  

#calcualte price function. takes number of tickets  and returns num tickets * TICKET_PRICE

def calculate_price(wanted_tickets):
    # create a new constant for the 2 dollar service charge and add to what is due
    return (wanted_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print (f"There are {tickets_remaining} tickets remaining.")
    
    name = input("What is your name?  ")
        
        
    wanted_tickets = input(f"How many tickets would you like {name}? ")
    #expect a value error and handle appropriately
    try:
        wanted_tickets = int(wanted_tickets)
        #raise an exception if request more than available tickets
        if wanted_tickets > tickets_remaining:
            raise ValueError(f"There are only {tickets_remaining}")
    except ValueError as err:
        #include the error in the text in the output
        print(f"Oh no, we ran into an issue. {err}. Please try again.")
    else:
        price = calculate_price(wanted_tickets)
        print(f"The total due is ${price}.")
        decision =  input("Would you like to purchase these tickets?  Y/N ")
        if decision.lower() == "y":
            #TODO proceed to gather cc info
            print(f"SOLD to {name}!!!")
            tickets_remaining -= wanted_tickets
        else:
            print(f"No worries, {name} maybe next time!")
print("Sorry, there are no more tickets!! :(")

