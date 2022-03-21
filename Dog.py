def main():
    choice = 0
    while choice != 5:
        print("What to do?")
        print()
        print("1 Drop off dog")
        print("2 Pick up dog")
        print("3 Calculate cost")
        print("4 Print dog roll")
        print("5 Exit the system")
        print()
        print("===================================")

        choice = integer_checker("Enter your choice (number between 1 and 5): ")
        if choice == 1:
            drop_off()

        elif choice == 2:
            pick_up()

        elif choice == 3:
            calc_cost(len(roll))

        elif choice == 4:
            print_roll()

        elif choice == 5:
            end_program()

        else:
            print("Must be a number from 1 and 5")


def drop_off():
    dog_name = input("Enter name of dog: ")
    roll.append(dog_name)


def pick_up():
    dog_name = input("Enter name of dog to pick up: ")
    if dog_name in roll:
        roll.remove(dog_name)
        print(f"{dog_name} has been removed")
    else:
        print("We have no dog by that name")


def calc_cost(number):
    rate = 22.5
    days = integer_checker("How many days?")
    cost = number * days * rate
    print(f"The cost for {number} dogs for {days} is {cost}")


def print_roll():
    print("Dogs currently in DogsRus: ")
    for dog in roll:
        print(f"\{dog}")
    print()


def end_program():
    print("Bye!")


def integer_checker(question):
    error = "\nSorry, you must enter a integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


roll = []

print(
    "-------------------------------------------")

main()

