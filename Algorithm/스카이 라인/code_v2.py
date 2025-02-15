from bintrees import FastRBTree
from functools import lru_cache


class RBTreeSkyLine(FastRBTree):
    @staticmethod
    def static_method_1(param):
        return f"Static Method 1 received: {param}"

    @staticmethod
    def static_method_2(param1, param2):
        return f"Static Method 2 received: {param1} and {param2}"


# 사용 예시
result1 = StaticClass.static_method_1("Hello")
result2 = StaticClass.static_method_2("Hello", "World")

print(result1)  # Static Method 1 received: Hello
print(result2)  # Static Method 2 received: Hello and World
