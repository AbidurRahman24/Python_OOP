class Star_Cinema:
    hall_list = []

    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)

        seats = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(False)
            seats.append(row)

        self.seats[id] = seats

    def book_seats(self, id, seat_list):
        # Check if the show exists.
        if id not in self.seats:
            raise ValueError("Show does not exist.")

        # Check if the seats are available.
        for row, col in seat_list:
            if self.seats[id][row][col]:
                raise ValueError("Seat is already booked.")

        # Book the seats.
        for row, col in seat_list:
            self.seats[id][row][col] = True

    def view_show_list(self):
        print("Show List:")
        for show_id, movie_name, time in self.show_list:
            print(f"Show ID: {show_id}")
            print(f"Movie: {movie_name}")
            print(f"Time: {time}")
            print("-" * 20)


    def view_available_seats(self, id):
        # Check if the show exists.
        if id not in self.seats:
            print("Show does not exist.")
            return  # Exit the method if the show does not exist.

        # Print a list of all the available seats.
        print("Available seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.seats[id][row][col]:
                    print(f"({row}, {col})")

def run(cinema):
    while True:
        print("\nOptions:")
        print("1: View All Shows Today")
        print("2: View Available Seats")
        print("3: Book Ticket")
        print("4: Exit")
        ch = int(input("\nEnter Option: "))
        if ch == 1:
            for hall in cinema.hall_list:
                hall.view_show_list()
        elif ch == 2:
            show_id = int(input("Enter the ID of the show: "))
            for hall in cinema.hall_list:
                hall.view_available_seats(show_id)
        elif ch == 3:
            show_id = int(input("Enter the ID of the show: "))
            seat_list = []
            while True:
                row = int(input("Enter the row of the seat: "))
                col = int(input("Enter the column of the seat: "))
                seat_list.append((row, col))

                continue_booking = input("Continue booking? (y/n): ")
                if continue_booking.lower() != "y":
                    break

            try:
                for hall in cinema.hall_list:
                    hall.book_seats(show_id, seat_list)
                print("Booking successful!")
            except ValueError as e:
                print(e)
        elif ch == 4:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    cinema = Star_Cinema()
    hall1 = Hall(5, 10, 1)
    hall2 = Hall(6, 8, 2)
    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)
    run(cinema)
