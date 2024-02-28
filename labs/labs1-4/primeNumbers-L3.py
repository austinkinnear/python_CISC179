import random  # random module used to shuffle the prime numbers

prime = []
for num in range(2, 100): 
    is_prime = True
    # Check if num is divisible by any number between 2 and num - 1
    for i in range(2, num):
        if num % i == 0: 
            is_prime = False
            break
    if is_prime:
        prime.append(num)

rnd_prime = prime.copy()
# random.shuffle is a function to randomize the elements in the array
# rnd_prime is the array to store the shuffled prime numbers
random.shuffle(rnd_prime)

print("Prime Numbers:", prime)
print("Randomized Prime Numbers:", rnd_prime)

# Part 3: Selection Sort algorithm to sort the randomized list of prime numbers
for i in range(len(rnd_prime)):
    min_idx = i
    for j in range(i+1, len(rnd_prime)):
        if rnd_prime[j] < rnd_prime[min_idx]:
            min_idx = j
    rnd_prime[i], rnd_prime[min_idx] = rnd_prime[min_idx], rnd_prime[i]

print("Sorted Prime Numbers:", rnd_prime)

#Part 1: To find prime numbers 0 to 100 I used a basic way because I knew how to find them this way. To find numbers 0 through 100 I can loop through them and find each number that 
#is divisible by itself and the num - 1. The problem is 0 and 1 also fit into this so instead of restarting, I set the range to be from 2 the first prime number to 100.
#The first if statement allows me to quickly seperate non prime with prime numbers. Using the append I am able to store each element in the array.

#Part 4: Array's are better than lists because they take less memory, but lists do have more flexability. Array's are faster, and work when elements are known or unknown.
#List's are better if the amount of elements isnt known.


