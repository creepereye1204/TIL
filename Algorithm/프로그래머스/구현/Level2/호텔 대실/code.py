import heapq


def convert(time):
    return 60*int(time[:2])+int(time[3:])


def solution(book_time):
    answer = 0
    rooms = []
    books = [[convert(start), convert(end)] for start, end in book_time]
    books.sort(key=lambda x: x[0])

    for i in range(len(books)):
        if rooms:
            if rooms[0]+10 <= books[i][0]:
                heapq.heappop(rooms)
        heapq.heappush(rooms, books[i][1])
        answer = max(answer, len(rooms))

    return answer
