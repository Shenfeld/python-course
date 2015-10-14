n, k = input().split(' ')
n = int(n)
k = int(k)
def combinations(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    answer = 1
    for i in range(1, k+1):
        answer = answer * (n-i+1) // i
    return answer
print(combinations(n, k))# put your python code here
