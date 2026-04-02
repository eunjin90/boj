# for coin in coin_list[::-1]

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]

count = 0

for coin in coin_list[::-1]:  # 큰 동전부터
    if K == 0:
        break
    count += K // coin
    K %= coin

print(count)