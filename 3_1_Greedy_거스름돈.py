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

