from math import ceil
from collections import defaultdict


def solution(fees, records):
    answer = []
    parkings = {}
    cars = defaultdict(int)
    default_time, default_price, div_time, div_price = fees

    for record in records:
        time, car, io = record.split(' ')
        hour, minute = map(int, time.split(':'))
        if io == "IN":
            parkings[car] = hour*60+minute
        else:
            cars[car] += hour*60+minute-parkings[car]
            del parkings[car]

    for car, time in parkings.items():
        cars[car] += 23*60+59-time

    for car_id in sorted(cars.keys()):

        answer.append(
            default_price+max(0, ceil((cars[car_id]-default_time)/div_time)*div_price))

    return answer
