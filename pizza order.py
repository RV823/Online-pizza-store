import random

print("Welcome to the world famous online pizza store")
print("Here is our menu")
print("For Small pizza charge is $15")
print("For Medium pizza charge is $20")
print("For Large pizza charge is $25")

pizza = int(input("Enter the pizza price: "))

print("Here are add on available for your pizza")
print("for pepperoni extra charge is $2 for small and $3 for medium/large pizza")
pepperoni = int(input("Enter the pepperoni price (0/2/3): "))

print("Do you like to have extra cheeze for price $1")
cheeze = int(input("Enter the cheeze price (0/1): "))

bill_small_pizza = 15
bill_medium_pizza = 20
bill_large_pizza = 25

bill_small_pizza_with_pepperoni = 15 + 2
bill_medium_pizza_with_pepperoni = 20 + 3
bill_large_pizza_with_pepperoni = 25 + 3

bill_small_pizza_with_cheeze = 15 + 1
bill_medium_pizza_with_cheeze = 20 + 1
bill_large_pizza_with_cheeze = 25 + 1

bill_small_pizza_with_pepperoni_with_cheeze = 15 + 2 + 1
bill_medium_pizza_with_pepperoni_with_cheeze = 20 + 3 + 1
bill_large_pizza_with_pepperoni_with_cheeze = 25 + 3 + 1

if pizza == 15:
    if pepperoni == 2 and cheeze == 1:
        print(f"here is your small pizza with pepperoni and extra cheeze and bill is:${bill_small_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 2:
        print(f"here is your small pizza with pepperoni and bill is:${bill_small_pizza_with_pepperoni}")
    elif cheeze == 1:
        print(f"here is your small pizza with extra cheeze and bill is:${bill_small_pizza_with_cheeze}")
    else:
        print(f"here is your small pizza and bill is:${bill_small_pizza}")

if pizza == 20:
    if pepperoni == 3 and cheeze == 1:
        print(f"here is your medium pizza with pepperoni and extra cheeze and bill is:${bill_medium_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 3:
        print(f"here is your medium pizza with pepperoni and bill is:${bill_medium_pizza_with_pepperoni}")
    elif cheeze == 1:
        print(f"here is your medium pizza with extra cheeze and bill is:${bill_medium_pizza_with_cheeze}")
    else:
        print(f"here is your medium pizza and bill is:${bill_medium_pizza}")

if pizza == 25:
    if pepperoni == 3 and cheeze == 1:
        print(f"here is your large pizza with pepperoni and extra cheeze and bill is:${bill_large_pizza_with_pepperoni_with_cheeze}")
    elif pepperoni == 3:
        print(f"here is your large pizza with pepperoni and bill is:${bill_large_pizza_with_pepperoni}")
    elif cheeze == 1:
        print(f"here is your large pizza with extra cheeze and bill is:${bill_large_pizza_with_cheeze}")
    else:
        print(f"here is your large pizza and bill is:${bill_large_pizza}")

total_members = int(input("total members? "))

if total_members == 2:
    ask_to_play = input("Here is a game of random bill payer so are you going to play the game? y/n: ")
    if ask_to_play == "y":
        friend_1 = input("Enter your name: ")
        friend_2 = input("Enter your name: ")
        friends = [friend_1, friend_2]
        random_number = random.randint(1, 2)
        if random_number == 1:
            print(friend_1)
        else:
            print(friend_2)
        print("congratulation you are going to pay the bill")
    else:
        print("congratulation you are going to pay the bill")

elif total_members == 3:
    ask_to_play = input("Here is a game of random bill payer so are you going to play the game? y/n: ")
    if ask_to_play == "y":
        friend_1 = input("Enter your name: ")
        friend_2 = input("Enter your name: ")
        friend_3 = input("Enter your name: ")
        friends = [friend_1, friend_2, friend_3]
        random_number = random.randint(1, 3)
        if random_number == 1:
            print(friend_1)
        elif random_number == 2:
            print(friend_2)
        else:
            print(friend_3)
        print("congratulation you are going to pay the bill")
    else:
        print("congratulation you are going to pay the bill")

elif total_members == 4:
    ask_to_play = input("Here is a game of random bill payer so are you going to play the game? y/n: ")
    if ask_to_play == "y":
        friend_1 = input("Enter your name: ")
        friend_2 = input("Enter your name: ")
        friend_3 = input("Enter your name: ")
        friend_4 = input("Enter your name: ")
        friends = [friend_1, friend_2, friend_3, friend_4]
        random_number = random.randint(1, 4)
        if random_number == 1:
            print(friend_1)
        elif random_number == 2:
            print(friend_2)
        elif random_number == 3:
            print(friend_3)
        else:
            print(friend_4)
        print("congratulation you are going to pay the bill")
    else:
        print("congratulation you are going to pay the bill")

elif total_members == 5:
    ask_to_play = input("Here is a game of random bill payer so are you going to play the game? y/n: ")
    if ask_to_play == "y":
        friend_1 = input("Enter your name: ")
        friend_2 = input("Enter your name: ")
        friend_3 = input("Enter your name: ")
        friend_4 = input("Enter your name: ")
        friend_5 = input("Enter your name: ")
        friends = [friend_1, friend_2, friend_3, friend_4, friend_5]
        random_number = random.randint(1, 5)
        if random_number == 1:
            print(friend_1)
        elif random_number == 2:
            print(friend_2)
        elif random_number == 3:
            print(friend_3)
        elif random_number == 4:
            print(friend_4)
        else:
            print(friend_5)
        print("congratulation you are going to pay the bill")
    else:
        print("congratulation you are going to pay the bill")

else:
    print("congratulation you are going to pay the bill")

print("Hope you will visit again Have a nice day")

