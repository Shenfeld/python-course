def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a+b)
a, b = input().split(' ')
a = int(a)
b = int(b)
print (euclid(a, b))

