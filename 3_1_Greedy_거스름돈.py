"""
n = int(input()) # 거슬러 줘야할 돈
def count(n):
    coin = 0
    while n >= 500:
        n -= 500
        coin += 1
    while 500 > n >= 100:
        n -= 100
        coin += 1
    while 100 > n >= 50:
        n -= 50
        coin += 1
    while 50 > n >= 10:
        n -= 10
        coin += 1
    return coin
"""

n = 1260 # 예시
count = 0
# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 정수 나누기 후 갯수 카운트에 저장
    n %= coin # n에 n을 coin으로 나눈 나머지 저장
print(count)