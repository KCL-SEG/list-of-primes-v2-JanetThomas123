"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""



def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("number of primes should be a positive number.")

    list = []
    num = 2
    while len(list) < number_of_primes:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            list.append(num)
        num += 1
    return list
