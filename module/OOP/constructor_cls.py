class Phone:
    manufacture = "Chaina"
    def __init__(self,name,brand,price) -> None:
        self.name = name
        self.brand = brand
        self.price = price
    
    def send_sms(self,phone,sms):
        text = f'Sending to {phone} -- {sms}'
        print(text)
# my_phone = Phone('Kala Chan', 'Oppo', 9800)
# print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('She amar jaan', 'iphone', 120000)
print(her_phone.name, her_phone.brand, her_phone.price)

my_phone = Phone('Niloy', 'VIVO', 9800)
print(my_phone.name, my_phone.brand, my_phone.price)