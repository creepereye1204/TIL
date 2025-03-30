dictCapital = {
    "Japan": "도쿄",
    "Italy": "로마",
    "England": "런던",
    "Korea": "서울",
    "Canada": "오타와"
}

country = input('검색 국가는 ').capitalize()
try:
    print(f'전체 검색 대상 국가 수는 {len(dictCapital.keys())}개 국가이며,')
    print(f'{country} 수도는 {dictCapital[country]}입니다.')
except:
    print(f'{country}는 존재하지 않는 국가입니다.')
