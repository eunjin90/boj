# 문제 유형: 정렬(Sorting)
# 사용 알고리즘: Python 내장 sort() (Timsort)
# 접근 방법:
# 1. 모든 점수를 리스트에 저장
# 2. 점수를 오름차순 정렬
# 3. 뒤에서 k번째 값(= 상위 k명 중 가장 낮은 점수)을 출력

import sys
# 빠른 입력 처리를 위해 sys 모듈을 가져옴

input = sys.stdin.readline
# input() 대신 readline을 사용하여 입력 속도를 빠르게 함

N, k = map(int, input().split())
# 첫 줄 입력을 받아서 공백 기준으로 나눔
# N: 전체 학생 수
# k: 상을 받는 학생 수

scores = list(map(int, input().split()))
# 둘째 줄에서 학생들의 점수를 공백 기준으로 입력받아
# 정수 리스트로 변환하여 scores에 저장

scores.sort()
# 점수 리스트를 오름차순으로 정렬
# 가장 작은 점수부터 가장 큰 점수 순으로 정렬됨

# 정렬된 리스트에서 뒤에서 k번째 값이 커트라인이 됨
# 인덱스 기준으로는 -k 위치

print(scores[-k])
# 뒤에서 k번째 값을 출력
# 상위 k명 중 가장 낮은 점수 = 커트라인