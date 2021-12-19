def is_number_try_except(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def input_numbers():
    while 1 == 1:
        num = (input())
        if is_number_try_except(num):
            return float(num)
        print("Only numbers")


def yes_or_no():
    answer = input().casefold()
    if answer == "yes" or answer == "y" or answer == "ye":
        return "yes"
    else:
        return "no"


def calc():
    print("How old is the dog in years")
    years = input_numbers()
    if years > 1:
        if years > 2:
            age = 22 + 5 * years
        else:
            age = 14 + 8 * years
    else:
        age = 14 * years

    print(f"The dog is {age} human years old")
    print("Want to calculate again (yes/no)")
    if yes_or_no() == "yes":
        calc()
    else:
        frog_or_dog()


def frog():
    print("How wide is the road the frog wants to cross?")
    distance = input_numbers()
    frog_distance = 0
    frog_jumps_length = 1
    jumps = 0
    finished = "no"
    while not frog_distance >= float(distance):
        jumps += 1
        frog_distance += frog_jumps_length
        if frog_jumps_length < 0.001:
            finished = "error"
            break
        else:
            print(
                f"The frog jumped from a distance of {frog_distance - frog_jumps_length}m "
                f"to a distance of {frog_distance}m"
                f" with jump no:{jumps}.")
        frog_jumps_length = frog_jumps_length / 2
    if finished == "error":
        print(f"The frog passed out after {jumps} jumps and a total distance of {frog_distance}m.")
    else:
        print(f"The frog needs {jumps} jumps to cross the road.")
    print("Do you want to torture the frog again?")
    if yes_or_no() == "yes":
        frog()
    else:
        frog_or_dog()


def frog_or_dog():
    print("Do you want to choose the frog calculator or the dog calculator? (dog/frog)")
    while 1 == 1:
        d = input().casefold()
        if d == "dog" or d == "d":
            calc()
        elif d == "frog" or d == "f":
            frog()
        print("Please answer the question.")


frog_or_dog()
