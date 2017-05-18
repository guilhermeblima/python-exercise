def menu():
    print("\n1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("3 - Exit")
    return int(input("Select the option: "))

def celsius_to_fehrenheit(celsius):
    return (celsius * 1.8) + 32

def fehrenheit_to_celsius(fehrenheit):
    return (fehrenheit - 32) / 1.8

def main():
    option = menu()
    while option != 3:
        if option == 1:
            celsius = eval(input("Insert the temperature in Celsius: "))
            print("The temperature in fehrenheit is: ", str(celsius_to_fehrenheit(celsius)))
            option = menu()
        elif option == 2:
            fehrenheit = eval(input("Insert the temperature in Fehrenheit: "))
            print("The temperature in celsius is: ", str(fehrenheit_to_celsius(fehrenheit)))
            option = menu()
        else:
            print("Invalid option, try again...")
            option = menu()

main()
