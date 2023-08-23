for i in range(1582, 2025, 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i, "es bisiesto.")
    else:
        print(i, "no es bisiesto.")
