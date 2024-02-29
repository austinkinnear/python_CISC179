from sys import path
# Appends the path to my directory to get to extra 
path.append('labs\\lab5\\packages')

# Imports extra package and its subpackages sigma, alpha, iota, and beta modules
import extra.good.best.sigma as sig 
import extra.good.alpha as alp 
from extra.iota import FunI 
from extra.good.beta import FunB 

# Print function of FunS, FunA, FunI and FunB from sigma, alpha, iota, and beta
print(sig.FunS()) 
print(alp.FunA()) 
print(FunI())
print(FunB())