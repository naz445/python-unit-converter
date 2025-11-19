# Python Unit Converter

A modular Python unit converter that supports multiple measurement conversions.  
This project demonstrates fundamental concepts such as user input handling, function-based architecture, modular design, and clean CLI formatting.

---

## Features

The converter currently supports the following transformations:

- Meter → Centimeter  
- Kilometer → Meter  
- Celsius → Fahrenheit  
- Kilogram → Gram  

Each conversion is implemented as a single-purpose function to ensure modularity and reusability.

---

## Technologies Used

- Python 3  
- Terminal/CLI interface  
- Modular function design  

---

## How It Works

The program uses a simple menu-driven architecture:

1. Users select an option  
2. The corresponding conversion function is executed  
3. The output is displayed in a clean format  

### Key Functions

#### `meter_to_centimeter(value)`
Converts meters into centimeters.

#### `kilometer_to_meter(value)`
Converts kilometers into meters.

#### `celsius_to_fahrenheit(value)`
Converts Celsius temperature into Fahrenheit.

#### `kilogram_to_gram(value)`
Converts kilograms into grams.

---

## Sample Output
— Unit Converter —
(1) Meter → Centimeter
(2) Kilometer → Meter
(3) Celsius → Fahrenheit
(4) Kilogram → Gram
(5) Exit
Select option: 3
Enter Celsius value: 22
Result: 71.6 °F
---

## Future Improvements

- Fahrenheit → Celsius support  
- Length-to-length full mapping (km ↔ m ↔ cm)  
- Weight conversions (gram ↔ kg ↔ pound)  
- GUI version with Tkinter  
- API-based remote conversion module  

---

## License

This project is released under the MIT License.
Enter Celsius value: 22
## Sample Output
