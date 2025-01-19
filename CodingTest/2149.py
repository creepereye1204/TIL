k1=list(input())
n=input()
k2=sorted(k1)
length=len(n) //len(k1)
arr=[(k2[i],n[i*length:(1+i)*length]) for i in range(len(k1))]
res=''

for k in k1:
    for j in range(len(arr)):
        if arr[j][0]==k:
            res+=arr[j][1]
            arr.pop(j)
            break

for i in range(length):
    for j in range(len(k1)):
        print(res[j*length+i],end='')