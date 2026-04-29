# 정렬 문제 - 내장 정렬 함수(list.sort())를 사용한 풀이
# 사용 알고리즘: Sorting (Timsort - Python 내장 sort) Timsort 알고리즘 사용
# 분류: 구현 + 정렬
# 특징: 내장 sort()는 병합정렬 기반(Timsort)을 사용한 안정 정렬

import sys  # 파이썬의 표준 입력/출력을 더 빠르게 사용하기 위해 sys 모듈을 가져옴
input = sys.stdin.readline
# input() 대신 sys.stdin.readline을 사용하여 입력 속도를 빠르게 함
# (특히 입력이 많을 때 시간 초과를 방지하기 위해 사용)

N = int(input())  
# 첫 번째 줄에서 정수 하나를 입력받음
# 이 값은 정렬할 숫자의 개수 N을 의미함

arr = []    # 입력받은 숫자들을 저장할 빈 리스트를 생성
# 숫자를 저장할 리스트

# N번 반복하면서 숫자를 하나씩 입력받기 위한 반복문
# '_'는 반복 변수로 사용하지만 실제로는 사용하지 않겠다는 의미
for _ in range(N):

    # 한 줄씩 입력받은 값을 정수로 변환하여 리스트 arr에 추가
    # input()은 문자열로 입력되기 때문에 int()로 정수 변환을 해줌
    arr.append(int(input()))  
    # 한 줄씩 정수를 입력받아 리스트에 추가

arr.sort()  
# 리스트를 오름차순으로 정렬 (기본값: 오름차순)
# 리스트 arr를 오름차순으로 정렬
# 기본 정렬 방식은 오름차순이며, 내부적으로는 Timsort 알고리즘 사용

for num in arr: # 정렬된 리스트 arr를 처음부터 끝까지 하나씩 순회
    print(num)  
    # 정렬된 값을 한 줄씩 출력