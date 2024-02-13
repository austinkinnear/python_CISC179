import random

# Function to generate prime numbers using Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    primes = []
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return primes

# Function to sort an array using Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Generate prime numbers from 1 to 100
prime = sieve_of_eratosthenes(100)

# Randomize the order of prime numbers
rnd_prime = prime.copy()
random.shuffle(rnd_prime)

# Sort the randomized prime numbers using Selection Sort
sorted_rnd_prime = selection_sort(rnd_prime)

prime, rnd_prime, sorted_rnd_prime  # Display the original, randomized, and sorted arrays

