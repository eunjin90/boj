# DP(다이나믹 프로그래밍) - 타뷸레이션(반복문 방식)
# 피보나치 수 4

n = int(input())    # 입력: 피보나치 수를 구할 n번째 값


# DP 테이블 생성
# table[0] = 0, table[1] = 1로 초기화
# 나머지는 0으로 채움
table = [0, 1] + [0] * (n - 1)

# 피보나치 점화식을 이용해 table 채우기
# 점화식: F(i) = F(i-1) + F(i-2)
for i in range(2, n + 1):
    
    table[i] = table[i-1] + table[i-2]  # 이전 두 값을 이용해 현재 값 계산

print(table[n]) # n번째 피보나치 수 출력