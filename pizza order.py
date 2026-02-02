print("Welcome to the world famous online pizza store")
print("Here is our menu")
print("For Small pizza charge is $15")
print("For Medium pizza charge is $20")
print("For Large pizza charge is $25")
pizza=int(input("Enter the pizza price: "))
print("Here are add on available for your pizza")
print("for pepperoni extra charge is $2 for small and $3 for medium/large pizza")
pepperoni=int(input("Enter the pepperoni price: "))
print("Do you like to have extra cheeze for price $1")
cheeze = input("Enter the cheeze price: ")
bill_small_pizza=15
bill_medium_pizza=20
bill_large_pizza=25
bill_small_pizza_with_pepperoni=15+2
bill_medium_pizza_with_pepperoni=20+3
bill_large_pizza_with_pepperoni=25+3
bill_small_pizza_with_cheeze=15+1
bill_medium_pizza_with_cheeze=20+1
bill_large_pizza_with_cheeze=25+1
bill_small_pizza_with_pepperoni_with_cheeze=15+2+1
bill_medium_pizza_with_pepperoni_with_cheeze=20+3+1
bill_large_pizza_with_pepperoni_with_cheeze=25+3+1
if pizza == 15:
    if pepperoni == 2 and cheeze==1:
        print(f"here is your small pizza with pepperoni and extra cheeze and bill is:${bill_small_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 2:
        print(f"here is your small pizza with pepperoni and bill is:${bill_small_pizza_with_pepperoni}")
    elif cheeze==1:
        print(f"here is your small pizza with extra cheeze and bill is:${bill_small_pizza_with_cheeze}")
    else:
        print(f"here is your small pizza and bill is:${bill_small_pizza}")
if pizza == 20:
    if pepperoni == 3 and cheeze==1:
        print(f"here is your medium pizza with pepperoni and extra cheeze and bill is:${bill_medium_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 3:
        print(f"here is your medium pizza with pepperoni and bill is:${bill_medium_pizza_with_pepperoni}")
    elif cheeze==1:
        print(f"here is your medium pizza with extra cheeze and bill is:${bill_medium_pizza_with_cheeze}")
    else:
        print(f"here is your medium pizza and bill is:${bill_medium_pizza}")
if pizza == 25:
    if pepperoni == 3 and cheeze==1:
        print(f"here is your large pizza with pepperoni and extra cheeze and bill is:${bill_large_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 3:
        print(f"here is your large pizza with pepperoni and bill is:${bill_large_pizza_with_pepperoni}")
    elif cheeze==1:
        print(f"here is your large pizza with extra cheeze and bill is:${bill_large_pizza_with_cheeze}")
    else:
        print(f"here is your large pizza and bill is:${bill_large_pizza}")

print("Hope you will visit again Have a nice day")
