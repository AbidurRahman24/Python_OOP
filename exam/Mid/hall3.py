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

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.show_list.append(show_info)

        # Allocate seats for this show using a 2D list
        seat_allocation = [[0] * self.cols for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation

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

# Add a show to hall1
hall1.entry_show("show1", "Movie A", "12:00 PM")

# Check the contents of hall1's show_list
for show in hall1.show_list:
    print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Show Time: {show[2]}")

# Check the seat allocation for the show
print(hall1.seats["show1"])
