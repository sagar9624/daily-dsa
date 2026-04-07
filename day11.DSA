def missing_number(arr, n):
    xor1 = 0
    xor2 = 0
    for i in range(n - 1):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i + 1)
    return xor1 ^ xor2 ^ n

n = int(input())
arr = list(map(int, input().split()))
result = missing_number(arr, n)
print(result)
