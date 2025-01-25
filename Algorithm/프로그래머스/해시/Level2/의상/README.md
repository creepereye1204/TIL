# 의상

## 📝 배운것

- Counter
- math.prod
- reduce

reduce 함수는 Python의 functools 모듈에 포함되어 있으며, 주어진 이터러블의 요소를 누적하여 하나의 결과를 생성하는 데 사용됩니다. 주로 두 개의 인자를 받아서 누적 계산을 수행합니다.

다음은 reduce 함수의 기본 사용법입니다.

기본 사용법
python

from functools import reduce

# 예: 리스트의 합을 구하는 경우

numbers = [1, 2, 3, 4]

# 합을 구하는 함수

def add(x, y):
return x + y

result = reduce(add, numbers)
print(result) # 출력: 10
예시: 리스트의 곱 구하기
python

from functools import reduce
from operator import mul

numbers = [1, 2, 3, 4]

# 곱을 구하는 경우

result = reduce(mul, numbers, 1)
print(result) # 출력: 24
예시: 문자열 연결하기
python

from functools import reduce

words = ["Hello", " ", "World", "!"]

# 문자열을 연결하는 경우

result = reduce(lambda x, y: x + y, words)
print(result) # 출력: Hello World!
요약
reduce는 이터러블의 요소를 두 개의 인자를 받아 누적하여 계산하는 데 유용합니다.
일반적으로 reduce와 함께 사용할 함수를 정의하거나, operator 모듈의 함수를 사용할 수 있습니다.
reduce를 사용할 때는 가독성을 고려하여 간단한 경우에만 사용하는 것이 좋습니다.

### collections 모듈의 Counter 사용법

해시 가능한 객체의 개수를 계산하고 이를 관리하는 데 사용됩니다. 주로 문자열이나 리스트에서 항목의 빈도를 세는 데 유용합니다.

`Counter` 생성자는 여러 형태의 데이터를 인자로 받는데요. 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 됩니다.

```python
Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})
```

```python
Counter("hello world")
# Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

`collections` 모듈의 `Counter` 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 시용할 수가 있습니다.
