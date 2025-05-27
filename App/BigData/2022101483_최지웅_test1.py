import pandas as pd

# 1.
file_path = r'c:\python_work\sungjuk.csv'
try:
    df = pd.read_csv(file_path)
    print("1. sungjuk.csv 파일을 성공적으로 읽어왔습니다.")
    print(df.head(11))
    print("-" * 30)
except FileNotFoundError:
    print(f"오류: {file_path} 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    exit()

# 2.
print("2. 결측치 값 조회 결과:")
print(df.isnull().sum())
print("-" * 30)

# 3.
df_cleaned_step3 = df.dropna(subset=['kor', 'eng', 'math'])
print("3. 'kor', 'eng', 'math' 컬럼에 결측치가 있는 행을 삭제했습니다.")
print("삭제 후 데이터프레임 정보:")
print(df_cleaned_step3)
print("-" * 30)


# 4.
df_cleaned_step4 = df.dropna(thresh=len(df.columns) - 1)
print("4. 행 방향으로 2개 이상의 NULL 값이 있는 데이터를 모두 삭제했습니다.")
print("삭제 후 데이터프레임 정보:")
print(df_cleaned_step4)
print("-" * 30)


df = df_cleaned_step4.copy()

# 5.
df['math'] = 0
print("5. 'math' 를 0으로 채워넣었습니다.")
print(df)
print("-" * 30)


# 6.
try:
    df['kor'] = df['kor'].astype(int)
    df['eng'] = df['eng'].astype(int)
    df['math'] = df['math'].astype(int)
    print("6. 'kor', 'eng', 'math' 컬럼을 정수형으로 변환했습니다.")
    print(df)
    print("-" * 30)
except ValueError as e:
    print(
        f"오류: 정수형 변환 중 문제가 발생했습니다. 오류: {e}")


# 7.
df_reset_index = df.reset_index(drop=True)
print("7. 인덱스 번호를 순서대로 재설정했습니다.")
print(df_reset_index)
print("-" * 30)


df = df_reset_index.copy()

# 8.
new_data = {'name': '이은비', 'kor': 60,
            'eng': 90, 'math': 0}
new_row_df = pd.DataFrame([new_data])
df_part1 = df.iloc[:8]
df_part2 = df.iloc[8:]

df_inserted = pd.concat([df_part1, new_row_df, df_part2],
                        ignore_index=True)

print("8. 8번 인덱스 위치에 새로운 데이터를 삽입했습니다.")
print(df_inserted.iloc[7:10])
print("-" * 30)


df_final = df_inserted
print(df_final)
print("-"*30)

# 9.
print("9. 중복 데이터 조회 결과:")

duplicate_rows = df_final[df_final.duplicated(keep=False)]
print(duplicate_rows)
if duplicate_rows.empty:
    print("-> 중복된 데이터가 없습니다.")
print("-" * 30)

# 10.
df_no_duplicates = df_final.drop_duplicates(keep='first')
print("10. 중복 데이터 중 첫 번째 데이터를 제외하고 삭제했습니다.")
print("중복 삭제 후 데이터프레임:")
print(df_no_duplicates)
print("-" * 30)


df = df_no_duplicates.copy()

# 11.
df_no_math = df.drop('math', axis=1)
print("11. 데이터가 없는(0인) 'math' 열을 삭제했습니다.")
print("math 열 삭제 후 데이터프레임:")
print(df_no_math)
print("-" * 30)

df = df_no_math.copy()

# 12.
zero_score_rows = df[(df['kor'] == 0) | (df['eng'] == 0)]

df_no_zero_scores = df[~((df['kor'] == 0) | (df['eng'] == 0))].copy()


print("12. 'kor' 또는 'eng' 점수가 0점인 행을 삭제했습니다.")
print("0점 데이터 삭제 후 데이터프레임:")
print(df_no_zero_scores)
print("-" * 30)


df = df_no_zero_scores.copy()

# 13.
df.loc[df['kor'] <= 60, 'kor'] = 65
print("13. 'kor' 과목이 60점 이하인 데이터를 65점으로 상향 조정했습니다.")
print("kor 점수 조정 후 데이터프레임:")
print(df)
print("-" * 30)

# 14.
df['total'] = df['kor'] + df['eng']

df['rank'] = df['total'].rank(method='dense', ascending=False).astype(int)
print("14. 'kor' + 'eng' 점수 합계에 대해 높은 순으로 순위를 부여했습니다.")
print("순위 부여 후 데이터프레임:")
print(df)
print("-" * 30)

# 15.
df_sorted = df.sort_values(by='rank', ascending=True)
print("15. 성적 순위(rank) 기준으로 데이터프레임을 정렬했습니다.")
print("순위 정렬 후 최종 데이터프레임:")
print(df_sorted.drop(columns=['total']))
print("-" * 30)
