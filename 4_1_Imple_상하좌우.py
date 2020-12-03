# 시뮬레이션 유형 : 일련의 명령에 따라서 개체를 차례대로 이동!

n = int(input())
arr = list(map(str, input().split()))
print(arr)
x, y = 1, 1

for key in arr:
    if key == "L":
        y += -1
        if 1 > y or y > n:
            y += 1
    elif key == "R":
        y += 1
        if 1 > y or y > n:
            y += -1
    elif key == "U":
         x += -1
         if 1 > x or x > n:
             x += 1
    elif key == "D":
         x += 1
         if 1 > x or x > n:
             x += -1

print(x, y)

