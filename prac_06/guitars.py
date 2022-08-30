
from Guitar import Guitar


def main():
    guitars_list = []

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        formatted_guitar = Guitar(guitar_name, year, cost)
        guitars_list.append(formatted_guitar)
        print(f"{formatted_guitar} added.")
        guitar_name = input("Name: ")

    guitars_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars_list:
        guitars_list.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars_list):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars.")


main()