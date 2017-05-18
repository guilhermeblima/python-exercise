def menu():
    print("\n1 - Kilometers to Miles")
    print("2 - Miles to Kilometers")
    print("3 - Exit")
    choice = int(input("Choose your option: "))
    return choice

def km_to_miles(km):
    return km * 0.62137

def miles_to_km(miles):
    return 1.609 * miles

def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            kilometers = eval(input("\nType the distance in Kilometers: "))
            print("\nThe distance in miles: ",str("%.2f" % km_to_miles(kilometers)))
            choice = menu()
        elif choice == 2:
            miles = eval(input("\nType the distance in Miles: "))
            print("The distance in kilometers: ",str("%.2f" % miles_to_km(miles)))
            choice = menu()
        else:
            print("Invalid option!")
            choice = menu()

main()
