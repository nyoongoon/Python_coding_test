n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 배열 A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때에만 교체를 수행해야한다.

arr1.sort()
arr2.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(sum(arr1))