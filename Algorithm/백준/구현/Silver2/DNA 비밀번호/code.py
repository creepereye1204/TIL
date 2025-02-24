# 우선 처음에는 딕셔너리로 알파벳의 개수를 초기화 시켜둬
# 그리고 처음 윈도우를 움직일때는 문자열의전체를 체크해서 딕셔너리에 저장시켜 그리고 이동할때마다
# 윈도우크기의 첫번째 부분을 롤백하고 마지막부분으로 하나씪 업데이트해가면서 딕셔너리가 0보다 작거나 같을떄만 cnt+=1

s, p = map(int, input().split(" "))
dna = input()
rst = 0
arr = list(map(int, input().split(" ")))
dic = {}
dic["A"] = arr[0]
dic["C"] = arr[1]
dic["G"] = arr[2]
dic["T"] = arr[3]


def check(dic):
    global rst

    if all(v <= 0 for v in dic.values()):
        rst += 1


def slide(start, end):
    global s, p, arr
    dic[dna[start]] += 1
    dic[dna[end]] -= 1
    check(dic)


for i in range(p):

    dic[dna[i]] -= 1
check(dic)  # 이거 때문에 틀림...

for i in range(1, s - p + 1):
    slide(i - 1, i + p - 1)
print(rst)
