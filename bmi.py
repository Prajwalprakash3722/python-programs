# program to calculate bmi(Body Mass Index)
is_weight = int(input("What is your weight? "))
is_unit = input("(K)gs, (P)ounds ")
is_height = int(input("What is your height? "))
is_unita = input("(C)m, (I)nch, (F)t ")
mass = 1
# checking the weight is it is in pounds then converting it to kg
if is_unit.lower() == 'k':
    mass = int(is_weight)
elif is_unit.lower() == 'p':
    mass = int(is_weight) * 0.4535
else:
    print(f"Type only given Letters, you have typed {is_unit.upper()} instead of K or P")
meter = 1
# Checking the height and converting to Metter units
if is_unita.lower() == 'c':
    meter = int(is_height) * 0.01
elif is_unita.lower() == 'i':
    meter = int(is_height) * 0.0254
elif is_unita.lower() == 'f':
    meter = int(is_height) * 0.3047999
else:
    print(f"Type only given Letters, you have typed {is_unita.upper()} instead of C or I or F")

# Calculating the BMI
h = meter * meter
bmi = mass / h
if bmi < 18.5:
    type = "Under weight"
elif bmi>=18.5 and bmi<=24.9:
    type = "Normal"
elif bmi >= 25 and bmi <= 29.9:
    type = "Over-weight"
else:
    type = "Obese"
print(f"Your BMI(Body Mass Index) is {bmi}, You are {type}")
