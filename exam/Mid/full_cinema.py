class Star_Cinema:
    hall_list = []
    def entry_hall(self, rows, cols, hall_no):
        new_hall = Hall(rows, cols, hall_no)
        Star_Cinema.hall_list.append(new_hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    def entry_show(self, id='', movie_name='', time=''):
        showInfo = (id, movie_name, time)
        self.show_list.append(showInfo)
        seat = []
        rowChar = 65
        for i in range(self.rows):
            colList = []
            for j in range(self.cols):
                colList.append(f'{0}{0}')
            seat.append(colList)
        makeKey = {id: seat}
        self.__seats.update(makeKey)

    def isValidTicket(self, show_id, seatList=[()]):
        validOrBooked = 0
        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    if i[0] > self.rows or i[1] > self.cols or i[0] < 0 or i[1] < 0:
                        validOrBooked = 2
                        return validOrBooked
                    elif self.__seats[get_id][i[0]][i[1]] == 0:
                        validOrBooked = 1
                        print('rdt')
                        return validOrBooked
        return validOrBooked

    def book_seats(self, name, num, show_id, seatList=[()]):

        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    self.__seats[get_id][i[0]][i[1]] = 0
        movieDetails = ()
        for i in self.show_list:
            if i[0] == show_id:
                movieDetails = i
        customer_details = {'name': name, 'phone': num, 'show_id': show_id, 'seatList': seatList, 'movieDetails': movieDetails}
        return customer_details

    def view_show_list(self):
        for i in self.show_list:
            print('\t\tMovie Name: ',i[1], '\tShow Id: ', i[0], '\tTime: ', i[2])

    def view_available_seats(self, show_id):
        for k in self.__seats[show_id]:
            for j in k:
                print('\t', j, end=' ')
            print('')

    def isValidId(self, show_id):
        isValid = True
        for i in self.show_list:
            if i[0] != show_id:
                isValid = False
            else:
                isValid = True
                return isValid
        return isValid


cinema = Star_Cinema()
cinema.entry_hall(3, 5, 'hall23')
cinema.hall_list[0].entry_show('sfd', 'sujon maji', 'Oct 8 2023 11:00 PM')
cinema.hall_list[0].entry_show('fd', 'sujon maji 2', 'Oct 9 2023 11:00 PM')


while (True):
    print('1.VIEW ALL SHOWS TODAY')
    print('2.VIEW AVAILABLE SEATS')
    print('3.BOOK TICKET')
    print("4.EXIT")
    cp = input('ENTER OPTION: ')
    if int(cp) == 1:
        cinema.hall_list[0].view_show_list()
    elif int(cp) == 2:
        id = input('ENTER SHOW ID: ')
        check_id_validation = cinema.hall_list[0].isValidId(id)
        if check_id_validation == True:
            len = len(cinema.hall_list[0]._Hall__seats[id][0])
            print(len)
            print()
            cinema.hall_list[0].view_available_seats(id)
            print()
        else:
            print('Given Show Id is not exists.')
    elif int(cp) == 3:
        name = input('NAME : ')
        phone_num = input('PHONE NUMBER : ')
        show_id = input('SHOW ID : ')
        ticketQuantity = input('NUMBER OF TICKET : ')
        ticketList = []
        useTicket = []
        for i in range(int(ticketQuantity)):
            seatNo = input('SEAT NO : ')
            useTicket.append(seatNo)
            row = ord(seatNo[0])
            col = ord(seatNo[0])
            seat = (row, col)
            ticketList.append(seat)
        is_id_valid = cinema.hall_list[0].isValidId(show_id)
        
        if is_id_valid == True:
            ticket_valid_booked = cinema.hall_list[0].isTicketValid(show_id, ticketList)
            if ticket_valid_booked == 0:
                customerBooking = cinema.hall_list[0].book_seats(
                    name, phone_num, show_id, ticketList)
                print('TICKET BOOKED SUCCESSFULLY!!')
                print('NAME : ', name)
                print('NUMBER : ', phone_num)
                print('')
                print('MOVIE NAME : ',customerBooking['movieDetails'][1],' MOVIE TIME : ', customerBooking['movieDetails'][2])

                print('TICKETS : ', end=' ')
                for i in useTicket:
                    print(i, end=' ')
                print('HALL : Hall24')
            elif ticket_valid_booked == 1:
                print('This ticket is already booked.')
            elif ticket_valid_booked == 2:
                print('Nt a valid ticket.')
        else:
            print('Show Id is not exists.')
    elif int(cp) == 4:
        break
    else:
        print('Not valid Input')