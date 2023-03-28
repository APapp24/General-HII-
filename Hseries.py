def calc(a, b):
    ionisationEnergy = 13.598433
    Z = 1
    R = 109677.5834 * 1.e7
    return (R * Z**2 * (a**-2 - b**-2))**-1

while True:
    num1 = float(input("Enter first energy level: "))
    # if num1 not in (1, 2, 3, 4, 5, 6):
    #     print("Please enter a valid energy level.")

    num2 = float(input("Enter second energy level: "))
    # if num2 not in ('1', '2', '3', '4', '5'):
    #     print("Please enter a valid energy level.")

    if num1 == num2:
        print("Division by zero error. Please retry.")
        continue

    print("Wavelength: ", calc(num1, num2))

    onward = input("Continue calculations? (yes/no): ")
    if onward == "no":
        break

# --expression for stromgren sphere
# academic search complete: stromgren spheres: how created, radius, spectral type of stars/radii --> relationship b/t spectral type and radii

# rationale behind choice ML engine, pros/cons of all options --> why'd we choose this one?
# APJ format for references