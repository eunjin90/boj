# 8. 알람 시계

# 알람을 45분 앞당기는 계산

H, M = input().split()
H = int(H)
M = int(M)
# 근이가 설정한 알람 시간 H시 M분

if M >= 45:
    M = M - 45
else:
    M = M + 60 - 45  # 45분 빼기
    H = H - 1         # 한 시간 빼기
    if H < 0:         # 0시 전이면 23시로
        H = 23

print(H, M)