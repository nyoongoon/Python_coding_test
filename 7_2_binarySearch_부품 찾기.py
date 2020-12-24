n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))
arr2.sort()

def binary_search(array, target, start, end):
    if start>end:
        return "no"
    mid = (start+end)//2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

results = []

for target in arr2:
    result = binary_search(arr1, target, 0, n-1)
    results.append(result)

for answer in results:
    print(answer, end=" ")
