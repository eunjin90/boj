# 5. 팩토리얼2

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

n = int(input())
result = 1  # 초기값 1로 설정, 0!도 1이므로 안전

for i in range(1, n+1):
    result *= i  # result = result * i

print(result)