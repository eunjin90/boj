# 7. 오븐 시계

# 입력: 현재 시각 A시 B분, 요리 시간 C분
# 전체 분 계산 → total_min = B + C
# 추가 시 계산 → extra_hour = total_min // 60
# 분 → total_min % 60
# 시 → (A + extra_hour) % 24 (24시 넘어가면 0시로 돌아가기)

A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

# 분 계산
total_min = B + C
# 분 먼저 더하고
end_min = total_min % 60
# 60으로 나눈 몫을 시간에 더함


# 시간 계산
extra_hour = total_min // 60
end_hour = (A + extra_hour) % 24
# 시간은 24로 나눈 나머지를 사용하여 디지털 시계처럼 처리

print(end_hour, end_min)
