def my_range(a, b):
    while a <= b:
        yield a**2
        a += 1

a = int(input())
b = int(input())

for val in my_range(a, b):
    if val == a**2:
        print(val)
    a+=1