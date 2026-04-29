# 문제 유형: 정렬(Sorting)
# 사용 알고리즘: Python 내장 sort() (Timsort)
# 접근 방법:
# 1. (x, y) 좌표를 리스트에 저장
# 2. sort()의 key를 사용하여
#    - 1차 기준: y좌표 오름차순
#    - 2차 기준: y가 같으면 x좌표 오름차순

import sys
# 빠른 입력을 위해 sys 모듈 사용

input = sys.stdin.readline
# input() 대신 빠른 입력 함수 사용

N = int(input())
# 점의 개수 입력

points = []
# 좌표를 저장할 리스트 생성

for _ in range(N):
    x, y = map(int, input().split())
    # 한 줄에서 x, y 좌표를 입력받아 정수로 변환
    
    points.append((x, y))
    # 좌표를 튜플 형태로 리스트에 저장

points.sort(key=lambda p: (p[1], p[0]))
# 정렬 기준 설정:
# 1차: y좌표 (p[1]) 오름차순
# 2차: x좌표 (p[0]) 오름차순
# → y가 같으면 x 기준으로 정렬됨

for x, y in points:
    # 정렬된 좌표를 하나씩 순회
    
    print(x, y)
    # 좌표를 공백으로 출력