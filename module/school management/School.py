class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.classroom = {}

    def add_classroom(self,classroom):
        self.classroom[classroom.name] = classroom #classroom sheri take
    #poti classroom a student add hobe
    def student_addmition(self,student,classroom_name):
        # class room ar maje jeno class room take tai if else use korte hobe
        # TODO: set student id(roll number) at the time of adding the student
        if classroom_name in self.classroom:
            self.classroom[classroom_name].add_student(student)
        else:
            print(f"no class room as name {classroom_name}")

class Classroom:
    def __init__(self,name) -> None:
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students) + 1}'
        self.student.append(student)

    def __repr__(self) -> str:
        return f'{self.name}-{len(self.students) }'
    
    # TODO: sort students by grade
    def get_top_student(self):
        pass

