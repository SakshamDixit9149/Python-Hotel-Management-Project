cusinfo = []
roomrent = []
restaurent = []
cusid = []
gaming = []
fashion = []
print(" JKET CONVENT SCHOOL ".center(82, "🌸"))
print(" HOTEL MANAGEMENT SYSTEM ".center(84, "🌸"))
print(" VRANDAVAN PLAZA ".center(80, "🌸"))
print(" DESIGNED AND MAINTAINED BY ".center(86, "🌸"))
print(" Saksham Class 11th ".center(82, "🌸"))
print(" ALL RIGHTS RESERVED ".center(82, "🌸"))
print("")
print("")
USERNAME = input("ENTER THE USERNAME : ")
PASSWORD = input("ENTER THE PASSWORD : ")
cusinfo.append(USERNAME)
cusinfo.append(PASSWORD)
print("")
print("CONGRATULATION !! YOU HAVE SUCCESSFULLY REGISTERED ON PROGRAM")
print("")
while True:
    print("1--->ENTER CUSTOMER DETAILS".center(85, "🌹"))
    print("2--->BOOKING RECORD AND ROOM RENT".center(81, "🌹"))
    print("3--->CALCULATE RESTAURENT BILL".center(87, "🌹"))
    print("4--->CALCULATE GAMING BILL".center(85, "🌹"))
    print("5--->CALCULATE FASHION STORE BILL".center(88, "🌹"))
    print("6--->GENERATE TOTAL BILL AMOUNT".center(87, "🌹"))
    print("7--->EXIT".center(76, "🌹"))
    choice = input()
    if choice == "1":
        customer_identification_number = input(
            "ENTER CUSTOMER IDENTIFICATION NUMBER / CUSTOMER ID:")
        customer_name = input("ENTER CUSTOMER NAME :")
        customer_address = input("ENTER CUSTOMER ADDRESS :")
        customer_age = int(input("ENTER CUSTOMER AGE :"))
        customer_country = input("ENTER CUSTOMER COUNTRY :")
        contact_number = int(input("ENTER CUSTOMER CONTACT NUMBER :"))
        cusid.append(customer_identification_number)
        cusinfo.append(customer_name)
        cusinfo.append(customer_address)
        cusinfo.append(customer_age)
        cusinfo.append(customer_country)
        cusinfo.append(contact_number)
        print("NEW CUSTOMER ENTERED IN THE SYSTEM SUCCESSFULLY !")
        print("")
        print("")
        # if condition needed
    elif choice == "2":
        cid = input("ENTER CUSTOMER ID :")
        if cid in cusid:
            print(cusinfo)
            checkIN = int(
                input("ENTER CUSTOMER CHECKIN DATE [ YYYY-MM-DD ] :"))
            checkOUT = int(
                input("ENTER CUSTOMER CHECKOUT DATE [ YYYY-MM-DD ] :"))
            roomrent.append(checkIN)
            roomrent.append(checkOUT)
            print("CHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
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
                roomrent.append(rr)
            elif option == 2:
                crn1 = int(input("ENTER CUSTOMER ROOM NO : "))
                nd1 = int(input(" ENTER NO. OF DAYS : "))
                print("")
                print("ROYAL ROOM RENT :", 5000 * nd1)
                print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd1)
                print("YOUR TOTAL ROOM RENT IS:", 5000 * nd1)
                rr1 = 5000 * nd1
                roomrent.append(rr1)
            elif option == 3:
                crn2 = int(input("ENTER CUSTOMER ROOM NO : "))
                nd2 = int(input(" ENTER NO. OF DAYS : "))
                print("")
                print("ELITE ROOM RENT :", 3500 * nd2)
                print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd2)
                print("YOUR TOTAL ROOM RENT IS:", 3500 * nd2)
                rr2 = 3500 * nd2
                roomrent.append(rr2)
            else:
                crn3 = int(input("ENTER CUSTOMER ROOM NO : "))
                nd3 = int(input(" ENTER NO. OF DAYS : "))
                print("")
                print("ULTRA ROYAL ROOM RENT :", 2500 * nd3)
                print("THANK YOU, YOUR ROOM HAS BEEN BOOKED FOR :", nd3)
                print("YOUR TOTAL ROOM RENT IS:", 2500 * nd3)
                rr3 = 2500 * nd3
                roomrent.append(rr3)
        else:
            print("ERROR")
    elif choice == "3":
        cid2 = input("ENTER CUSTOMER ID :")
        if cid2 in cusid:
            print(cusinfo)
            print("""1. VEGETATION COMBO                  ----> 300 RS.
                        2. NON-VEGETATION COMBO              ----> 500 RS.
                        3. VEGETATION & NON-VEGETATION COMBO ----> 750 RS.""")
            order = int(input("ENTER YOUR ORDER :"))
            qty = int(input("ENTET QUANTITY / NO. OF PLATES :"))
            print("")
            if order == 3:
                print(" SO YOUR BILL IS :RS.", 750*qty)
                bq = 750*qty
                restaurent.append(bq)
            elif order == 2:
                print(" SO YOUR BILL IS :RS.", 500 * qty)
                bq = 500 * qty
                restaurent.append(bq)
            else:
                print(" SO YOUR BILL IS :RS.", 300 * qty)
                bq = 300 * qty
                restaurent.append(bq)
            print("******* WE HOPE YOU WILL ENJOY YOUR MEAL ***********"
                  "THANK YOU FOR VISITING COME AGAIN !!!")
            print("")
            print("")
            print("")
        else:
            print("ERROR")
    elif choice == "4":
        cid3 = input("ENTER CUSTOMER ID :")
        if cid3 in cusid:
            print(cusinfo)
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
                gaming.append(gb)
            elif play == 2:
                print("YOU WANT TO PLAY : BOWLING ")
                print("YOUR TOTAL BILL FOR", playhr, "IS:", 100 * playhr)
                print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
                gb = 100 * playhr
                gaming.append(gb)
            elif play == 3:
                print("YOU WANT TO PLAY : SNOOKER ")
                gb = 250 * playhr
                print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
                print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
                gaming.append(gb)
            elif play == 4:
                print("YOU WANT TO PLAY : VR WORLD GAMING(HEAD SET) ")
                gb = 400 * playhr
                print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
                print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
                gaming.append(gb)
            elif play == 5:
                print("YOU WANT TO PLAY : NORMAL VEDIO GAMES` ")
                gb = 300 * playhr
                print("YOUR TOTAL BILL FOR", playhr, "IS:", gb)
                print(" WE HOPE YOU WILL DO FUN WHILE GAMING ")
                gaming.append(gb)
                print("")
                print("")
                print("")
    elif choice == "5":
        cid4 = input("ENTER CUSTOMER ID :")
        if cid4 in cusid:
            print(cusinfo)
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
                fashion.append(fb)
            elif wear == 2:
                print("")
                print("T-SHIRTS")
                print("YOU WANT", buy, "T-SHIRTS !!"
                      "SO YOUR TOTAL BILL IS :", 600*buy)
                fb = 600 * buy
                fashion.append(fb)
            elif wear == 3:
                print("")
                print("JEENS")
                print("YOU WANT", buy, "JEENS !!"
                      "SO YOUR TOTAL BILL IS :", 500*buy)
                fb = 500 * buy
                fashion.append(fb)
            elif wear == 4:
                print("")
                print("TOP")
                print("YOU WANT", buy, "TOP !!"
                      "SO YOUR TOTAL BILL IS :", 500*buy)
                fb = 500 * buy
                fashion.append(fb)
            elif wear == 5:
                print("")
                print("GOWN")
                print("YOU WANT", buy, "GOWN !!"
                      "SO YOUR TOTAL BILL IS :", 800*buy)
                fb = 800 * buy
                fashion.append(fb)
            elif wear == 6:
                print("")
                print("BLEASER")
                fb = 5000 * buy
                print("YOU WANT", buy, "BLEASER !!"
                      "SO YOUR TOTAL BILL IS :", fb)
                fashion.append(fb)
    elif choice == "6":
        cid6 = input("ENTER CUSTOMER ID :")
        # print(cusinfo)
        print("")
        print("******VRANDAVAN PLAZA******* CUSTOMER TOTAL BILLING*******")
        print("CUSTOMER NAME :", customer_name)
        print("ROOM RENT   : RS.", roomrent)
        print("RESTAURENT BILL   : RS.", restaurent)
        print("FASHION BILL   : RS.", fashion)
        print("GAMING BILL   : RS.", gaming)
        print("")
        print("__________________________________________________")
        print("TOTAL AMOUNT   : RS.", sum(roomrent+restaurent+fashion+gaming))
    elif choice == "7":
        break
