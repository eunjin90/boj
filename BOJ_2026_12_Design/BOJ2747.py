# 재귀 + 다이나믹 프로그래밍(DP, 메모이제이션)
# 피보나치수

def fibo(num):

    # 종료 조건
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    # 아직 계산 안 된 경우
    if mem[num] == -1:
        # 계산해서 저장 (메모이제이션)
        mem[num] = fibo(num - 1) + fibo(num - 2)
    # 저장된 값 반환
    return mem[num]
# 입력
n = int(input())

# 메모이제이션 배열 (-1은 아직 계산 안 했다는 의미)
mem = [-1] * (n + 1)

print(fibo(n))