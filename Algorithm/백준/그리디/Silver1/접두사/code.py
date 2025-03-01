# 일단 리스트로 시간 저장하고
# arr[1]번의 시간까지 set에 저장한다
# 이후 시작 시간 초과에 대하서는
# set에 있는지 arr[2]까지 들어가있는지 확인하고 결과 set에다가 저장
# 이후 길이 리턴
import sys

input = sys.stdin.readline
start, end, off = map(str, input().split(" "))
join = set()
rst = set()
try:
    while True:
        time, id = map(str, input().split(" "))
        if time <= start:
            join.add(id)
        elif end <= time <= off:
            if id in join:
                rst.add(id)
except:
    print(len(rst))
