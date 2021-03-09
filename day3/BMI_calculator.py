weight = int(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

BMI = round(weight/(height**2), 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are slightly underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}. You are obese.")
else:
    print(f"Your BMI is {BMI}. You are clinically obese.")


# Output
# Please enter your weight in kg: 85
# Please enter your height in m: 1.71
# Your BMI is 29.07. You are slightly overweight.

# Please enter your weight in kg: 75
# Please enter your height in m: 1.75
# Your BMI is 24.49. You have a normal weight.