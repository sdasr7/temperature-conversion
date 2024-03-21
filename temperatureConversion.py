""" Temperature Conversion ----> Supriyo Das """

def convert_temperature(temp):
    unit = temp[-1]
    value = int(temp[:-1])
    
    if unit == 'C':
        celsius_to_fahrenheit = (value * 9/5) + 32
        return celsius_to_fahrenheit, 'Fahrenheit'
    elif unit == 'F':
        fahrenheit_to_celsius = (value - 32) * 5/9
        return fahrenheit_to_celsius, 'Celsius'
    else:
        return None, None

def main():
    print("Python program to convert temperatures to and from Celsius, Fahrenheit\n")

    temp_input = input('Input the temperature you would like to convert? (e.g: 102C, 45F, 110C etc.): ').upper()

    result, target_unit = convert_temperature(temp_input)

    if result is not None and target_unit is not None:
        print(f'The temperature in {target_unit} is {result} degrees.')
    else:
        print('Invalid input. Please provide temperature in the correct format (e.g: 102C, 45F).')

if __name__ == "__main__":
    main()
