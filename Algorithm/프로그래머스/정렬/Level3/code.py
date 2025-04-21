def solution(operations):
    queue = []
    while operations:
        operation = operations.pop(0)
        op, val = operation.split(' ')
        if op == 'I':
            queue.append(int(val))
        else:
            if queue:
                queue.sort()
                if val == '-1':
                    queue.pop(0)
                else:
                    queue.pop()

    return [max(queue), min(queue)] if queue else [0, 0]
