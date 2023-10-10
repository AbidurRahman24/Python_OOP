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

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            seat_allocation = self.seats[show_id]

            for row, col in seats_to_book:
                if 1 <= row <= self.rows and 1 <= col <= self.cols:
                    if seat_allocation[row - 1][col - 1] == 0:
                        seat_allocation[row - 1][col - 1] = 1  # Book the seat
                        print(f"Seat-{row}-{col} has been booked.")
                    else:
                        print(f"Seat-{row}-{col} is already booked.")
                else:
                    print(f"Invalid seat: Seat-{row}-{col}")
        else:
            print(f"Show with ID {show_id} does not exist in this hall.")

    def view_show_list(self):
        if self.show_list:
            print("Shows running in this hall:")
            for show in self.show_list:
                print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Show Time: {show[2]}")
        else:
            print("No shows running in this hall.")

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

# Add shows to hall1
hall1.entry_show("show1", "Movie A", "12:00 PM")
hall1.entry_show("show2", "Movie B", "3:00 PM")

# View the list of shows running in hall1
hall1.view_show_list()
