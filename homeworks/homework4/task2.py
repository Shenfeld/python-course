def factorial(x):
    n = 1
    if x == 0:
        return 1
    else:
        for i in range(1,x + 1):
            n = n*i
    return n
a = open("dict.txt", "r")
text = a.read()
numbr=0
adj = 0
noun = 0
for word in text.split('\n'):
    if word.endswith ('yo'):
        adj +=1
    elif word.endswith ('ka'):
        noun+=1
    else:
        numbr+=1
adjective = 0
for i in range(1, adj+1):
    adjective += factorial(adj) // factorial(adj - i)
print(adjective*noun*numbr)


