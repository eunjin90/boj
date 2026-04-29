# 문제 유형: 정렬(Sorting)
# 사용 알고리즘: Python 내장 sort() (Timsort)
# 접근 방법:
# 1. 학생 정보를 (이름, 국어, 영어, 수학) 형태로 저장
# 2. 정렬 기준을 key로 설정
# 3. 조건에 맞게 정렬 우선순위 구성:
#    - 국어: 내림차순 (-국어)
#    - 영어: 오름차순
#    - 수학: 내림차순 (-수학)
#    - 이름: 사전순 오름차순

import sys
# 빠른 입력을 위해 sys 모듈 사용

input = sys.stdin.readline
# input() 대신 빠른 입력 함수 사용

N = int(input())
# 학생 수 입력

students = []
# 학생 정보를 저장할 리스트

for _ in range(N):
    name, kor, eng, math = input().split()
    # 한 줄에서 이름과 3과목 점수를 입력받음
    
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    # 점수를 정수형으로 변환
    
    students.append((name, kor, eng, math))
    # 학생 정보를 튜플 형태로 저장

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 정렬 기준:
# 1차: 국어 점수 내림차순 (-x[1])
# 2차: 영어 점수 오름차순 (x[2])
# 3차: 수학 점수 내림차순 (-x[3])
# 4차: 이름 사전순 오름차순 (x[0])

for student in students:
    # 정렬된 학생 리스트를 순회
    
    print(student[0])
    # 이름만 출력

