""" Hail the Primes """


def am_i_prime(num):
    """checks if a number is prime"""
    # If the number is less than or equal to 1, it's not prime
    if num <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False  # Not prime if divisible by any number in this range
        i += 1

    return True  # Prime if no divisors found


def get_user_input():
    """Prompt the user to enter the start and end values of the range"""
    start = int(input("Enter the start value of the range: "))
    end = int(input("Enter the end value of the range: "))

    # Validate the input to ensure that start is less than the end
    while start >= end:
        print("End value must be greater than start value. Please try again.")
        start = int(input("Enter the start value of the range: "))
        end = int(input("Enter the end value of the range: "))

    return (start, end)


def find_primes_in_range(start, end):
    """runs prime check function and appends valid numbers
    to a list"""
    prime_numbers = []
    for num in range(start, end + 1):
        if am_i_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def main():
    # Get user input for range
    start, end = get_user_input()

    # Find prime numbers within the range
    primes_in_range = find_primes_in_range(start, end)

    # Print the prime numbers
    print(f"Prime numbers in the range {start} to {end}:")
    print(primes_in_range)
    print('All Hail The Primes!')


# ---------program begin--------- #
main()
