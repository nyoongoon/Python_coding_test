n, m, k = map(int, input().split()) # map로 입력 받기
arr = list(map(int, input().split())) # list로 입력 받기
result = 0 # 결과값
# 최댓값 뽑기 -> 오름차순 정렬 ->(작은 수가 먼저)반대로 세기!!
arr.sort()
first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 두번쨰 큰 수
# 내가 구한 공식!!
result = (k*first+second) * (m // (k + 1))
        # 한 수열내의 합 * 수열의 갯수
result += (m % (k + 1)) * first
        # 나머지 값 더하기

print(result)
