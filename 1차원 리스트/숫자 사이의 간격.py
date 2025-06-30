# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 가장 긴 거리 저장할 변수
max_count = 0

# 첫 번째 숫자 위치를 i라고 하고
for i in range(len(arr)):
    # 그 다음 위치부터 끝까지 돌면서
    for j in range(i + 1, len(arr)):
        # 같은 숫자를 찾으면
        if arr[i] == arr[j]:
            # 그 사이에 있는 숫자 개수는 (j - i - 1)
            count = j - i - 1
            # 최대값 갱신
            if count > max_count:
                max_count = count
            break  # 같은 숫자는 2번만 나오니까 더 볼 필요 없음

# 정답 출력
print(max_count)
