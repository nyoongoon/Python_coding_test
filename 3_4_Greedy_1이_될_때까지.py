n, k = map(int, input().split())
count = 0;
while True:
    if n % k == 0:
        n = n // k
        count += 1
        if n == 1:
            break
    else :
        n -= 1
        count += 1
        if n == 1:
            break
print(count)

"""
단순하게 푸는 답안 예
n, k = map(int, input().split())
result = 0;

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 뺴기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k # k로 나눈 몫을 n에 저장
    result += 1
    
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
    
print(result)
"""
"""
일일이 1씩 빼는 것이 느려질 수 있으므로
N이 K의 배수가 되도록 효율적으로 한번에 뺴는 방식

n, k = map(int, input().split())
result = 0;

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 뺴기
    target = (n // k) * k 
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # K로 나누기 
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (n-1)
print(result)
"""
