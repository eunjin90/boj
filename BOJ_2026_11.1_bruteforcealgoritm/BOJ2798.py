# 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0 # 현재까지 찾은 가장 큰 합, 처음에는 아무것도 없으니까 0으로 시작

for i in range(N):  # i는 카드 인덱스
    for j in range(i + 1, N):   # 같은 카드 두 번 선택 방지
        for k in range(j + 1, N):   # 3장 모두 다른 카드
            total = cards[i] + cards[j] + cards[k]  # 선택된 3장의 합 계산

            if total <= M:  # M 이하만 인정
                if total > max_sum: # 지금 값이 더 크면 교체
                    max_sum = total

print(max_sum)


#=================================================================================

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

def findMax():
    max = 0
    for card1_index in range(N-2):
        for card2_index in range(card1_index+1, N-1):
            for card3_index in range(card2_index+1,N):
                sum = card_list[card1_index] + card_list[card2_index] + card_list[card3_index]
                if sum == M: return sum
                elif sum < M and sum > max:
                    max = sum
    return max
print(findMax())


