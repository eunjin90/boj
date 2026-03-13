# 6. 삼격형 외우기

# 세 각 모두 60 → Equilateral
# 세 각 합이 180이고, 두 각이 같음 → Isosceles
# 세 각 합이 180이고, 같은 각 없음 → Scalene
# 세 각 합이 180이 아님 → Error

a = int(input())
b = int(input())
c = int(input())

total = a + b + c

if total != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")


# total != 180 → 삼각형이 될 수 없는 경우 (Error)
# a == b == c → 모두 같으면 정삼각형 (Equilateral)
# a == b or a == c or b == c → 두 각만 같으면 (Isosceles)
# 나머지 → 세 각 모두 다름 → (Scalene)

# 삼각형의 세 각을 보고 종류를 나누려면 세 각의 합이 180인지 알아야됨
# 합이 180이 아닌 경우도 먼저 조건을 만족하는 if/elif에 걸릴 수 있음