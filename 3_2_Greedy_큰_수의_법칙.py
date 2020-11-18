n, m, k = map(int, input().split()) # map로 입력 받기
arr = list(map(int, input().split())) # list로 입력 받기
result = 0 # 결과값
# 최댓값 뽑기 -> 오름차순 정렬 ->(작은 수가 먼저)반대로 세기!!
arr.sort()
first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 가장 큰 수

# 반복되는 수열에 대해 파악!!!
count = int(m / k+1) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second
print(result)

