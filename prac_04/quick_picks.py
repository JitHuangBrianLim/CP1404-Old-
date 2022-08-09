import random

LINE_LIMIT = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(LINE_LIMIT):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()