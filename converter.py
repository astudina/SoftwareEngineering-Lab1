def convertor(temperature):
    temperature = temperature.split(" ")

    if len(temperature) != 2:
        print("You should write two arguments")
    else:
        try:
            degree = int(temperature[0])
            unit = temperature[1]
            if unit.upper() == "C":
                res_degree = int(round((9 * degree) / 5 + 32))
                print("The temperature in Fahrenheit is", res_degree, "degrees.")
            elif unit.upper() == "F":
                res_degree = int(round((degree - 32) * 5 / 9))
                print("The temperature in Celsius is", res_degree, "degrees.")
            else:
                print("Incorrect measurement unit")
        except ValueError:
            print("Incorrect input")


temp = input("Enter the temperature you want to convert (e.g. 12 F or 24 C): ")
convertor(temp)
