def converter(temperature):
    temperature = temperature.split(" ")

    degree = int(temperature[0])
    unit = temperature[1]

    if unit.upper() == "F":
        res_degree = int(round((degree - 32) * 5 / 9))
        res_unit = "Celsius"
    else:
        print("Incorrect measurement unit")
        exit(0)
    print("The temperature in", res_unit, "is", res_degree, "degrees")


temp = input("Enter the temperature you want to convert from Fahrenheit to Celsius (e.g. 12 F or 24 F): ")
converter(temp)
