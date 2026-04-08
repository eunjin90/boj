# BOJ11728
# 정렬된 두 배열을 합치는 문제 (병합, merge)
# 정렬된 두 배열 A, B를 하나로 합쳐 정렬된 결과를 만드는 문제

size_A, size_B = map(int, input().split())  # A 배열의 크기(size_A), B 배열의 크기(size_B) 입력
A = list(map(int, input().split())) # 정렬된 배열 A 입력
B = list(map(int, input().split())) # 정렬된 배열 B 입력

merged_list = []    # 두 배열을 합친 결과를 저장할 리스트

pA = pB = 0
# pA: A 배열을 가리키는 포인터
# pB: B 배열을 가리키는 포인터
# 둘 다 처음 인덱스 0부터 시작

while pA < size_A and pB < size_B:  # A와 B 둘 다 아직 끝까지 안 간 경우에 반복
    if A[pA] < B[pB]:   # A의 현재 값이 더 작으면
        merged_list.append(A[pA])   # A의 값을 결과 리스트에 추가
        pA += 1 # A 포인터를 다음으로 이동
    else:   # B의 현재 값이 더 작거나 같은 경우
        merged_list.append(B[pB])   # B의 값을 결과 리스트에 추가
        pB += 1 # B 포인터를 다음으로 이동

# ================================
# A 배열에 남은 값 처리
# ================================
# while pA < size_A:
#     merged_list.append(A[pA])
#     pA += 1
if pA < size_A: # A 배열에 아직 남은 값이 있으면
    # merged_list += A[pA:size_A]
    merged_list.extend(A[pA:size_A])    # 남은 부분을 통째로 이어붙임 (슬라이싱 사용)

# ================================
# B 배열에 남은 값 처리
# ================================
# while pB < size_B:
#     merged_list.append(B[pB])
#     pB += 1

if pB < size_B: # B 배열에 아직 남은 값이 있으면
    merged_list += B[pB:size_B] # 남은 부분을 이어붙임

print(" ".join(map(str,merged_list)))   # 리스트를 문자열로 변환해서 공백 기준으로 출력