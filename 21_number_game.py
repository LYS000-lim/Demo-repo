def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ').strip().upper()

        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("How many numbers do you wish to enter? (1-3)")
                    inp = int(input('> '))

                    if 1 <= inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    print("Now enter the values (space-separated):")
                    user_input = input("> ").strip().split()

                    if len(user_input) != inp:
                        print("Number of inputs doesn't match your declared count.")
                        lose1()

                    for num in user_input:
                        xyz.append(int(num))

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            lose1()
                        else:
                            for j in range(1, comp + 1):
                                xyz.append(last + j)
                            print("Order of inputs after computer's turn is:")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Order of inputs after computer's turn is:")
                print(xyz)

                if xyz[-1] == 20:
                    lose1()

                print("\nYour turn.")
                print("How many numbers do you wish to enter? (1-3)")
                inp = int(input("> "))

                print("Enter your values (space-separated):")
                user_input = input("> ").strip().split()

                if len(user_input) != inp:
                    print("Number of inputs doesn't match your declared count.")
                    lose1()

                for num in user_input:
                    xyz.append(int(num))

                last = xyz[-1]

                if check(xyz):
                    near = nearestMultiple(last)
                    comp = near - last
                    if comp == 4:
                        comp = 3
                else:
                    print("\nYou did not input consecutive integers.")
                    lose1()

            print("\n\nCONGRATULATIONS !!!")
            print("YOU WON !")
            exit(0)

        else:
            print("Wrong choice. Please enter 'F' or 'S'.")

# Main loop
while True:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ').strip().lower()

    if ans == 'yes':
        start1()
    elif ans == 'no':
        print("Do you want to quit the game? (yes / no)")
        nex = input('> ').strip().lower()
        if nex == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex == "no":
            print("Continuing...")
        else:
            print("Wrong choice")
    else:
        print("Invalid input. Please type 'Yes' or 'No'.")
