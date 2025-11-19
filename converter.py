def meter_to_centimeter(value: float) -> float:
    return value * 100

def kilometer_to_meter(value: float) -> float:
    return value * 1000

def celsius_to_fahrenheit(value: float) -> float:
    return (value * 9/5) + 32

def fahrenheit_to_celsius(value: float) -> float:
    return (value - 32) * 5/9

def kilogram_to_gram(value: float) -> float:
    return value * 1000


def show_menu():
    print("\n--- Unit Converter ---")
    print("(1) Meter → Centimeter")
    print("(2) Kilometer → Meter")
    print("(3) Celsius → Fahrenheit")
    print("(4) Kilogram → Gram")
    print("(5) Exit")


def main():
    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            value = float(input("Enter value: "))
            print("Result:", meter_to_centimeter(value))
        elif choice == "2":
            value = float(input("Enter value: "))
            print("Result:", kilometer_to_meter(value))
        elif choice == "3":
            value = float(input("Enter Celsius value: "))
            print("Result:", round(celsius_to_fahrenheit(value), 2), "°F")
        elif choice == "4":
            value = float(input("Enter value: "))
            print("Result:", kilogram_to_gram(value))
        elif choice == "5":
            break
        else:
            print("Invalid option.")

main()
