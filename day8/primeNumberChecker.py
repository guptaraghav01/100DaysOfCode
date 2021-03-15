def prime_checker(number):
    is_prime = "Is Prime"
    for i in range(2, number):
        if number % i == 0:
            is_prime = "Is not Prime"

    print(is_prime)


n = int(input("Check this number: "))
prime_checker(number=n)

# Output
# Check this number: 9
# Is not Prime

# Check this number: 11
# Is Prime
