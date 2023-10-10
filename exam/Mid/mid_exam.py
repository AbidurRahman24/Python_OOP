class Star_Cinema:
  hall_list = []
  
  def entry_hall(self, hall):
    self.hall_list.append(hall)

  

class Hall(Star_Cinema):
  def __init__(self, hall_name, no_of_seats):
    self.hall_name = hall_name
    self.no_of_seats = no_of_seats

    