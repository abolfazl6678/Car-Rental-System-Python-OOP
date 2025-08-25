import datetime
class customer():

    dt_today=datetime.date.today()
    with open('Inventory.txt', 'r') as file:
        inventory_h = int(file.readline().strip())
        inventory_d = int(file.readline().strip())
        inventory_w = int(file.readline().strip())

    
    with open('Requested.txt', 'r') as file:
        lines = file.readlines()
        int(lines[len(lines)-5])




    
    
    
    with open('Requested.txt', 'r') as file:
        
        
        
        
        
        
        
        
        Requested_customer_n = int(file.readline().strip())
        Requested_name = str(file.readline().strip())
        Requested_date = file.readline().strip()
        Requested_mode = file.readline().strip()
        Requested_number = file.readline().strip()

    @classmethod
    def available_cars(cls):
        print("--------------------------------------------------------------------------------------------")
        print("Number of available cars in hourly mode (", customer.dt_today.strftime("%B %d, %Y"), "): ", customer.inventory_h)
        print("                             daily mode (", customer.dt_today.strftime("%B %d, %Y"), "): ", customer.inventory_d)        
        print("                            weekly mode (", customer.dt_today.strftime("%B %d, %Y"), "): ", customer.inventory_w)        
        print("--------------------------------------------------------------------------------------------")

    @classmethod
    def RequestCar(cls):

        with open('Requested.txt', 'r') as file:
            lines = file.readlines()
            customer_n = int(lines[len(lines)-5])+1
        
        customer_name = str(input('What is your name?                  '))
        customer_date = customer.dt_today
        print("--------------------------------------------------------------------------------------------")
        print("Please request your car based on below information:")
        print("Please make sure the number of cars you are requesting is lower than availble cars")
        customer.available_cars()
        print('Please write your rental request mode: ')
        mode_request = str(input("For hourly: write H, For daily: write D, For Weekly: write W         "))
        while mode_request not in ['H', 'D', 'W']:
            print("You have selected:", mode_request)
            mode_request = str(input("Invalid input. Please enter H, D, or W: "))
        print("You have selected:", mode_request)
        print('How many cars do you need?')
        if mode_request == "H":
            number_request = int(input(f"How many cars do you need (it must be integer between 0 and {customer.inventory_h}         "))
            while (number_request > customer.inventory_h) or (number_request < 0):
                number_request = str(input(f"Invalid input. it must be integer between 0 and {customer.inventory_h} "))
            with open('Inventory.txt', 'w') as file:
                file.write(str(customer.inventory_h-number_request) + "\n")
                file.write(str(customer.inventory_d) + "\n")
                file.write(str(customer.inventory_w) + "\n")
        elif mode_request == "D":
            number_request = int(input(f"How many cars do you need (it must be integer between 0 and {customer.inventory_d}         "))
            while (number_request > customer.inventory_d) or (number_request < 0):
                number_request = str(input(f"Invalid input. it must be integer between 0 and {customer.inventory_d} "))
            with open('Inventory.txt', 'w') as file:
                file.write(str(customer.inventory_h) + "\n")
                file.write(str(customer.inventory_d-number_request) + "\n")
                file.write(str(customer.inventory_w) + "\n")
        else:
            number_request = int(input(f"How many cars do you need (it must be integer between 0 and {customer.inventory_w}         "))
            while (number_request > customer.inventory_w) or (number_request < 0):
                number_request = str(input(f"Invalid input. it must be integer between 0 and {customer.inventory_w} "))
            with open('Inventory.txt', 'w') as file:
                file.write(str(customer.inventory_h) + "\n")
                file.write(str(customer.inventory_d) + "\n")
                file.write(str(customer.inventory_w-number_request) + "\n")
        with open('Requested.txt', 'a') as file:
            file.write(str(customer_n) + "\n")
            file.write(customer_name + "\n")
            file.write(str(customer_date) + "\n")
            file.write(mode_request + "\n")
            file.write(str(number_request) + "\n")     
        
        return [customer_n, customer_name, customer_date, mode_request,number_request]
        

    @classmethod
    def ReturnCar(cls):
        with open('Requested.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]  # remove \n

        customer_n_r = int(input('Enter your customer request number: '))

    # safer validation (assuming 5 lines per request)
        total_requests = len(lines) // 5
        while customer_n_r >= total_requests:
            customer_n_r = int(input('Enter a valid customer request number: '))

    # Each request block is 5 lines
        base = customer_n_r * 5
        customer_name = lines[base + 1]
        rent_date = lines[base + 2]
        mode_return = lines[base + 3]
        quantity = int(lines[base + 4])   # convert to integer
    # Update inventory based on mode
        with open('Inventory.txt', 'w') as file:
            if mode_return == 'H':
                print('Returning Hourly Rental')
                file.write(str(customer.inventory_h + quantity) + "\n")
                file.write(str(customer.inventory_d) + "\n")
                file.write(str(customer.inventory_w) + "\n")
            elif mode_return == 'D':
                print('Returning Daily Rental')
                file.write(str(customer.inventory_h) + "\n")
                file.write(str(customer.inventory_d + quantity) + "\n")
                file.write(str(customer.inventory_w) + "\n")
            elif mode_return == 'W':
                print('Returning Weekly Rental')
                file.write(str(customer.inventory_h) + "\n")
                file.write(str(customer.inventory_d) + "\n")
                file.write(str(customer.inventory_w + quantity) + "\n")
            else:
                print("Invalid return mode!")
        

        return [customer_n_r, customer_name, rent_date, mode_return, quantity]

