
space_avail = 4
registered_plates=[]
registered_CC=[]

def register_vehicle1():
    global space_avail # declare a global variable inside the function
    parking_spaces_used = 0
    if space_avail > parking_spaces_used: # check to see if there is enough parking spaces max is set above in global variable space_avail
        print ("The parking lot has space for your vehicle")
        plate_number = input("Enter your plate number:")
        if plate_number not in registered_plates:
            registered_plates.append(plate_number)
            credit_card = input("Enter your credit card number ($4.00 charge):")
            registered_CC.append(credit_card)
            print (f"Thank you, your plate {plate_number} has been added to the lot.")
            #print (registered_plates) uncomment to see a printed list of the plate added to list registered_plates
            #print (registered_CC) uncomment to see a printed list of the credit card added to list registered_CC
            space_avail -= 1
           # print (space_avail) uncomment this line if you would like to see the remaining parking spaces
            restart3 = input("Please Press enter to continue...")
        else:
            print (f"The vehicle with plate {plate_number} is registered in the lot.")
            restart4 = input("Please Press enter to continue...")
    else:
        print ("The parking lot is full.")
        restart5 = input("Please Press enter to continue...")
    
def verify_vehicle2(verify):
    if verify in registered_plates:
        print (f"The vehicle with plate# {verify} is registered in the lot.")
        restart6 = input("Please Press enter to continue...")
    else:
        print ("The vehicle is NOT registered.")
        restart7 = input("Please Press enter to continue...")

def display_vehicle3():
    # if len(registered_plates) == 0: can reverse the is statment to apply if statment on an empty list
    if not registered_plates:
        print ("The Parking Lot is empty!")
        restart9 = input("Please Press enter to continue...") # allows the user a break
    else:
        my_file = open('vehicle.txt', 'w') # opens the file in write mode, if nothing is written(i think if nothing is written in it will only delete it) in pyhton deletes all contents in the file. this ensures we have a blank document before we write to it.
        my_file.close()
        print('A list of registered vehicles for 2023-10-29') # Can we get a function/obj/class(whatever) to display the date for that day? or should this be tied to the date the text file was created or last edited?
        my_file = open('vehicle.txt', 'a')
        my_file.write("====================\n")
        my_file.write ("       Plate\n")
        my_file.write("====================\n")
        for item in registered_plates:
            my_file.write(f"{str(item):>11}\n") # to format data types string you must specify str before the variable example{str(item):>11.2f} ////////  {total_interest:>14.2f} is meant to format integers.
        my_file.write("====================\n")
        my_file.close()
        print('Daily parking summary for 2023-10-29') # Can we get a function/obj/class(whatever) to display the date for that day? or should this be tied to the date the text file was created or last edited?
        my_file= open('vehicle.txt', 'r')
    # print each line of file
        for each_line in my_file:
            each_line = each_line.rstrip()
            print(each_line)
        my_file.close()
        restart8 = input("Please Press enter to continue...") # allows the user a break

def display_Charges4():
    my_file = open('charges.txt', 'w') # opens the file in write mode, if nothing is written(i think if nothing is written in it will only delete it) in pyhton deletes all contents in the file. this ensures we have a blank document before we write to it.
    my_file.close()
    my_file = open('charges.txt', 'a')
    my_file.write("======================================================\n")
    my_file.write ("       Plate           Credit Card         Charge in $\n")
    my_file.write("======================================================\n") 
    charge = 4
    number_of_cars = len(registered_plates)
    total_charges_for_day = charge * number_of_cars
    for i in range(len(registered_plates)):
        plate = registered_plates[i]
        cc = registered_CC[i]
        my_file.write(f"{str(plate):>11}{str(cc):>22}{charge:>16}\n")# to format data types string you must specify str before the variable example{str(item):>11.2f} ////////  {total_interest:>14.2f} is meant to format integers.

    my_file.write("======================================================\n")
    my_file.write(f"{'Total':>12}{total_charges_for_day:>37}") # you dont have to press space 12 times for proper spacing you can put a string into {} curcly braces and use the :>13 format option. just make sure to not use "" if you used them to surround your original statment.
    my_file.close()
    print('Daily parking summary for 2023-10-29') # Can we get a function/obj/class(whatever) to display the date for that day? or should this be tied to the date the text file was created or last edited?
    my_file= open('charges.txt', 'r')
