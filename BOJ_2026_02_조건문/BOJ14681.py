# 4. 사분면 고르기

# x, y의 부호를 보고 사분면을 판단
# 제1사분면: x > 0, y > 0
#   점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면
# 제2사분면: x < 0, y > 0
#   점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면
# 제3사분면: x < 0, y < 0
#   점 C는 x좌표가 음수이고 y좌표가 음수이므로 제3사분면
# 제4사분면: x > 0, y < 0
#   점 D는 x좌표가 양수이고 y좌표가 음수이므로 제4사분면

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:  # x > 0 and y < 0
    print(4)