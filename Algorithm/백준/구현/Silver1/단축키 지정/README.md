## 피드백

- 리스트나 문자열을 수정할 때는 인덱스로 값에 접근하자

- 문자열은 불변(immutable) 타입이기 때문에 직접 수정할 수 없다.

예시 코드
python

# 문자열 리스트

vocas = ["apple", "banana", "cherry"]

# 잘못된 접근 - 직접 수정하려고 시도

for voca in vocas:
voca[0] = voca[0].upper() # 오류 발생: 'str' object does not support item assignment

# 올바른 접근 - 새 문자열로 업데이트

for i in range(len(vocas)):
vocas[i] = vocas[i][0].upper() + vocas[i][1:] # 첫 글자를 대문자로 변경

print(vocas) # 결과: ['Apple', 'Banana', 'Cherry']
설명
잘못된 접근:

voca[0] = voca[0].upper()와 같이 문자열의 특정 인덱스를 직접 수정하려고 하면 오류가 발생합니다. 문자열은 불변 타입이기 때문에 이렇게 수정할 수 없습니다.
올바른 접근:

vocas[i] = vocas[i][0].upper() + vocas[i][1:]와 같이 새 문자열을 만들어서 vocas 리스트의 해당 인덱스에 할당합니다. 이 방법은 문자열의 첫 글자를 대문자로 변경하는 올바른 방법입니다.
