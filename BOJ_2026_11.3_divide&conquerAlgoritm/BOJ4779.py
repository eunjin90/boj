# ========================================(N 기준)
def cantor(n):
    # 종료 조건: 더 이상 쪼갤 수 없는 단계
    # 길이가 1인 "-" 하나만 남음
    if n == 0:
        return "-"

    # 이전 단계 결과를 재귀적으로 가져옴
    prev = cantor(n - 1)

    # 가운데 공백은 이전 결과의 길이만큼 생성
    # (양쪽을 같은 길이로 유지하기 위해)
    space = " " * len(prev)

    # 왼쪽 + 공백 + 오른쪽 구조로 결합
    return prev + space + prev


while True:
    try:
        N = int(input())
        print(cantor(N))
    except:
        break

#=================================================================(size 기준)
import sys

def getCantor(size):
    # base condition # 종료 조건: 길이가 1이면 "-" 하나만 반환
    if size == 1: return '-'

    #divide
    # 현재 길이를 3등분
    new_size = size // 3

    # 가운데 부분은 공백으로 채움
    # (칸토어 집합에서 가운데를 제거하는 효과)
    center = ' ' * new_size

    # 왼쪽과 오른쪽은 재귀 호출로 생성
    side = getCantor(new_size)

    # 왼쪽 + 공백 + 오른쪽 구조로 결합
    return side + center + side

# 여러 줄 입력 처리 (EOF까지 계속 입력)
while True:
    try:
        # 각 줄마다 N 입력 받기
        N = int(input())

        # 전체 문자열 길이는 3^N
        size = 3 ** N

        # 칸토어 문자열 생성 후 출력
        result_str = getCantor(size)
        print(result_str)
    # 입력이 끝나면 반복 종료
    except EOFError:
        break

# total = map(int,sys.stdin.read().split('\n'))
# for N in total:
#     size = 3 ** N   # 길이 기준으로 쪼갬
#     result_str = getCantor(size)
#     print(result_str)