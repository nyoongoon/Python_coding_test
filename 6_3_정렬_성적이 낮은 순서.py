n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(str(input().split())))

def setting(arr):
    return arr[1]

result = sorted(arr, key=setting, reverse=True)

for i in range(n):
    print(arr[0])

