import pickle
import warnings
import numpy as np

warnings.filterwarnings("ignore", category=UserWarning)


def load_file(filename: str, d_type: str, encoding: str | None = 'utf-8') -> object:
    """파일을 로드합니다.
    Args:
        filename (str): 파일 이름
        d_type (str): 파일 유형 (예: 'rb' 또는 'rt')
    Returns: 로드된 파일 내용
    """
    try:
        with open(file='./static/'+filename, mode=d_type, encoding=encoding) as f:
            try:
                value = pickle.load(f)
            except Exception:
                lines = f.readlines()
                value = [line.strip() for line in lines]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{e}: 파일을 찾을 수 없습니다: {filename}")
    except Exception as e:
        raise ValueError(f"{e}: 오류 발생")
    return value


def get_user_input(questions: list, limit: int) -> np.array:
    """사용자에게 질문을 하고 응답을 받습니다.
    Args:
        questions (list): 질문 목록
        limit (int): 응답의 최대값
        Returns: np.array: 응답 배열"""
    responses = []
    for question in questions:

        response = int(input(question + " "))
        if response < 0 or response > limit:
            raise ValueError("응답은 0에서 {} 사이여야 합니다.".format(limit))
        responses.append(response)

    return np.array(responses).reshape(1, -1)


def predict(model: pickle, responses: list, answers: list, scaler: object | None = None) -> None:
    """모델을 사용하여 예측합니다.
    Args:
        model: 학습된 모델
        responses (np.array): 사용자 응답
        answers (list): 예측 결과에 대한 설명
    Returns: None"""
    try:
        if scaler:
            responses = scaler.transform(responses)
        prediction = model.predict(responses)[0]
        print("예측 결과:", answers[int(prediction)])
    except Exception as e:
        raise ValueError(f"{e}: 예측 중 오류 발생")
