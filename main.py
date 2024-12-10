# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import csv
import ast
from tabulate import tabulate
def add_car():
    csv_list = []
    id=1
    name = input("Enter Name:")
    brand = input("Enter Brand:")
    category = input("Enter Category[Hatchback/Suv/Coupe/Van]:")
    while True:
      if category not in ['Hatchback', 'Suv', 'Coupe', 'Van']:
        print("Invalid Category!!")
        category = input("Enter Category[Hatchback/Suv/Coupe/Van]:")
      else:
          break
    min_price = input("Enter Min Price:")
    max_price = input("Enter Max Price:")
    fuel_type = input("Feul Type [Petrol, Deisel, Electric, CNG, Hybrid]:")
    while True:
     if fuel_type not in ['Petrol' , 'Deisel' , 'Electric' , 'CNG' , 'Hybrid']:
        print("Invalid Feul Type!!")
        fuel_type = input("Feul Type [Petrol, Deisel, Electric, CNG, Hybrid]:")
     else:
         break
    max_seat = input("Enter Max Seating Capability:")
    milege = input("Enter Milege:")

    csv_list.clear()

    with open('cars.csv', mode='r') as f_ile:
        add_csv_lst = csv.reader(f_ile)
        summary_length = list(add_csv_lst)
        for x, line in enumerate(summary_length, 0):
            print(line)
            if(line==[]):
                print("This is empty")
            else:
                id=int(line[0])+1
    csv_list.insert(0, id)
    csv_list.insert(1, name)
    csv_list.insert(2, brand)
    csv_list.insert(3, category)
    csv_list.insert(4, min_price)
    csv_list.insert(5, max_price)
    csv_list.insert(6, fuel_type)
    csv_list.insert(7, max_seat)
    csv_list.insert(8, milege)

    with open('cars.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_list)
        print("Added Successfully")
def show_all_cars():
    with open('cars.csv', mode='r') as f_ile:
        csv_lst = csv.reader(f_ile)
        table = tabulate(csv_lst,
                headers=["Name", "Brand", "Category", "Min Price", "Max Price", "Fuel Type","Max Seat","Milege"],
                tablefmt="grid"
                )
        print(table)
def show_selected_car():
    user_input=int(input("Enter the Car Id:"))
    with open('cars.csv', mode='r') as f_ile:
        add_csv_lst = csv.reader(f_ile)
        summary_length = list(add_csv_lst)
        summary_list = []
        for x, line in enumerate(summary_length, 0):
            summary_list.append(line)
            if (x <=len(summary_length) - 1):
                if (summary_list[x] != []):
                    if(str(user_input)==summary_list[x][0]):
                        table = tabulate(summary_list,
                                         headers=["Id","Name", "Brand", "Category", "Min Price", "Max Price", "Fuel Type",
                                                  "Max Seat", "Milege"],
                                         tablefmt="grid"
                                         )
                else:
                    summary_list[x].clear()
        print(table)
def search_cars():
    user_input = input("Enter Search:")
    with open('cars.csv', mode='r') as f_ile:
        add_csv_lst = csv.reader(f_ile)
        summary_length = list(add_csv_lst)
        summary_list = []
        for x, line in enumerate(summary_length, 0):
            summary_list.append(line)
            if (x <= len(summary_length) - 1):
                if (summary_list[x] != []):
                    if (str(user_input) == summary_list[x][1] or str(user_input) == summary_list[x][2] or str(user_input) == summary_list[x][3]):
                        table = tabulate(summary_list,
                                         headers=["Id", "Name", "Brand", "Category", "Min Price", "Max Price",
                                                  "Fuel Type","Max Seat", "Milege"],
                                         tablefmt="grid"
                                         )
        print(table)
def edit_selected_car():
    user_input = int(input("Enter the Car Id:"))
    with open('cars.csv', mode='r') as f_ile:
        add_csv_lst = csv.reader(f_ile)
        summary_length = list(add_csv_lst)
        summary_list = []
        active_row=False
    for x, line in enumerate(summary_length, 0):
        summary_list.append(line)
        print(line)
        if (x <= len(summary_length) - 1):
            if (summary_list[x] != []):
                if (str(user_input) == summary_list[x][0]):
                    active_row=True
                    print(" older summary_list"+str(summary_list))
                    name = input("Enter Name:")
                    brand = input("Enter Brand:")
                    category = input("Enter Category[Hatchback/Suv/Coupe/Van]:")
                    while True:
                        if category not in ['Hatchback', 'Suv', 'Coupe', 'Van']:
                            print("Invalid Category!!")
                            category = input("Enter Category[Hatchback/Suv/Coupe/Van]:")
                        else:
                              break
                    min_price = input("Enter Min Price:")
                    max_price = input("Enter Max Price:")
                    fuel_type = input("Feul Type [Petrol, Deisel, Electric, CNG, Hybrid]:")
                    while True:
                         if fuel_type not in ['Petrol' , 'Deisel' , 'Electric' , 'CNG' , 'Hybrid']:
                            print("Invalid Feul Type!!")
                            fuel_type = input("Feul Type [Petrol, Deisel, Electric, CNG, Hybrid]:")
                         else:
                             break
                    seat = input("Enter Max Seating Capability:")
                    milege = input("Enter Milege:")

                    summary_list[x][0]=user_input
                    summary_list[x][1]=name
                    summary_list[x][2]=brand
                    summary_list[x][3]=category
                    summary_list[x][4]=min_price
                    summary_list[x][5]=max_price
                    summary_list[x][6]=fuel_type
                    summary_list[x][7]=seat
                    summary_list[x][8]=milege
                    break
    if active_row:
      with open('cars.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(summary_list)
        print("Added Successfully")
def delete_selected_car():
    user_input = input("Enter the Car ID to delete: ")
    csv_lst=[]
    with open('cars.csv', mode='r') as f_ile:
        add_csv_lst = csv.reader(f_ile)
        summary_length = list(add_csv_lst)
        row_change=False

    for x, line in enumerate(summary_length, 0):
            print(line)
            if(line==[]):
                print("This is empty")
            elif(user_input == line[0]):
                print("yee"+str(summary_length[x]))
                del summary_length[x]
                print("summ"+str(summary_length))
                row_change=True

    if row_change:
            with open('cars.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for y, csv_line in enumerate(summary_length, 0):
                    if (summary_length[y] != []):
                        csv_lst.insert(0, summary_length[y][0])
                        csv_lst.insert(1, summary_length[y][1])
                        csv_lst.insert(2, summary_length[y][2])
                        csv_lst.insert(3, summary_length[y][3])
                        csv_lst.insert(4, summary_length[y][4])
                        csv_lst.insert(5, summary_length[y][5])
                        csv_lst.insert(6, summary_length[y][6])
                        csv_lst.insert(7, summary_length[y][7])
                        csv_lst.insert(8, summary_length[y][8])
                        writer.writerow(csv_lst)
                        csv_lst=[]
    print("Deleted Successfully")

def main():
    while True:
        user_input = int(input("Select any of the options: \n 1. Add Car \n 2. Show All cars \n 3. Show Selected Car \n 4. Search cars by name/Brand/Caregory\n"
                               " 5. Edit selected car \n 6. Delete Selected car \n"))
        if user_input == 1:
            add_car()
        elif user_input == 2:
            show_all_cars()
        elif user_input == 3:
            show_selected_car()
        elif user_input == 4:
            search_cars()
        elif user_input == 5:
            edit_selected_car()
        elif user_input == 6:
            delete_selected_car()
        else:
            print("Invalid Input. Please select again.")
main()
