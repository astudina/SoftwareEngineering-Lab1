def convertor(temperature):
    temperature = temperature.split(" ")

    if len(temperature) != 2:
        print("You should write two arguments")
        exit()
    else:
        try:
            degree = int(temperature[0])
            unit = temperature[1]
        except ValueError:
            print("Incorrect input")
            exit()

    if unit.upper() == "C":
        res_degree = int(round((9 * degree) / 5 + 32))
        res_unit = "Fahrenheit"
    elif unit.upper() == "F":
        res_degree = int(round((degree - 32) * 5 / 9))
        res_unit = "Celsius"
    else:
        print("Incorrect measurement unit")
        exit()
    print("The temperature in", res_unit, "is", res_degree, "degrees.")


temp = input("Enter the temperature you want to convert (e.g. 12 F or 24 C): ")
convertor(temp)
