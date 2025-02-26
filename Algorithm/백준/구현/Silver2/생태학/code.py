from collections import defaultdict
import sys

input = sys.stdin.read  # 전체 입력을 한 번에 읽기
dic = defaultdict(int)
total = 0

# 전체 입력을 한 번에 읽고 줄 단위로 나누기
lines = input().strip().splitlines()

for line in lines:
    dic[line] += 1
    total += 1

# 사전순으로 정렬하여 출력
for key in sorted(dic.keys()):
    percentage = dic[key] * 100 / total
    rounded_percentage = round(percentage, 4)  # 명시적으로 반올림
    print(f"{key.strip()} {rounded_percentage:.4f}")
