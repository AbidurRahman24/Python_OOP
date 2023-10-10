class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}  # Initialize seats as an empty dictionary
        self.show_list = []  # Initialize show_list as an empty list

        # Populate seats dictionary based on rows and columns
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                seat_number = f"Seat-{row}-{col}"
                self.seats[seat_number] = {"status": "unoccupied"}

        # Insert the Hall object into the Star_Cinema's hall_list
        Star_Cinema.entry_hall(self)

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
        else:
            print("Invalid input. Please provide an object of class Hall.")

# Example usage:
hall1 = Hall(rows=5, cols=10, hall_no=1)
hall2 = Hall(rows=6, cols=8, hall_no=2)

# Check the contents of Star_Cinema's hall_list
for hall in Star_Cinema.hall_list:
    print(f"Hall Number: {hall.hall_no}, Rows: {hall.rows}, Columns: {hall.cols}")
