#!/usr/bin/env python3
# A prime number function
# Example of prime numebr is 2 ,3, 5, 7, 11..abs

def is_prime(number):
    # Check if the number is less than 2; if so, it's not prime
    if number < 2:
        return False

    # Check for divisibility from 2 to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False  # It's divisible, so it's not prime

    return True  # It's not divisible by any number, so it's prime


print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))