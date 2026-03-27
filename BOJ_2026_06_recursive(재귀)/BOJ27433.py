# 팩토리얼 2

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# factorial 을 recursive로 계산
def fact_r(N):
    # base condition
    if N <= 1:
        return 1
    
    # recursive composition -> combine
    return N * fact_r(N-1) # result = N * fact_r(N-1)

N = int(input())
print(fact_r(N))