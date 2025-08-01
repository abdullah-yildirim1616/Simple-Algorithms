def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result



def combination(x, y):
    return factorial(x) // (factorial(y) * factorial(x - y))

print(combination())