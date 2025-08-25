import datetime
import Cust_m
print('what do you want to do? For inventory avaiablity: type a ')
print('                        For rent a car          : type r ')
print('                        For return a car        : type r_b')
action = input(str('Your response is:                       '))

dt_today2=datetime.date.today()

if action == 'a':
    Cust_m.customer.available_cars()

elif action == 'r':
    Cust_m.customer.RequestCar()
    print('Car request is done!')

elif action == 'r_b':
    #Cust_m.customer.ReturnCar()
    rent_billing = Cust_m.customer.ReturnCar()
    mode_rent = rent_billing[3] 
    mode_rent = 'H'
    if mode_rent == 'H':
        n_hours = int(input('How many hours did you used the cars? '))
        rate_rent = int(input('Enter rate of the company for returned car:     '))
        n_cars = int(rent_billing[4])
        total_price = n_hours *rate_rent*n_cars
    elif ((mode_rent == 'D') or  (mode_rent == 'W')):
        rate_rent = input('Enter rate of the company for returned car:     ')
        n_days = (dt_today2 - rent_billing[2]).days
        n_cars = int(rent_billing[4])
        total_price = n_days *rate_rent*n_cars
    else:
        print('Start over and enter a valid number!')

    print('Return process is done!')
    print('                                    ')    
    print(f' Dear {rent_billing[1]}: you have returned the car. See below for your billing detail')
    print('---------------------------------------------------------------------------------------------------')
    print(f'Your rented number: {rent_billing[0]}. Please keep and show it to the admin if you have any question in the future.')
    print(f'Name of renter: {rent_billing[1]}')
    print(f'Number of cars rented: {rent_billing[4]}')
    print(f'Rent duration: from {rent_billing[2]} ')
    print(f'rent rate: {rate_rent}')
    print(f'Total price: {total_price}')
    print('---------------------------------------------------------------------------------------------------')



