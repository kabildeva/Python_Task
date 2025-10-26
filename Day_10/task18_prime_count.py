def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = {2, 3, 4, 5, 6, 7, 8}
prime_count = len([n for n in nums if is_prime(n)])
print('Number of primes:', prime_count)
