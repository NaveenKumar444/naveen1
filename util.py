def find_max(num):
    x = num[0]
    for i in num:
        if i > x:
            x = i
    return x

