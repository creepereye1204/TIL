from dataclasses import dataclass


@dataclass
class Method:
    model: str
    warning: int
    change: int


arr = [Method('주먹구구식 모델', 1, 1), Method(
    '선형 순차적 모델', 20, 20), Method('진화적 프로세스 모델', 100, 100), Method('단계적 개발 모델', 50, 50), Method('통합 프로세스 모델', 50, 2), Method('애자일 프로세스 모델', 50, 100)]

print(sorted(arr, key=lambda x: x.warning))
