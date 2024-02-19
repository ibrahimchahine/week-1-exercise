def sieve_of_eratosthenes(number_list):
    prime_numbers = [2, 3]
    array = list(number_list)
    length = len(array)
    i = 0
    while i < length:
        num = array[i]
        for j, prime in enumerate(prime_numbers):
            if num % prime == 0:
                i += 1
                break
            if j == len(prime_numbers) - 1:
                prime_numbers.append(num)
                # https://stackoverflow.com/questions/40851128/removal-of-multiples-of-a-number-on-a-list
                array = list(filter(lambda x: x % num, array))

        length = len(array)
    return prime_numbers


max = int(input("Enter The maximum number (N>3)"))
array = [i for i in range(4, max)]
primes = sieve_of_eratosthenes(array)
print(primes, len(primes))
