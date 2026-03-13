# 14. 나는 행복합니다~

# 번호 K가 몇 번째 줄(N) 몇 번째 칸(M)에 있는지 찾는다
# 한 줄에 M개씩 번호가 증가

# 줄 번호(n) → K // M
# 칸 번호(m) → K % M

N, M, K = input().split()

N = int(N)
M = int(M)
K = int(K)

n = K // M
m = K % M

print(n, m)