n, m, k = map(int, input().split()) # map로 입력 받기
arr = list(map(int, input().split())) # list로 입력 받기
result = 0 # 결과값
# 최댓값 뽑기 -> 오름차순 정렬 ->(작은 수가 먼저)반대로 세기!!
arr.sort()
first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 가장 큰 수

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기 # k-1번이 아니라 k번!
        if m == 0: # 더할 때마다 m 값 검사
            break
        result += first
        m -= 1 # 더할 때마다 1 빼기
    if m == 0: # 더할 때마다 m 값 검사
        break
    result += second
    m -= 1 # 더할 때마다 1 빼기

print(result)
