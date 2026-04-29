# 문제 유형: 정렬(Sorting) + 중복 제거(Deduplication)
# 사용 알고리즘: Python 내장 sort() (Timsort)
# 접근 방법:
# 1. 중복 제거를 위해 set 사용
# 2. set을 리스트로 변환
# 3. 정렬 기준:
#    - 1차: 문자열 길이 오름차순
#    - 2차: 길이가 같으면 사전순 정렬


import sys
# 빠른 입력을 위해 sys 모듈 사용

input = sys.stdin.readline
# input() 대신 빠른 입력 함수 사용

N = int(input())
# 단어의 개수 입력

words = set()
# 중복된 단어를 제거하기 위해 set 자료구조 사용
# set은 자동으로 중복을 허용하지 않음

for _ in range(N):
    word = input().strip()
    # 한 줄씩 단어를 입력받고 strip()으로 개행문자 제거
    
    words.add(word)
    # set에 단어 추가 (중복이면 자동으로 무시됨)

words = list(words)
# set은 순서가 없기 때문에 리스트로 변환

words.sort(key=lambda x: (len(x), x))
# 정렬 기준 설정:
# 1차: len(x) → 단어 길이 오름차순
# 2차: x → 길이가 같으면 사전순 정렬

for word in words:
    # 정렬된 단어들을 하나씩 순회
    
    print(word)
    # 한 줄씩 출력