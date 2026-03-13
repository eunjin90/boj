# 10. 초코바

# 밤고가 초코바를 살 수 있으면 Yes를, 없으면 No를 출력한다.

# 밤고가 가진 돈 = 100원 × N
# 가진 돈이 M보다 크거나 같으면 Yes, 아니면 No

N, M = input().split()

N = int(N)
M = int(M)

money = N * 100

if money >= M:
    print("Yes")
else:
    print("No")