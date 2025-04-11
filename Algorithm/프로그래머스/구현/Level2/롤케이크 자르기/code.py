from collections import Counter,defaultdict
def solution(toppings):
    answer = 0
    bro=Counter(toppings)
    me=defaultdict(int)
    for topping in toppings:
        me[topping]=1
        bro[topping]-=1
        if bro[topping]<1:
            del bro[topping]
        if len(bro.keys())>len(me.keys()):
            pass
        elif len(bro.keys())==len(me.keys()):
            answer+=1
        else:
            break
    
    return answer