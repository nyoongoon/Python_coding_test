n = int(input())
arr = []
for i in range(n):
    input_data = input().split()
    arr.append(((input_data[0], int(input_data[1]))))

def setting(arr):
    return arr[1]

result = sorted(arr, key=setting)
# 람다 가능 result = sorted(arr, key = lambda setting:setting[1])
for results in result:
    print(results[0], end=' ')

