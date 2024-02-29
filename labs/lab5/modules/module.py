import sys
for p in sys.path:
    print(p)

# Private counter variable  
__counter = 0
# Function to calculate the sume of elements within a list
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

# Function to calculate the product of elements within a list
def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

# Module runs only as a script, and not as an import 
if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)