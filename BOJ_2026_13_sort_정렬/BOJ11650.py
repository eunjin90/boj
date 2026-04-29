# 문제 유형: 정렬 (Sorting)
# 사용 알고리즘: Python 내장 sort() (Timsort)
# 접근 방법:
# 1. (x, y) 좌표를 리스트에 저장
# 2. sort()의 key를 사용하여
#    - 1차 기준: x좌표 오름차순
#    - 2차 기준: x가 같으면 y좌표 오름차순

import sys
# 빠른 입력을 위해 sys 모듈을 사용

input = sys.stdin.readline
# input() 대신 빠른 입력 함수 사용

N = int(input())
# 점의 개수 N을 입력받음

points = []
# 좌표 (x, y)를 저장할 리스트 생성

for _ in range(N):
    x, y = map(int, input().split())
    # 한 줄에서 x, y 좌표를 공백 기준으로 입력받고 정수로 변환
    
    points.append((x, y))
    # 튜플 형태로 좌표를 리스트에 저장
    # 예: (1, 2), (3, 4) 형태

points.sort()
# sort()는 기본적으로 튜플을 사전식(lexicographical)으로 정렬함
# 즉, (x, y) 기준으로 자동 정렬됨:
# 1차: x 오름차순
# 2차: x가 같으면 y 오름차순

for x, y in points:
    # 정렬된 리스트를 순회하면서
    
    print(x, y)
    # 각 점의 좌표를 한 줄씩 출력