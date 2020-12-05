# 현재 나이트의 위치 입력받기! (답안 도움 받음->ord()알아두기)
input_data = input()
row = int(input_data[1]) # 문자열을 리스트처럼 인덱스 활용!
col = int(ord(input_data[0]))-int(ord('a')) + 1 # ord()->문자 아스키 코드값으로 변

count = 0


if 1 <= col + 2 <= 8 and 1 <= row + 1 <= 8:
    count += 1
if 1 <= col + 2 <= 8 and 1 <= row - 1 <= 8:
    count += 1
if 1 <= col - 2 <= 8 and 1 <= row + 1 <= 8:
    count += 1
if 1 <= col - 2 <= 8 and 1 <= row - 1 <= 8:
    count += 1
if 1 <= col + 1 <= 8 and 1 <= row + 2 <= 8:
    count += 1
if 1 <= col - 1 <= 8 and 1 <= row + 2 <= 8:
    count += 1
if 1 <= col + 1 <= 8 and 1 <= row - 2 <= 8:
    count += 1
if 1 <= col - 1 <= 8 and 1 <= row - 2 <= 8:
    count += 1

print(count)

"""
*답안
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 리스트로 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0 

for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동할 수 있으면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)
"""