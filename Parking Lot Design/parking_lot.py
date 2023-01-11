# Parking lot design

class Car : 
    def __init__(self, license, model, color) -> None:
        self.license = license
        self.model = model
        self.color = color
    
    def __repr__(self) : 
        return f'{self.license}, {self.model}, {self.color}'

class Garage : 
    def __init__(self) -> None:
        self.car_added = []
        self.spot = 10
        self.car_infos = {}
        self.bill = 0
        self.ticket = []

    def spots_available(self) : 
        return f'Total spots available : {self.spot}'
    
    def add_car_to_garage(self, car) :
        self.spot_name = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        
        if self.spot > 0 : 
             user_data = str(car).split(',')
             self.spot -= 1
             self.car_added.append(user_data)
             self.car_infos = {'Tickets' : [], 'License' : [], 'Model' : [], 'Color' : []}
             ticket = ''

             for i, val in enumerate(self.car_added) : # [[], [], [], [], []]
                ticket = self.spot_name[i] + val[0] 
                # print(ticket)
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
                
             print(f'Successfully Parked!\nYour TICKET is : {ticket}')
            
        else : 
            print('No spot available!')
        
    def unpark(self, ticket, hours) :
        if ticket not in self.car_infos['Tickets'] : # security check purpose -> O(N)
            print('No car found!!!')
            return
        else : 
            for i, val in enumerate (self.car_infos['Tickets']) : 
                if val == ticket : 
                    print(i)
                    print(f"Your License is : {self.car_infos['License'][i]}")
                    print(f"Your Model is : {self.car_infos['Model'][i]}")
                    print(f"Car color is {self.car_infos['Color'][i]}")
                    removed_car_index = i
                    self.car_infos['License'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.car_infos['Tickets'].pop(i)

                    self.spot += 1

        if hours > 30 : 
            print(f'Total Bill : ${hours * 5 + 100}')
        else :
            print(f'Total Bill : ${hours * 5}')

    def total_cars_in_garage(self) : 
        for i in self.car_infos.items() : 
            print(i)

my_garage = Garage()

# user_car = Car('1234MB', 'Audi', 'Blue')
# user_car1 = Car('453EH', 'Ferrari', 'Green')
# my_garage.add_car_to_garage(user_car)
# my_garage.add_car_to_garage(user_car1)
# my_garage.total_cars_in_garage()
# my_garage.unpark('A11234MB', 10)
# my_garage.total_cars_in_garage()
# my_garage.unpark('B1453EH', 40)
# my_garage.total_cars_in_garage()

print("************** Welcome to our system ***************")

while True : 
    print("What do you want?")
    print("1. Park your Car\n2. Check available space\n3. Unpark your Car\nTotal cars in Garage")

    user_choice = int(input('Enter your choice : '))

    if user_choice == 1 : 
        car_license = input('Enter your car license : ')
        car_model = input("Enter your car model : ")
        car_color = input("Enter your car color : ")
        user_car = Car(car_license, car_model, car_color) # Car Class object

        my_garage.add_car_to_garage(user_car)
        print()
    
    elif user_choice == 2 :
        print(my_garage.spots_available())
        print()

    elif user_choice == 3 : 
        ticket = input('Enter your ticket number : ')
        hours = int(input('Enter hours : '))
        if my_garage.spot == 10 : 
            continue
        else : 
            my_garage.unpark(ticket, hours)
        print()

    elif user_choice == 4 : 
        my_garage.total_cars_in_garage()
        print()

    else : 
        break