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
"""
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력받아 확인
for i in n:
    arr = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(arr)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)
"""
"""
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력받아 확인
for i in n:
    arr = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in arr:
        min_value = min(min_value, a) # 각 행에서 최소값 뽑아서 저장
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)        
"""

