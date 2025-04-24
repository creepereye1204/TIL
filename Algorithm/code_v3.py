import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 시드 고정
np.random.seed(42)

# x 데이터 생성 (10000, 9)
x = np.random.randint(-4, 4, size=(10000, 9))

# y 데이터 생성 및 분류 함수 정의


def classify_gambling_risk(y):
    risk_level = np.zeros_like(y, dtype=int)
    risk_level[y < 1] = 0  # 비문제
    risk_level[(y >= 1) & (y <= 2)] = 1  # 저위험도박
    risk_level[(y > 2) & (y <= 7)] = 2  # 중위험도박
    risk_level[y > 7] = 3  # 문제도박
    return risk_level


y = classify_gambling_risk(np.sum(x, axis=1, keepdims=True))

print("x 데이터 shape:", x.shape)
print("y 데이터 shape:", y.shape)

# 데이터 분할 (학습 데이터 80%, 테스트 데이터 20%)
train_size = int(0.8 * len(x))
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 로지스틱 회귀 모델 학습
model = LogisticRegression(
    random_state=42, solver='liblinear', multi_class='ovr')  # 모델 초기화 및 설정
model.fit(x_train, y_train.ravel())  # 학습 데이터로 모델 학습

# 모델 평가
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

# 정확도 계산
accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred_test)

print(f"Training Accuracy: {accuracy_train * 100:.2f}%")
print(f"Test Accuracy: {accuracy_test * 100:.2f}%")

print("Gambling Risk Levels:")
print("0 - 비문제")
print("1 - 저위험도박")
print("2 - 중위험도박")
print("3 - 문제도박")

# 사용자 입력 받기


def get_user_input():
    questions = [

    ]

    responses = []
    for question in questions:
        while True:
            try:
                response = int(input(question + " "))
                if response < 0 or response > 3:
                    raise ValueError("응답은 0에서 3 사이여야 합니다.")
                responses.append(response)
                break
            except ValueError as e:
                print(e)

    return responses


# 사용자 입력 받기
user_responses = get_user_input()

# 예측 수행
user_responses = np.array(user_responses).reshape(1, -1)  # 2D 배열로 변환
predicted_risk_level = model.predict(user_responses)

# 예측된 위험 레벨을 0부터 3까지의 값으로 출력
print(f"예측된 도박 위험 레벨: {predicted_risk_level[0]}")
