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

"""
# n 을 입력받기
n = int(input)
x, y = 1, 1
plans = input().split

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1] #세로로 보는 좌표!
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)        


"""

