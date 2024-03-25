weight = int(input("give me your weight: "))
height = int(input("what is your height: "))


BMI = (weight * 703) / (height * height)
print(BMI)

if BMI <= 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 40:
    print("Overweight")
else:
    print("Obese")