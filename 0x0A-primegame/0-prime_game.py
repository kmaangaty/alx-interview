#!/usr/bin/python3
""" Module for determining the winner in the prime game """


def isWinner(x, nums):
    """ Determine the winner between Maria
    and Ben based on the prime game rules """
    if not nums or x < 1:
        return None
    # Find the maximum number in nums to determine
    # the range for the sieve
    max_num = max(nums)
    # Sieve array to mark prime numbers up to max_num
    sieve = [True for _ in range(max(max_num + 1, 2))]
    # Implementing the Sieve of Eratosthenes algorithm
    # to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            sieve[j] = False
    # 0 and 1 are not prime numbers
    sieve[0] = sieve[1] = False
    # Counting the number of primes up to each index
    # using cumulative sum
    prime_count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            prime_count += 1
        sieve[i] = prime_count
    # Counting points for Maria based on the number
    # of odd-indexed primes in nums
    maria_points = 0
    for n in nums:
        maria_points += sieve[n] % 2 == 1
    # Determining the winner based on points comparison
    if maria_points * 2 == len(nums):
        return None
    if maria_points * 2 > len(nums):
        return "Maria"
    return "Ben"
