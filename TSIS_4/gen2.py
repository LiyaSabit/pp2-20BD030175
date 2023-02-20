def factors(n):
    factors_list = []
    for val in range(1, n+1):
        if val % 2 == 0:
            factors_list.append(val)
    return factors_list

n=int(input())
print(*factors(n), sep=", ")