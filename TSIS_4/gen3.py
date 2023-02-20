def div(n):
    div_list = []
    for val in range(0, n+1):
        if val % 3 == 0 and val % 4 == 0:
            div_list.append(val)
    return div_list

n = int(input())
print(div(n))