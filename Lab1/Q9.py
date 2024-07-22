# WAP to check whether a)is a perfect number b)is an Armstrong number

def is_perfect(n):
    if n < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == n

number = int(input("Enter a number: "))

if is_perfect(number):
    print(f"{number} is a Perfect number.")
else:
    print(f"{number} is not a Perfect number.")

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

