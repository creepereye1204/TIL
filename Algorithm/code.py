import itertools
import sys

# 순열 생성
perm = itertools.permutations(range(50), 5)

# 메모리 사용량 측정
perm_list = list(perm)  # 모든 순열을 리스트로 변환하여 메모리 사용량 측정
memory_usage = sys.getsizeof(perm_list) / (1024 * 1024)  # MB로 변환

print(f"메모리 사용량: {memory_usage:.2f} MB")
