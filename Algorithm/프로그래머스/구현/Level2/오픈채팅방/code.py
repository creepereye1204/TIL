def solution(records):
    answer = []
    users = {}
    for record in records:
        command, *arr = record.split(' ')
        if command == 'Enter':
            answer.append((arr[0], '님이 들어왔습니다.'))
            users[arr[0]] = arr[1]
        elif command == 'Leave':
            answer.append((arr[0], '님이 나갔습니다.'))
        else:
            users[arr[0]] = arr[1]
    return [f'{users[user]}{command}' for user, command in answer]
