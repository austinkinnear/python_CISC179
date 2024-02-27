from sys import path

path.append('labs\\lab5\\modules') #In CISC and then I am telling it to go into labs, labs5 and then modules

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

