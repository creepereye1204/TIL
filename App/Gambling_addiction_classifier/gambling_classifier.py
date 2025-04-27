# -*- coding: utf-8 -*-


if __name__ == "__main__":
    try:
        from src.job import Classifier
    except ImportError:
        print("모듈을 찾을 수 없습니다. 모듈을 확인하세요.")
        exit(0)

    params = {"model": ["gamble_model.pkl", "rb", None],
              "questions": ["gamble_questions.txt", "rt"],
              "answers": ["gamble_answers.txt", "rt"],
              "limit": 3,
              }
    Classifier.run(**params)
