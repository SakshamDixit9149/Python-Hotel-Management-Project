def name_password(filenameup, USERNAME, PASSWORD):
    with open(filenameup, 'a') as file:
        file.write(USERNAME)
        file.write(PASSWORD)
        print("Your User Name and Password has been Saved Successfully.")


def customer_info(filenameci, customer_identification_number, customer_name, customer_address, customer_age, customer_country, customer_contact_number, customer_email):
    with open(filenameci, 'a') as file:
        file.write(customer_identification_number)
        file.write(customer_name)
        file.write(customer_address)
        file.write(customer_age)
        file.write(customer_country)
        file.write(customer_contact_number)
        file.write(customer_email)
        print("Your Data has been Saved Successfully.")


def booking_record(filenamebr, checkIN, checkOUT):
    with open(filenamebr, 'a') as file:
        file.write(checkIN)
        file.write(checkOUT)
        print("Your Check In and Check Out Details has been Successfully Saved!")


print(" JKET CONVENT SCHOOL ".center(82, "🌸"))
print(" HOTEL MANAGEMENT SYSTEM ".center(84, "🌸"))
print(" VRANDAVAN PLAZA ".center(80, "🌸"))
print(" DESIGNED AND MAINTAINED BY ".center(86, "🌸"))
print(" Saksham Class 11th ".center(82, "🌸"))
print(" ALL RIGHTS RESERVED ".center(82, "🌸"))
print("")
print("")
filenameup = input(
    "Enter the File Name in which you want to Save Your Username and Password : ")
