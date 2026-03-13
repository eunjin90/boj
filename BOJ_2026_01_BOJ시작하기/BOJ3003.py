# 15. 킹, 퀸, 룩, 비숍, 나이트, 폰

# 체스의 정상 개수는 이미 정해져있다
    #(킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성)
# 정상 개수 - 입력 개수를 하면 됨

k, q, r, b, n, p = input().split()

k = int(k)
q = int(q)
r = int(r)
b = int(b)
n = int(n)
p = int(p)

print(1 - k, 1 - q, 2 - r, 2 - b, 2 - n, 8 - p)