n, m, k = int(input().split()) # k <= m
arr = list(int(input().split())) # n == len(arr)
count = 0
# 최댓값 뽑기 -> 오름차순 정렬
arr.sort()
# 최댓값을 k번 넣기
arr_plus = []

while count != m:
    for i in range(k + 1):
        arr_plus.append(arr[0])
        count += 1
    # 그다음 최댓값 1번 더하기
    arr_plus.append(arr[1])
    count += 1

# 최댓값 k번 더하기

# len(arr_plus) == m 일때 sum 출력.
print(sum(arr_plus))