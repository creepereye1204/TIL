import heapq


def solution(jobs):
    answer, now, tasks, queue = 0, 0, [], []

    for i in range(len(jobs)):
        heapq.heappush(tasks, (jobs[i][0], jobs[i][1], i))

    while queue or tasks:

        while tasks:
            start, latent, idx = heapq.heappop(tasks)
            if now < start:
                heapq.heappush(tasks, (start, latent, idx))
                break
            heapq.heappush(queue, (latent, start, idx))

        if queue:
            latent, start, _ = heapq.heappop(queue)
            now += latent
            answer += now - start

            continue

        now = start

    return answer // len(jobs)
