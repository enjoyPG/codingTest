# 문제 2-1: 리스트 출력
print("문제 2-1")
arr = list(map(int, input().split()))
print(arr[0])
print(arr[1])
print(arr[2])


# 문제 2-2: 같은지 비교
print("\n문제 2-2")
arr = list(map(int, input().split()))
print(arr[0] == arr[2])


# 문제 2-3: 같은 숫자 찾기 (반복문 사용)
print("\n문제 2-3")
arr = list(map(int, input().split()))
found = False
for i in range(3):
    for j in range(i + 1, 3):
        if arr[i] == arr[j]:
            print("같은 숫자 발견:", arr[i])
            found = True
            break
    if found:
        break


# 문제 2-4: 같은 숫자의 위치
print("\n문제 2-4")
arr = list(map(int, input().split()))
for i in range(4):
    for j in range(i + 1, 4):
        if arr[i] == arr[j]:
            print("숫자", arr[i], "의 위치:", i, "와", j)
            break
    else:
        continue
    break


# 문제 2-4.5: 대량 수열에서 첫 중복 위치 찾기 (쉽게)
print("\n문제 2-4.5")
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(f"{arr[i]} : {i} - {j}")
            exit()


# 문제 2-5: 모든 숫자의 첫 중복 위치 찾기 (쉽게)
print("\n문제 2-5")
arr = list(map(int, input().split()))
checked = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in checked:
            print(f"{arr[i]} : {i} - {j}")
            checked.append(arr[i])
            break
