"""Try to make a script that converts Celsius to Fahrenheit
and creates a text file and stores the converted values inside the text file.
Your text file content should look like this:
50.0
-4.0
212.0
Please don't write any message in the text file when input is lower than -273.15.
"""
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def write_file(temperature):
    with open("allowed_temperatures.txt", "a") as file:
            file.write(str(temperature)+"\n")

def main():
    temperatures = [10,-20,-289,100]
    for temperature in temperatures:
        if temperature > -273.15:
             write_file((celsius_to_fahrenheit(temperature)))

main()
