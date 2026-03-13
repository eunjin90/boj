# 5. 주사위 세계

# 주사위 눈 3개를 비교해서 조건별로 상금을 계산
# 3개가 모두 같을 때 → 10,000 + (같은 눈) × 1,000
# 2개만 같을 때 → 1,000 + (같은 눈) × 100
# 모두 다를 때 → (가장 큰 눈) × 100

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    money = 10000 + a * 1000
elif a == b or a == c:
    money = 1000 + a * 100
elif b == c:
    money = 1000 + b * 100
else:
    money = a
    if b > money:
        money = b
    if c > money:
        money = c
    money = money * 100

print(money)

# a == b == c → 세 개 같음
# a == b or a == c → a와 다른 두 개 중 하나가 같음 → 2개 같음
# b == c → b와 c가 같음 → 2개 같음
# else → 모두 다름 → 가장 큰 값 * 100 (a,b,c중 가장 큰값구하기)