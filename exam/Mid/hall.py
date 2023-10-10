class Hall:
    def __init__(self, hall_name, capacity):
        self.hall_name = hall_name
        self.capacity = capacity

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
        else:
            print("Invalid input. Please provide an object of class Hall.")
