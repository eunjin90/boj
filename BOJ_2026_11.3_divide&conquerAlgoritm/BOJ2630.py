import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue

    # 현재 영역의 첫 번째 값
    color = paper[x][y]

    # 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                # 하나라도 다르면 4등분
                new_size = size // 2

                divide(x, y, new_size)                         # 좌상
                divide(x, y + new_size, new_size)              # 우상
                divide(x + new_size, y, new_size)              # 좌하
                divide(x + new_size, y + new_size, new_size)   # 우하
                return

    # 여기까지 왔다는 건 전부 같은 색
    if color == 0:
        white += 1
    else:
        blue += 1


# 전체 영역부터 시작
divide(0, 0, N)

print(white)
print(blue)