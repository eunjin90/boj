# 부녀회장이 될테야
# 전형적인 DP(다이나믹 프로그래밍)
t = int(input())    # 테스트 케이스 개수 입력

for _ in range(t):  # 각 테스트 케이스마다 반복

    # k층, n호 입력
    k = int(input())
    n = int(input())
    
    # DP 테이블 생성
    # dp[i][j] = i층 j호에 사는 사람 수
    # 크기: (k+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화
    # 규칙: 0층의 j호에는 j명이 산다
    for i in range(1, n + 1):
        dp[0][i] = i
    
    # ---------------------------
    # DP 점화식 채우기
    # 규칙:
    # dp[i][j] = dp[i][j-1] + dp[i-1][j]
    #
    # 의미:
    # 현재 층의 이전 호수 사람 수 +
    # 아래 층의 같은 호수 사람 수
    # ---------------------------
    for i in range(1, k + 1):       # 층 반복 (1층 ~ k층)
        for j in range(1, n + 1):   # 호수 반복 (1호 ~ n호)
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    print(dp[k][n]) # 결과 출력 (k층 n호)