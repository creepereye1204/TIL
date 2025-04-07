class A:
    a="apple"
    def __init__(self):  # 생성자
        self.b="banana"
        self.c="carrot"

    
class B(A):  # A를 상속받음
    def __init__(self):  # 생성자
        super().__init__()  # 부모 클래스 생성자 호출
        print(self.b)
    def s(self):
        print(self.c)

b=B()  # B 클래스 객체 생성
b.s()