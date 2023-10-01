class Student:
    def __init__(self,name,current_class,id) -> None:
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self) -> str:
        return f'Student name : {self.name} class : {self.current_class} id : {self.id}'

class Teachers:
    def __init__(self,name, subject,id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher {self.name} subject : {self.subject} id : {self.id}'
    
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name,subject):
        id = len(self.teachers) + 101
        teacher = Teachers(name,subject,id)
        self.teachers.append(teacher)


    def enroll(self,name,fee):
        if fee < 6500:
            return "NO POSSIBLE TO ENROLL HERE"
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
        
    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'
    

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)