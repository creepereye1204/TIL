from collections import Counter
import sys
def s1(strs):
    arr=[]
    strs=strs.lower()
    for index in range(len(strs)-1):
        if strs[index:index+2].isalpha():
            arr.append(strs[index:index+2])
    return Counter(arr),set(arr)
def solution(str1, str2):
    A,a=s1(str1)
    B,b=s1(str2)
    C=a&b
    D=a|b
    x=y=0
    for c in C:
        mn=sys.maxsize
        if c in A:
            mn=min(mn,A[c])
        if c in B:
            mn=min(mn,B[c])
        x+= mn if mn!=sys.maxsize else 0
    
    for d in D:
        mx=-sys.maxsize
        if d in A:
            mx=max(mx,A[d])
        if d in B:
            mx=max(mx,B[d])
        y+= mx if mx!=-sys.maxsize else 0
    
    try:
        
        return int((x/y)*65536)
    except:
        return 65536