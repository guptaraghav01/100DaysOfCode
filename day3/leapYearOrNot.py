year = int(input("Enter the year you wish to check if it's leap or not: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Output
# Enter the year you wish to check if it's leap or not: 2000
# 2000 is a leap year.

# Enter the year you wish to check if it's leap or not: 2100
# 2100 is not a leap year.