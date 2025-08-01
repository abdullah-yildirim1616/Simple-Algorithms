def find_divisors(x):
    divisors = set()
    i = 1
    while i * i <= x:
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
        i += 1
    return sorted(divisors)

print(find_divisors(36))