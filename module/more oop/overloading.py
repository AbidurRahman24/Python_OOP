class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('gym e poisa diya hudai gham jorai')
    # overlaod
    def __add__(self, other):
        return self.age + other.age

sakib = Cricketer('sakib', 38,68,70,"BD")
moshi = Cricketer('mosi', 34,64,50,"BD")

print(sakib + moshi)