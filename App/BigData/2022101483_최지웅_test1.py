import pandas as pd
import numpy as np

df = pd.DataFrame({
    '이름': ['박보검', '아이유', '김선호', '이수경', '이준영', '박해준'],
    '나이': [33, 32, 36, 25, 27, 45],
    '신장': [183, 165, 180, 165, 178, 180],
    '체중': [75, 55, 74, 58, 72, 78],
    '혈액형': ['A', 'B', 'B', 'O', 'AB', 'B']
})

new_data = pd.DataFrame(
    {'이름': '김용림', '나이': 86, '신장': 162, '체중': 75, '혈액형': 'AB'}, index=[6])

df = pd.concat([df, new_data])

df['소속사'] = ['SM', '쿠팡', '카카오', 'SM', 'JYP', 'SM', '무소속']

df.rename(columns={'이름': '이  름'}, inplace=True)
results = [list(df.columns)]+list(map(list, df.values))
for result in results:
    print('\t'.join(map(str, result)))
print('='*49)
print(f'A형 인원수: {len(df[df["혈액형"] == "A"])}명')
print(f'AB형 인원수: {len(df[df["혈액형"] == "AB"])}명')
print(f'B형 인원수: {len(df[df["혈액형"] == "B"])}명')
print(f'O형 인원수: {len(df[df["혈액형"] == "O"])}명')
print(f'평균 나이={np.average(df["나이"]):.2f}세')
print(f'평균 신장={np.average(df["신장"]):.2f}cm')
print(f'평균 체중={np.average(df["체중"]):.2f}kg')
