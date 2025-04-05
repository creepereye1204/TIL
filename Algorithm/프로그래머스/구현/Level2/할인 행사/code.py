def solution(wants, numbers, discounts):
    answer = 0

    for day in range(len(discounts)):
        shopping_bag = {}
        for want, number in zip(wants, numbers):
            shopping_bag[want] = number
        for i in range(10):
            try:
                if shopping_bag[discounts[day+i]] > 0:
                    shopping_bag[discounts[day+i]] -= 1
            except:
                pass
        if sum(shopping_bag.values()) == 0:
            answer += 1

    return answer
