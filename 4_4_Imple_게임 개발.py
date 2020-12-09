n, m = map(int, input().split())
a, b, d = map(int, input().split())

arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].extend(list(map(int, input().split())))

count = 0

while(True):
    if not arr[a-1][b] == 0 or arr[a][b-1] == 0 or arr[a+1][b] == 0 or arr[a][b+1] == 0:
        if d == 0:
            b = b + 1
            if arr[a][b] == 1:
                break
        elif d == 1:
            a = a - 1
            if arr[a][b] == 1:
                break
        elif d == 2:
            b = b - 1
            if arr[a][b] == 1:
                break
        elif d == 3:
            a = a + 1
            if arr[a][b] == 1:
                break

    if d == 0:
        if arr[a-1][b] == 0:
            arr[a][b] = 2
            a = a-1
            count += 1
            d = 3
        else: d = 3
    elif d == 1:
        if arr[a][b-1] == 0:
            arr[a][b] = 2
            b = b-1
            count += 1
            d = 0
        else: d = 0
    elif d == 2:
        if arr[a+1][b] == 0:
            arr[a][b] = 2
            a = a+1
            count += 1
            d = 1
        else: d = 1
    elif d == 3:
        if arr[a][b+1] == 0:
            arr[a][b] = 2
            b = b+1
            d = 2
            count += 1
        else: d = 2

print(count)