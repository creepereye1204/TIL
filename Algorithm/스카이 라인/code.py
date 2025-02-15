# # from bintrees import FastRBTree
# # from functools import lru_cache


# # class RBTreeSkyLine(FastRBTree):
# #     def __init__(self):
# #         super().__init__()

# #     @lru_cache(maxsize=None)  # 무제한 캐시
# #     def _find_below_and_above(value):
# #         below = tree.floor_key(value)
# #         above = tree.ceiling_key(value)

# #         return below, above

# #     def insert(self, key, value):


# # # 특정 값의 바로 아래 및 위 값을 찾는 함수
# # @lru_cache(maxsize=None)  # 무제한 캐시
# # def find_below_and_above(value):
# #     below = tree.floor_key(value)
# #     above = tree.ceiling_key(value)

# #     return below, above


# # # 트리 생성
# # tree = FastRBTree()

# # N = 10**3

# # # 트리에 값 삽입
# # for index in range(N):
# #     tree.insert(index, "value1")
# from bintrees import FastRBTree

# # 두 개의 트리 생성
# tree_by_a = FastRBTree()  # a를 기준으로
# tree_by_b = FastRBTree()  # b를 기준으로


# # 데이터 삽입
# def insert(a, b, value):
#     tree_by_a.insert(a, (b, value))
#     tree_by_b.insert(b, (a, value))


# # 데이터 추가
# insert(10, 20, "값 1")
# insert(5, 25, "값 2")
# insert(15, 30, "값 3")


# # a 기준으로 검색
# def search_by_a(a):
#     return tree_by_a.get(a)


# # b 기준으로 검색
# def search_by_b(b):
#     return tree_by_b.get(b)


# # 사용 예시
# result_a = search_by_a(10)
# print(f"a=10인 결과: {result_a}")

# result_b = search_by_b(20)
# print(f"b=20인 결과: {result_b}")
from typing import List, Tuple
import bisect


class SkylineQuery:
    def __init__(self):
        # 현재까지의 스카이라인 포인트들을 저장
        # y좌표를 기준으로 정렬된 상태 유지
        self.skyline_points: List[Tuple[int, int]] = []

    def is_dominated(self, point: Tuple[int, int]) -> bool:
        """
        주어진 점이 현재 스카이라인의 어떤 점에 의해 지배되는지 확인
        이진 탐색을 사용하여 O(log n) 시간 복잡도 달성
        """
        # 스카이라인이 비어있으면 지배될 수 없음
        if not self.skyline_points:
            return False

        # point의 y좌표보다 큰 y좌표를 가진 첫 번째 점의 위치를 찾음
        idx = bisect.bisect_left(self.skyline_points, point, key=lambda x: x[1])

        # 모든 스카이라인 점들의 y좌표가 point보다 작은 경우
        if idx == len(self.skyline_points):
            # 마지막 점만 확인하면 됨
            last_point = self.skyline_points[-1]
            return last_point[0] <= point[0]

        # point보다 y좌표가 큰 첫 번째 점 확인
        if idx < len(self.skyline_points):
            current = self.skyline_points[idx]
            if current[0] <= point[0]:
                return True

        # point보다 y좌표가 작은 점들 중 가장 큰 것 확인
        if idx > 0:
            prev = self.skyline_points[idx - 1]
            if prev[0] <= point[0]:
                return True

        return False

    def remove_dominated(self, point: Tuple[int, int]):
        """
        새로운 점에 의해 지배되는 기존 스카이라인 점들을 제거
        """
        # point의 y좌표보다 큰 y좌표를 가진 첫 번째 점의 위치를 찾음
        idx = bisect.bisect_left(self.skyline_points, point, key=lambda x: x[1])

        # point보다 y좌표가 작은 점들 중에서 x좌표가 point보다 큰 것들을 제거
        i = idx - 1
        while i >= 0:
            if self.skyline_points[i][0] >= point[0]:
                self.skyline_points.pop(i)
            i -= 1

    def add_point(self, point: Tuple[int, int]) -> bool:
        """
        새로운 점을 스카이라인에 추가
        점이 스카이라인에 추가되면 True 반환
        """
        # 이미 지배되는 점이면 추가하지 않음
        if self.is_dominated(point):
            return False

        # 새로운 점에 의해 지배되는 기존 점들 제거
        self.remove_dominated(point)

        # 새로운 점을 y좌표 순서에 맞게 삽입
        bisect.insort_left(self.skyline_points, point, key=lambda x: x[1])
        return True

    def get_skyline(self) -> List[Tuple[int, int]]:
        """현재 스카이라인 포인트들 반환"""
        return self.skyline_points


# 사용 예시
def test_skyline():
    sq = SkylineQuery()
    test_points = [(1, 5), (2, 3), (3, 4), (5, 2), (6, 1)]

    for point in test_points:
        sq.add_point(point)
        print(f"Added {point}, Current skyline: {sq.get_skyline()}")

    return sq.get_skyline()
