def cal(text,toggle):
    mid=int(len(text)/2)
    a=text[:mid]
    b=text[mid:][::-1]
    
    if a==b:
        if toggle:
            print(0)
            
        else:
            print(1)
        return True
    else:
        if len(a)!=len(b):
            
    return False
    
for _ in range(int(input())):
    text='Uf'*300000
    
    if cal(text,True):
        continue
    
    else:
        
        toggle=False
        for i in range(len(text)):
            temp=text[:i]+text[i+1:]
            
            toggle=cal(temp,False)
            if toggle:
                break
    if not toggle:
        print(2)
    