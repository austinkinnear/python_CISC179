import cmath

def solve_quadratic(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b - d) / (2*a)
    x2 = (-b + d) / (2*a)
    return x1, x2

def format_solution(x):
    if x.imag == 0:
        return x.real
    else:
        return x

a = float(input("Enter a term for a: "))
while a == 0:
    a = float(input("a cannot be 0. Enter a different value for a: "))

b = float(input("Enter a term for b: "))
c = float(input("Enter a term for c: "))

solution = solve_quadratic(a, b, c)
formatted_solution = [format_solution(s) for s in solution]
print(f"The solutions are {formatted_solution[0]} and {formatted_solution[1]}")
