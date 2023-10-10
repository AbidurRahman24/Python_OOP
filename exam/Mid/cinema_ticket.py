class Star_Cinema:
    hall_list = []

    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
    
    def entry_show(self,id,movie_name,time):
        show = (id, movie_name, time)
        self.show_list.append(show)

        seats = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(False)
            seats.append(row)

        self.seats[id] = seats

    def book_seats(self,id,seat_list):
        
        if id not in self.seats:
            raise ValueError("Show does not exist.")


        for row, col in seat_list:
            if self.seats[id][row][col]:
                raise ValueError("Seat is already booked.")


        for row, col in seat_list:
            self.seats[id][row][col] = True
    @property
    def view_show_list(self):
        if self.show_list:
            print("Shows running in this hall:")
            for show in self.show_list:
                print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Show Time: {show[2]}")
        else:
            print("No shows running in this hall.")

    def view_available_seats(self, id):
        if id not in self.seats:
            raise ValueError("Show does not exist.")
        
        print("Available seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.seats[id][row][col]:
                    print(f"({row}, {col})")
hall1 = Hall(rows=5, cols=10, hall_no=1)
# Add shows to hall1
hall1.entry_show("show1", "Movie A", "12:00 PM")
hall1.entry_show("show2", "Movie B", "3:00 PM")

# View the list of shows running in hall1
hall1.view_show_list()
    



