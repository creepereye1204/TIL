from collections import deque
import requests
import bs4
user = input().strip()
limit = int(input())

actions = ('ing', 'ers')
HEADERS = {
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
for action in actions:
    queue = deque([(user, 0)])
    visited = set([user])
    try:
        while queue:
            friend, gen = queue.popleft()

            if gen >= limit:
                break
            print(f'{gen}:', friend)
            URL = f'https://github.com/{friend}?tab=follow{action}'
            response = requests.get(URL, headers=HEADERS)
            response.raise_for_status()

            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            for tag in soup.find_all('span', class_='Link--secondary'):
                friend = tag.get_text(strip=True)
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, gen+1))
    except requests.exceptions.RequestException as e:
        print(f"웹 페이지 요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"데이터 처리 중 오류 발생: {e}")
