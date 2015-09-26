numbers = input().split()
numbers = [int(i) for i in numbers]
chet = []
nechet = []
for index, number in enumerate(numbers):
    if index % 2 != 0:
        nechet.append(number)
    else:
        chet.append(number)
nechet.sort()
nechet.reverse()
chet.sort()
result = ' '
for index in range(len(chet)):
    result = result + str(chet[index])+' '
    result = result + str(nechet[index])+' '
print(result)