# print each line of file
    for each_line in my_file:
        each_line = each_line.rstrip()
        print(each_line)
    my_file.close()
    restart10 = input("Please Press enter to continue...") # allows the user a break

def remove_vehicle5(remove_plate):
    global space_avail # declare a global variable inside the function
    if remove_plate in registered_plates: # checks to see if the plate number inputted by the user is in the list registered_plates
        index_number = registered_plates.index(remove_plate) # finds the index number of the item remove_plate and assigns it to variable index_number
        del registered_plates[index_number] # deletes the index_number (remove_plates "index number" is assigned to index_number variable on line above. I know I shoulda picked a better name. ) of the license plate from the list registered_plates
        del registered_CC[index_number] # deletes the index number of the credit card from the list resitered_CC
        print (f"{remove_plate} is removed.")
        space_avail += 1
        restart11 = input("Please Press enter to continue...") # allows the user a break
    else:
        print (f"{remove_plate} is not registered.")
        restart12 = input("Please Press enter to continue...") # allows the user a break

def clear_vehicle6():
    global space_avail  
    space_avail = 4
    my_file = open('vehicle.txt', 'w') # opens the file in write mode, if nothing is written(i think if nothing is written in it will only delete it) in pyhton deletes all contents in the file. this ensures we have a blank document before we write to it.
    my_file.close()
    my_file = open('charges.txt', 'w') # opens the file in write mode, if nothing is written(i think if nothing is written in it will only delete it) in pyhton deletes all contents in the file. this ensures we have a blank document before we write to it.
    my_file.close()
    registered_plates.clear()
    registered_CC.clear()
    print ("All vehicles were removed and the lot is empty.")
    restart13 = input("Please Press enter to continue...") # allows the user a break
    #my_list = [] both of these options will clear a list
    #my_list.clear() both of these options will clear a list
  
def check_password():
    password = input("Enter your password: ") #(Hint password=password)
    if password == "password":
        authorize = True
        return authorize 
    else:
        print("Password is incorrect!")
        restart2 = input("Please Press enter to continue...")
        authorize = False
        return authorize


def print_menu(): 
    i = True
    while i == True:
        print("************************************************************")
        print("*** Welcome to Park and Go Parking Application! ***")
        print("Park from 6 PM - Midnight for a flat fee of $4.00")
        print("************************************************************")
        print("Select from the following options:")
        print("1- Register a vehicle")
        print("2- Verify vehicle registration")
        print("3- Display registered vehicles and save them to a file ")
        print("4- Display daily charges and save them to a file")
        print("5- Remove a vehicle")
        print("6- Clear vehicles")
        print("0- Exit")
        menu_option = input(">>>")
        
        if menu_option == "1":
            register_vehicle1()
        elif menu_option == "2":
            authorize = check_password()
            if authorize == True:
                check_plate = input("Enter your plate number:")
                verify_vehicle2(check_plate)
        elif menu_option == "3":
            authorize = check_password()
            if authorize == True:
                display_vehicle3()
        elif menu_option == "4":
            authorize = check_password()
            if authorize == True:
                display_Charges4()
        elif menu_option == "5":
            authorize = check_password()
            check_plate = input("Enter your plate number:")
            if authorize == True:
                remove_vehicle5(check_plate)
        elif menu_option == "6":
            authorize = check_password()
            if authorize == True:
                clear_vehicle6()
        elif menu_option == "0":
            i = False
        else:
            print ("Invalid input")
            restart = input("Please Press enter to continue...")


print_menu()

#this is a test 
