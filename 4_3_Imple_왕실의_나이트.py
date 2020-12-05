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