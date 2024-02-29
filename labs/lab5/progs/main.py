from sys import path

path.append('labs\\lab5\\modules') #In python_CISC 179 and then I am telling it to go into labs, labs5 and then modules

import module
# List of 5 zeroes
zeroes = [0 for i in range(5)]
# List of 5 ones
ones = [1 for i in range(5)]
# Printing the sum1 and prod1 function from module
print(module.suml(zeroes)) # Gets sum of list of zeros
print(module.prodl(ones)) # Gets product of ones

