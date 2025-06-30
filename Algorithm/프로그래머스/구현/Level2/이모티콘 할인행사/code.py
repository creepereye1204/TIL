from itertools import product
    
        
    
def solution(users, emoticons):
    answer=[0,0]
    E=len(emoticons)
    prod=(10,20,30,40)
    for discounts in product(prod,repeat=E):
        user_cnt = total_price = 0
        for user_d,user_p in users:
            user_price=0
            for emoticon,discount in zip(emoticons,discounts):
                if user_d<=discount:
                    user_price+=emoticon*(100-discount)//100
                    
            if user_p<=user_price:
                user_cnt+=1
            else:
                total_price+=user_price
        answer=max(answer,[user_cnt,total_price])
            
    return answer