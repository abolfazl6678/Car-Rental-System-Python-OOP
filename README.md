# Car-Rental-System-Python-OOP
Python Object-Oriented Programming project simulating an online car rental platform. Demonstrates OOP concepts, inventory management, billing calculations, and DateTime handling in Jupyter Notebook.


## Overview
This project is part of my **Python OOP Course-End Project** where I developed an **online car rental platform** using **Object-Oriented Programming (OOP)** in Python.

The goal is to simulate a car rental company system where:  
- Customers can **view available cars**  
- Rent cars on an **hourly, daily, or weekly basis**  
- Return cars and receive an **auto-generated bill**  

This project demonstrates strong **OOP principles, modular design, and time-based calculations** in Python.

---

## Problem Statement
A car rental company needs a platform to manage customer rentals. The system should:  
- Allow customers to choose rental modes (**hourly, daily, weekly**)  
- Track car availability and prevent overbooking  
- Store rental time to calculate billing  
- Generate final bills upon return  
- Update the inventory automatically  

---

## Tools & Techniques Used
- **Programming Language:** Python  
- **Development Environment:** Jupyter Notebook  
- **Libraries:**  
  - `datetime` → handle rental start/end time  
  - Python OOP → modules, classes, methods, constructors  

---

## Project Description 
The platform is built with two main modules:

1. **CarRental Module**  
   - Monitor available inventory
   - Request cars on hourly, daily and weekly basis
   - Handle car returns and generate bills

2. **Cust_m Module**  
   - Request cars from the company  
   - Return rented cars  
   - Interface with rental methods  

---

## Key Tasks Performed 

**CarRental_m module**  
- User intraction for checking availability, renting and returning
- Using method and classes defined in Cust_m module to perform the tasks
- Used `datetime` to calculate rental duration  
- Billing calculated based on rental mode & duration  

**Cust_m moduleg**  
- Created available_cars class (check available cars in inventory)
- Defined methods for renting cars (hourly, daily, weekly)
- Created RequestCar class (hourlly, daily and weekly basis)
- Created ReturnCar class (return cars and update inventory)
- Stored and ypdated rental and returned car info
- Implemented validation (e.g., positive request, stock availability)
 
---

## Project Structure 
```
Online-Car-Rental-Platform/
├── CarRental_m.py # Rental system module (OOP logic)
├── Cust_m.py 
├── Inventory.txt
├── Requested.txt
├── output/
│ ├── screen_shot_availability_check.png
│ ├── screen_shot_request_cars.png
│ └── screen_shot_return_bill.png
└── README.md

```


---

## Features
- **OOP-based Design** – modular and extensible  
- **Multiple Rental Options** – hourly, daily, weekly  
- **Validation** – prevents invalid requests  
- **Automated Billing** – accurate cost based on time & cars  
- **Dynamic Inventory** – updates on rent/return  

---

## Future Enhancements
- Add **GUI interface** using Tkinter or Flask (web-based)  
- Implement **database backend** for persistence  
- Add **discount system** (e.g., family rental discount)  
- Track **customer history & loyalty programs**  










