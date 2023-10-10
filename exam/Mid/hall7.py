class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}  
        self.show_list = [] 

        for row in range(0, rows + 1):
            for col in range(0, cols + 1):
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
                        seat_allocation[row - 1][col - 1] = 0  # Book the seat
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

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            seat_allocation = self.seats[show_id]
            available_seats = []

            for row in range(len(seat_allocation)):
                for col in range(len(seat_allocation[0])):
                    if seat_allocation[row][col] == 0:
                        available_seats.append((row + 1, col + 1))

            if available_seats:
                print(f"Available seats for show {show_id}: {available_seats}")
            else:
                print(f"All seats for show {show_id} are booked.")
        else:
            print(f"Show with ID {show_id} does not exist in this hall.")

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
        else:
            print("Invalid input. Please provide an object of class Hall.")

def main():
    hall1 = Hall(rows=5, cols=10, hall_no=1)
    hall1.entry_show("show1", "Movie A", "12:00 PM")
    hall1.entry_show("show2", "Movie B", "3:00 PM")

    while True:
        print("\nWelcome to Star Cinema Counter")
        print("1. View all shows")
        print("2. View available seats in a show")
        print("3. Book tickets for a show")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hall1.view_show_list()
        elif choice == "2":
            show_id = input("Enter the show ID: ")
            hall1.view_available_seats(show_id)
        elif choice == "3":
            show_id = input("Enter the show ID: ")
            num_tickets = int(input("Enter the number of tickets to book: "))
            seats_to_book = []
            for i in range(num_tickets):
                row = int(input(f"Enter row for ticket {i + 1}: "))
                col = int(input(f"Enter column for ticket {i + 1}: "))
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)
        elif choice == "4":
            print("Thank you for using Star Cinema Counter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
