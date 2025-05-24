import pandas as pd


# 1.

file_path = r'c:\python_work\sungjuk.csv'
try:
    df = pd.read_csv(file_path)
    print("1. sungjuk.csv 파일을 성공적으로 읽어왔습니다.")
    print(df.head(11))  # 데이터프레임의 처음 5행을 출력하여 확인합니다.
    print("-" * 30)
except FileNotFoundError:
    print(f"오류: {file_path} 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    exit()  # 파일이 없으면 스크립트 종료

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

# 이후 작업은 3번 결과로 나온 df_cleaned_step3를 기준으로 진행합니다.
df = df_cleaned_step3.copy()  # 작업의 일관성을 위해 변수명을 다시 df로 사용합니다.

# 4. 행 방향으로 2개 이상의 NULL 값이 있는 데이터를 모두 삭제하시오.
# 각 행의 결측치 개수를 세고, 2개 이상인 행을 필터링하여 삭제합니다.
# 결측치가 (총 컬럼 개수 - 1)개 이하인 행만 남깁니다.
df_cleaned_step4 = df.dropna(thresh=len(df.columns) - 1)
print("4. 행 방향으로 2개 이상의 NULL 값이 있는 데이터를 모두 삭제했습니다.")
print("삭제 후 데이터프레임 정보:")
print(df_cleaned_step4)
print("-" * 30)

# 이후 작업은 4번 결과로 나온 df_cleaned_step4를 기준으로 진행합니다.
df = df_cleaned_step4.copy()

# 5. 'math' 과목에 모두 0 값으로 채워넣으시오.
# 이전에 3번/4번에서 'math' 컬럼의 결측치는 이미 삭제되었으므로, 이 단계는 추가적인 결측치가 발생했을 경우에 유효합니다.
# 만약 3번/4번 단계에서 'math' 결측치가 모두 제거되지 않았다면 이 코드는 동작합니다.
# 또는 결측치 채우기 전에 삭제를 하는 방식이라면, 순서가 바뀌어야 할 수 있습니다.
# 문제의 순서대로 진행하면 3, 4에서 결측치를 먼저 삭제하고 5에서 채우므로, 5번은 사실상 효과가 없을 수 있습니다.
# 만약 결측치를 먼저 채우고 삭제하는 순서라면 아래 코드는 유효합니다.
# 문제의 순서를 따르되, 만약 새로운 결측치가 생겼거나 의도적으로 math에 0을 채워야 한다면 사용합니다.
df['math'] = df['math'].fillna(0)
print("5. 'math' 컬럼의 결측치(있었다면)를 0으로 채워넣었습니다.")
print(df['math'].head())
print("-" * 30)


# 6. 'kor','eng', 'math' 세 과목 모두 정수 처리하시오.
# 결측치 처리가 완료된 후에 정수형으로 변환합니다.
# pd.NA가 아닌 np.nan으로 결측치가 표시되어 있고, 결측치가 없다면 astype(int)를 바로 사용 가능합니다.
# 만약 결측치 처리 후에도 NaN이 남아있다면, Int64 (pandas의 nullable integer) 타입을 사용해야 합니다.
try:
    df['kor'] = df['kor'].astype(int)
    df['eng'] = df['eng'].astype(int)
    df['math'] = df['math'].astype(int)
    print("6. 'kor', 'eng', 'math' 컬럼을 정수형으로 변환했습니다.")
    print(df.dtypes)  # 변환된 데이터 타입 확인
    print("-" * 30)
except ValueError as e:
    print(
        f"오류: 정수형 변환 중 문제가 발생했습니다. 결측치가 남아있거나 숫자로 변환할 수 없는 값이 있는지 확인해주세요. 오류: {e}")
    # 필요하다면 df['kor'] = df['kor'].astype('Int64') 와 같이 Nullable Integer 사용 고려

# 7. 인덱스 번호를 순서대로 재설정하시오.
df_reset_index = df.reset_index(drop=True)  # 기존 인덱스는 삭제하고 새로운 인덱스 생성
print("7. 인덱스 번호를 순서대로 재설정했습니다.")
print(df_reset_index.head())
print("-" * 30)

# 이후 작업은 7번 결과로 나온 df_reset_index를 기준으로 진행합니다.
df = df_reset_index.copy()

# 8. 8번 인덱스 위치에 아래 데이터를 삽입하시오.
new_data = {'이름': '이은비', 'kor': 60,
            'eng': 90, 'math': 0}  # 삽입할 데이터
new_row_df = pd.DataFrame([new_data])  # 삽입할 데이터를 데이터프레임 형태로 만듭니다.

# 데이터를 특정 인덱스 위치에 삽입하기 위해서는 concat을 사용하거나,
# iloc을 사용하여 특정 위치에 행을 삽입하는 방식을 사용할 수 있습니다.
# 여기서는 concat을 사용하여 데이터프레임을 분리하고 합치는 방법을 사용합니다.
df_part1 = df.iloc[:8]  # 8번 인덱스 (9번째 행) 전까지
df_part2 = df.iloc[8:]  # 8번 인덱스 (9번째 행) 부터 끝까지

df_inserted = pd.concat([df_part1, new_row_df, df_part2],
                        ignore_index=True)  # 데이터 합치고 인덱스 재설정

print("8. 8번 인덱스 위치에 새로운 데이터를 삽입했습니다.")
print(df_inserted.iloc[7:10])  # 삽입된 위치 주변 데이터 확인
print("-" * 30)

# 최종 결과 데이터프레임
df_final = df_inserted
print("\n최종 결과 데이터프레임:")
print(df_final)


print("-"*30)

# 9. 중복 데이터가 있는지 조회하시오.
print("9. 중복 데이터 조회 결과:")
# 모든 컬럼을 기준으로 중복된 행을 찾습니다.
duplicate_rows = df_final[df_final.duplicated()]
print(duplicate_rows)
if duplicate_rows.empty:
    print("-> 중복된 데이터가 없습니다.")
print("-" * 30)

# 10. 중복된 데이터 중 첫 번째 조회되는 중복 데이터는 유지하고 그 이후 중복되는 데이터를 삭제하시오.
# keep='first' 옵션을 사용하여 첫 번째 나타나는 중복을 제외한 나머지를 삭제합니다.
df_no_duplicates = df_final.drop_duplicates(keep='first')
print("10. 중복 데이터 중 첫 번째 데이터를 제외하고 삭제했습니다.")
print("중복 삭제 후 데이터프레임:")
print(df_no_duplicates)
print("-" * 30)

# 이후 작업은 10번 결과로 나온 df_no_duplicates를 기준으로 진행합니다.
df = df_no_duplicates.copy()

# 11. 데이터가 없는 ‘math’ 열을 삭제해주세요.
# 'math' 열을 삭제합니다. axis=1은 열 방향 삭제를 의미합니다.
df_no_math = df.drop('math', axis=1)
print("11. 'math' 열을 삭제했습니다.")
print("math 열 삭제 후 데이터프레임:")
print(df_no_math)
print("-" * 30)

# 이후 작업은 11번 결과로 나온 df_no_math를 기준으로 진행합니다.
df = df_no_math.copy()

# 12. 두 과목 중 한 과목이라도 0점인 과목은 삭제해 주세요.
# 'kor' 또는 'eng' 컬럼의 값이 0인 행을 찾아서 삭제합니다.
# 'kor'이 0이거나 'eng'이 0인 행을 선택합니다.
zero_score_rows = df[(df['kor'] == 0) | (df['eng'] == 0)]

# 해당 조건을 만족하는 행을 삭제합니다.
# keep='false' 옵션처럼 조건을 만족하는 행을 삭제하려면 인덱스를 사용하여 삭제해야 합니다.
# 조건을 만족하지 않는 행들만 선택하는 방식으로 구현하는 것이 일반적입니다.
df_no_zero_scores = df[~((df['kor'] == 0) | (df['eng'] == 0))].copy()
# ~는 조건을 반전시킵니다. 즉, 'kor'이 0이 아니고 'eng'도 0이 아닌 행만 선택합니다.

print("12. 'kor' 또는 'eng' 점수가 0점인 행을 삭제했습니다.")
print("0점 데이터 삭제 후 데이터프레임:")
print(df_no_zero_scores)
print("-" * 30)

# 이후 작업은 12번 결과로 나온 df_no_zero_scores를 기준으로 진행합니다.
df = df_no_zero_scores.copy()

# 13. ‘kor’ 과목이 60점 이하인 경우 65점으로 데이터를 상향 조정해 주세요.
# 'kor' 컬럼의 값이 60 이하인 조건을 사용하여 값을 65로 변경합니다.
df.loc[df['kor'] <= 60, 'kor'] = 65
print("13. 'kor' 과목이 60점 이하인 데이터를 65점으로 상향 조정했습니다.")
print("kor 점수 조정 후 데이터프레임:")
print(df)
print("-" * 30)

# 14. 순위를 부여하시오. 단, 순위는 kor+eng 점수에 대해 점수가 높은 순으로 순위를 부여 하시오.
# 'kor'과 'eng' 점수를 합하여 'total' 컬럼을 생성합니다.
df['total'] = df['kor'] + df['eng']

# 'total' 컬럼을 기준으로 순위를 부여합니다.
# method='dense': 동일한 값을 가진 항목에는 동일한 순위를 부여하고, 다음 순위는 중복된 순위의 다음 번호로 부여합니다. (예: 1, 2, 2, 3)
# ascending=False: 높은 점수가 더 높은(낮은 숫자의) 순위를 갖도록 내림차순으로 순위를 매깁니다.
df['rank'] = df['total'].rank(method='dense', ascending=False).astype(int)
print("14. 'kor' + 'eng' 점수 합계에 대해 높은 순으로 순위를 부여했습니다.")
print("순위 부여 후 데이터프레임:")
print(df)
print("-" * 30)

# 15. 성적이 우수한 성적 순위 기준으로 정렬하시오.
# 'rank' 컬럼을 기준으로 오름차순 정렬합니다.
df_sorted = df.sort_values(by='rank', ascending=True)
print("15. 성적 순위(rank) 기준으로 데이터프레임을 정렬했습니다.")
print("순위 정렬 후 최종 데이터프레임:")
print(df_sorted)
print("-" * 30)

# 최종 결과 데이터프레임
df_final_processed = df_sorted
print("\n최종 처리 완료된 데이터프레임:")
print(df_final_processed)
