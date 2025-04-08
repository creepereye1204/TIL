class Person: 
    def __init__(self, name, id): 
        self.name = name
        self.id = id
    def get_details(self):
        return f"이름: {self.name}, ID: {self.id}"
    
class Professor(Person): 
    def __init__(self, name, id, lecture): 
        super().__init__(name, id) 
        self.lecture = lecture 
    def get_details(self): 
        return f"교수:{self.name}, 코드:{self.id}, 강좌명:{self.lecture}"

class Student(Person): 
    def __init__(self, name, id, major,score ): 
        super().__init__(name, id) 
        self.major = major 
        self.score = score 
    def get_details(self): 
        return f"학생:{self.name}, 학번:{self.id}, 소속:{self.major}, 학점:{self.score}"
    


professor = Professor("최희식", "1371-01", "Big Data Processing")
student = Student("김삼육", "20251234", "컴퓨터공학", "B+")
print(professor.get_details()) 
print(student.get_details()) 