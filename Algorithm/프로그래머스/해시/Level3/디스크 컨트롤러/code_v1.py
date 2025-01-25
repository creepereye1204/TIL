import heapq


def solution(jobs):
    l = len(jobs)
    answer = 0
    tasks = []
    queue = []
    for i in range(len(jobs)):
        heapq.heappush(tasks, (jobs[i][0], jobs[i][1], i))

    time = 0
    job = None
    end = 0
    while queue or tasks:

        if end == time:
            while tasks:
                start, latent, idx = heapq.heappop(tasks)
                if time >= start:
                    heapq.heappush(queue, (latent, start, idx))
                else:
                    heapq.heappush(tasks, (start, latent, idx))
                    break

            if queue:
                latent, start, idx = heapq.heappop(queue)
                if time > start:
                    answer += time - start + latent
                elif time == start:
                    answer += latent

                end = time + latent

        time += 1

    return answer // l
