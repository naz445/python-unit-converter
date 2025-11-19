def meter_to_centimeter(value: float) -> float:
    return value * 100


def kilometer_to_meter(value: float) -> float:
    return value * 1000


def celsius_to_fahrenheit(value: float) -> float:
    return (value * 9 / 5) + 32


def kilogram_to_gram(value: float) -> float:
    return value * 1000


def show_menu():
    print("\n=== Unit Converter ===")
    print("1) Meter → Centimeter")
    print("2) Kilometer → Meter")
    print("3) Celsius → Fahrenheit")
    print("4) Kilogram → Gram")
    print("5) Exit")


def main():
    while True:
        show_menu()
        choice = input("Your choice (1–5): ").strip()

        if choice == "5":
            print("Exiting program...")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid selection. Please choose between 1 and 5.")
            continue

        try:
            value_str = input("Enter the value to convert: ").strip()
            value = float(value_str)
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if choice == "1":
            result = meter_to_centimeter(value)
            print(f"{value} meters = {result} centimeters")
        elif choice == "2":
            result = kilometer_to_meter(value)
            print(f"{value} kilometers = {result} meters")
        elif choice == "3":
            result = celsius_to_fahrenheit(value)
            print(f"{value} °C = {result} °F")
        elif choice == "4":
            result = kilogram_to_gram(value)
            print(f"{value} kilograms = {result} grams")


if __name__ == "__main__":
    main()