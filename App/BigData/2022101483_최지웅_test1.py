import pandas as pd
import requests
import bs4

URL = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
HEADERS = {
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
try:

    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    data_list = []
    country_list = set()
    for value in soup.find_all('option'):

        country = value.text.strip().split(' ')
        country = country[0] + ' ' + country[2]
        sale = value.get('value')

        if country and sale is not None and country != '대한민국 KRW' and country not in country_list:
            data_list.append({'국가명': country, '환율': sale})
            country_list.add(country)

    df = pd.DataFrame(data_list)

    print(df.head(10))
    df.to_csv('환율정보.csv', encoding='utf-8-sig', index=False)

except requests.exceptions.RequestException as e:
    print(f"웹 페이지 요청 중 오류 발생: {e}")
except Exception as e:
    print(f"데이터 처리 중 오류 발생: {e}")
