FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function to handle user input and perform temperature conversions."""
    try:
        # Get temperature input
        temperature_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temperature_input)  # Validate numeric input
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on user input
        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the script
if __name__ == "__main__":
    main()