USERNAME = input("ENTER THE USERNAME : ")
PASSWORD = input("ENTER THE PASSWORD : ")
name_password(filenameup, USERNAME, PASSWORD)
print("")
print("CONGRATULATION !! YOU HAVE SUCCESSFULLY REGISTERED ON PROGRAM")
print("")
while True:
    print("1--->ENTER CUSTOMER DETAILS".center(85, "🌹"))
    print("2--->BOOKING RECORD".center(81, "🌹"))
    print("3--->CALCULATE ROOM RENT".center(84, "🌹"))
    print("4--->CALCULATE RESTAURENT BILL".center(87, "🌹"))
    print("5--->CALCULATE GAMING BILL".center(85, "🌹"))
    print("6--->CALCULATE FASHION STORE BILL".center(88, "🌹"))
    print("7--->GENERATE TOTAL BILL AMOUNT".center(87, "🌹"))
    print("8--->EXIT".center(76, "🌹"))
    choice = input()
    if choice == "1":
        filenameci = input(
            "Enter the File Name in which you want to Save your Customer Data : ")
        customer_identification_number = input(
            "ENTER CUSTOMER IDENTIFICATION NUMBER:")
        customer_name = input("ENTER CUSTOMER NAME :")
        customer_address = input("ENTER CUSTOMER ADDRESS :")
        customer_age = int(input("ENTER CUSTOMER AGE :"))
        customer_country = input("ENTER CUSTOMER COUNTRY :")
        customer_contact_number = int(input("ENTER CUSTOMER CONTACT NUMBER :"))
        customer_email = input("ENTER CUSTOMER EMAIL :")
        print("NEW CUSTOMER ENTERED IN THE SYSTEM SUCCESSFULLY !")
        print("")
        print("")
        customer_info(filenameci, customer_identification_number, customer_contact_number,
                      customer_address, customer_age, customer_country, customer_name, customer_email)
        # if condition needed
    elif choice == "2":
        filenamebr = input(
            "Enter the File Name in which you want to Save your Booking Data : ")
        cid = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        checkIN = int(input("ENTER CUSTOMER CHECKIN DATE [ YYYY-MM-DD ] :"))
        checkOUT = int(input("ENTER CUSTOMER CHECKOUT DATE [ YYYY-MM-DD ] :"))
        print("CHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
    elif choice == "3":
        cid2 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        # if condition needed
        print(" WE HAVE FOLLOWING ROOMS AVAILABLE FOR YOU NOW ".center(80, "#"))
        print("""1. ULTRA ROYAL ----> 10000 RS.
                    2. ROYAL       ----> 5000 RS.
                    3. ELITE       ----> 3500 RS.
                    4. BUDGET      ----> 2500 USD""")
        option = int(input("ENTER YOUR OPTION : "))
        if option == 1:
            crn = int(input("ENTER CUSTOMER ROOM NO : "))
            nd = int(input(" ENTER NO. OF DAYS : "))
            print("")
            print("ULTRA ROYAL ROOM RENT :", 10000 * nd)
            print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd)
            print("YOUR TOTAL ROOM RENT IS:", 10000 * nd)
            rr = 10000*nd
            # roomrent.append(rr)
        elif option == 2:
            crn1 = int(input("ENTER CUSTOMER ROOM NO : "))
            nd1 = int(input(" ENTER NO. OF DAYS : "))
            print("")
            print("ROYAL ROOM RENT :", 5000 * nd1)
            print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd1)
            print("YOUR TOTAL ROOM RENT IS:", 5000 * nd1)
            rr1 = 5000 * nd1
            # roomrent.append(rr1)
        elif option == 3:
            crn2 = int(input("ENTER CUSTOMER ROOM NO : "))
            nd2 = int(input(" ENTER NO. OF DAYS : "))
            print("")
            print("ELITE ROOM RENT :", 3500 * nd2)
            print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd2)
            print("YOUR TOTAL ROOM RENT IS:", 3500 * nd2)
            rr2 = 3500 * nd2
            # roomrent.append(rr2)
        else:
            crn3 = int(input("ENTER CUSTOMER ROOM NO : "))
            nd3 = int(input(" ENTER NO. OF DAYS : "))
            print("")
            print("ULTRA ROYAL ROOM RENT :", 2500 * nd3)
            print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd3)
            print("YOUR TOTAL ROOM RENT IS:", 2500 * nd3)
            rr3 = 2500 * nd3
            # roomrent.append(rr3)
    elif choice == "4":
        cid3 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        print("""1. VEGETATION COMBO                  ----> 300 RS.
                     2. NON-VEGETATION COMBO              ----> 500 RS.
                     3. VEGETATION & NON-VEGETATION COMBO ----> 750 RS.""")
        order = int(input("ENTER YOUR ORDER :"))
        qty = int(input("ENTET QUANTITY / NO. OF PLATES :"))
        print("")
        if order == 3:
            print(" SO YOUR BILL IS :RS.", 750*qty)
            bq = 750*qty
            # restaurent.append(bq)
        elif order == 2:
            print(" SO YOUR BILL IS :RS.", 500 * qty)
            bq = 500 * qty
            # restaurent.append(bq)
        else:
            print(" SO YOUR BILL IS :RS.", 300 * qty)
            bq = 300 * qty
            # restaurent.append(bq)
        print("******* WE HOPE YOU WILL ENJOY YOUR MEAL ***********"
              "THANK YOU FOR VISITING COME AGAIN !!!")
        print("")
        print("")
        print("")
    elif choice == "5":
        cid4 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        print("")
        print("""    1. TABLE TENNIS                ----> 150 RS./HR
                         2. BOWLING                     ----> 100 RS./HR
                         3. SNOOKER                     ----> 250 RS./HR
                         4. VR WORLD GAMING(HEAD SET)   ----> 400 RS./HR
                         5. NORMAL VEDIO GAMES          ----> 300 RS./HR""")
        play = int(input("ENTER WHICH GAME WOULD YOU WANT TO PLAY :"))
        playhr = int(
            input("ENTER THE NO. OF HOURS IN WHICH YOU WANT TO PLAY :"))
        if play == 1:
            print("YOU WANT TO PLAY : TABLE TENNIS ")
            gb = 150*playhr
            print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
            print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
            # gaming.append(gb)
        elif play == 2:
            print("YOU WANT TO PLAY : BOWLING ")
            print("YOUR TOTAL BILL FOR", playhr, "IS:", 100 * playhr)
            print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
            gb = 100 * playhr
            # gaming.append(gb)
        elif play == 3:
            print("YOU WANT TO PLAY : SNOOKER ")
            gb = 250 * playhr
            print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
            print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
            # gaming.append(gb)
        elif play == 4:
            print("YOU WANT TO PLAY : VR WORLD GAMING(HEAD SET) ")
            gb = 400 * playhr
            print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
            print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
            # gaming.append(gb)
        elif play == 5:
            print("YOU WANT TO PLAY : NORMAL VEDIO GAMES` ")
            gb = 300 * playhr
            print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
            print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
            # gaming.append(gb)
            print("")
            print("")
            print("")
    elif choice == "6":
        cid5 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        print("""1. SHIRTS      ----> 450 RS.
                 2. T-SHIRTS    ----> 600 RS.
                 3. JEENS       ----> 500 RS.
                 4. TOP         ----> 500 RS.
                 5. GOWN        ----> 800 RS.
                 6. BLESER      ----> 5000 RS.""")
        wear = int(input("WHICH CLOTH WOULD YOU LIKE TO CHOOSE :"))
        buy = int(input("HOW MANY WANT TO BUY :"))
        print("")
        if wear == 1:
            print("")
            print("SHIRTS")
            print("YOU WANT", buy, "SHIRTS !!"
                  "SO YOUR TOTAL BILL IS :", 450*buy)
            fb = 450*buy
            # fashion.append(fb)
        elif wear == 2:
            print("")
            print("T-SHIRTS")
            print("YOU WANT", buy, "T-SHIRTS !!"
                  "SO YOUR TOTAL BILL IS :", 600*buy)
            fb = 600 * buy
            # fashion.append(fb)
        elif wear == 3:
            print("")
            print("JEENS")
            print("YOU WANT", buy, "JEENS !!"
                  "SO YOUR TOTAL BILL IS :", 500*buy)
            fb = 500 * buy
            # fashion.append(fb)
        elif wear == 4:
            print("")
            print("TOP")
            print("YOU WANT", buy, "TOP !!"
                  "SO YOUR TOTAL BILL IS :", 500*buy)
            fb = 500 * buy
            # fashion.append(fb)
        elif wear == 5:
            print("")
            print("GOWN")
            print("YOU WANT", buy, "GOWN !!"
                  "SO YOUR TOTAL BILL IS :", 800*buy)
            fb = 800 * buy
            # fashion.append(fb)
        elif wear == 6:
            print("")
            print("BLEASER")
            fb = 5000 * buy
            print("YOU WANT", buy, "BLEASER !!"
                  "SO YOUR TOTAL BILL IS :", fb)
            # fashion.append(fb)
    elif choice == "7":
        cid6 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        print("")
        print("******VRANDAVAN PLAZA******* CUSTOMER TOTAL BILLING*******")
        # print("CUSTOMER NAME :", customern)
        # print("ROOM RENT   : RS.", roomrent)
        # print("RESTAURENT BILL   : RS.", restaurent)
        # print("FASHION BILL   : RS.", fashion)
        # print("GAMING BILL   : RS.", gaming)
        print("")
        print("__________________________________________________")
        # print("TOTAL AMOUNT   : RS.", sum(roomrent+restaurent+fashion+gaming))
    elif choice == "9":
        break
