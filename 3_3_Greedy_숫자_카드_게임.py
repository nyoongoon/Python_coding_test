row, col = map(int, input().split()) # row는 리스트 갯수, col은 리스트 길이
arr = []
max = 0
for i in range(row):
    arr.append(list(map(int, input().split())))

for i in range(row):
    arr[i].sort()

for i in range(row):
    if max <= arr[i][0]:
        max = arr[i][0]

print(max)


# 각 행의 최솟값은 arr[i][-1]

