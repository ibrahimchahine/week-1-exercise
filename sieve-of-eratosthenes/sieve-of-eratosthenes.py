def sieve_of_eratosthenes(number_list):
    prime_numbers = [2, 3]
    array = list(number_list)
    for num in array.copy():
        for j, prime in enumerate(prime_numbers):
            if num % prime == 0:
                break
            if j == len(prime_numbers) - 1:
                prime_numbers.append(num)
                # https://stackoverflow.com/questions/40851128/removal-of-multiples-of-a-number-on-a-list
                array.remove(num)
                array = list(filter(lambda x: (x % num) > 0, array))

    return prime_numbers


max = int(input("Enter The maximum number (N>3)"))
array = [i for i in range(4, max)]
primes = sieve_of_eratosthenes(array)
print(primes, len(primes))
