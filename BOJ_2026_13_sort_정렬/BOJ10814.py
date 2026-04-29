# 문제 유형: 정렬(Sorting)
# 사용 알고리즘: Python 내장 sort() (Timsort, 안정 정렬)
# 접근 방법:
# 1. 회원 정보를 (나이, 이름) 형태로 리스트에 저장
# 2. 입력 순서를 유지한 상태에서 정렬 수행
# 3. 정렬 기준:
#    - 1차: 나이 오름차순
#    - 2차: 나이가 같으면 입력 순서 유지 (stable sort 활용)

import sys
# 빠른 입력을 위해 sys 모듈 사용

input = sys.stdin.readline
# input() 대신 빠른 입력 함수 사용

N = int(input())
# 회원 수 입력

members = []
# 회원 정보를 저장할 리스트 생성

for i in range(N):
    age, name = input().split()
    # 한 줄에서 나이와 이름을 공백 기준으로 입력받음
    
    age = int(age)
    # 나이를 정수로 변환
    
    members.append((age, i, name))
    # (나이, 입력순서, 이름) 형태로 저장
    # i는 가입 순서를 나타냄

members.sort(key=lambda x: (x[0], x[1]))
# 정렬 기준:
# 1차: 나이 (x[0]) 오름차순
# 2차: 가입 순서 (x[1]) 오름차순
# → 나이가 같을 경우 먼저 가입한 사람이 앞에 오도록 보장

for age, _, name in members:
    # 정렬된 결과를 순회하면서 출력
    
    print(age, name)
    # 나이와 이름을 공백으로 출력