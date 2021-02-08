# imports---------------------

import mysql.connector as c
import csv

# OUT OF SYLABUSS (～￣▽￣)～

import smtplib, ssl
import os
import time

# Functions--------------------

# noinspection PyBroadException
def main():                                                                 # This is the main function  and is where the program starts from.
    print ("Choose Category".upper())
    print("---------------")                                                # The main categories
    print("1. FOOD")
    print("2. CUSTOMER")
    print("3. BILLING")
    print("4. EXIT")
    choice = enter_correct("Enter The Option: ",1)
    if choice==1:
        food()
    elif choice==2:
        customer()
    elif choice==4:
        print("Are You sure to exit?")
        dump=enter_correct("Enter Y : ")
        if (dump.upper()).strip()=='Y':
            exit("Succesfully exited program")

#---------------------------------
def food():                                                                  # Function deals with all functions that alter the table food and its contents
    while True:
        print("\n")
        print("FOOD")
        print("---------")
        print("Options:")
        print("1. Add Food Details ")
        print("2. Delete Food Details ")
        print("3. Update Food Details ")
        print("4. Display Food items ")
        print("5. Search Food Details ")
        print("6. Back")
        choice = enter_correct("Choose the option: ",1)
        if choice == 1:
            add()
        elif choice == 2:
            x=enter_correct("Fno: ",1)
            delete(x)
        elif choice == 3:
            update()
        elif choice ==4:
            display()
        elif choice == 5:
            search(enter_correct("Enter Food No or Food Name: ",1))
        elif choice == 6:
            main()
        else:
            print("\n--------------\nInvalid Option\n--------------")

#---------------------------------

def customer():                                                                         # Function deals with all things related to the customer and the billing of his order.
    while True:     
        print("\n")
        print("CUSTOMER")
        print("---------")
        print("1. Add Customer Details And Bill Details")
        print("2. View Details")
        print("3. Back")
        ch = enter_correct("Enter Option: ",1)
        if ch==1:
            customs(enter_correct("Enter the name of the customer: "))
        elif ch==2:
            customs_read()
        elif ch==3:
            main()

#----------------------------

# Patent Pending ヾ(≧▽≦*)o-------------------

# noinspection PyBroadException

def enter_correct(var_msg,var=0):                                                       # This function prevents the program from crashing with any errors that occur in the program it solves them,
    val = input(var_msg)                                                                # or returns to the main program.
    if var==1:                                                                          # This is also a failsafe to abort the current action and return to the main program
        try:
            if (val.lower()).strip() == 'quit':
                print("\n------------------------")
                print("Aborting Current Process")
                time.sleep(1)
                print("Returning To Main Program")
                print("------------------------\n")
                time.sleep(1)
                main()
            val = int(val)
        except:
            print("\n--------------\nInvalid Option\n--------------\n")

        return val
    else:
        if (val.lower()).strip() == 'quit':
            print("\n------------------------")
            print("Aborting Current Process")
            time.sleep(1)
            print("Returning To Main Program")
            print("------------------------\n")
            time.sleep(1)
            main()
        return val

#-------------------------------

# Add------------------------------

def add():                                                                  # This function helps us add a new food item to the table, it checks the wether a simmilar entry exists or not, 
(    x = enter_correct("Enter Food ID: ",1)                                 # and if not gives us an option to add it to the food menu.
    cur.execute("select fno from food;")
    for i in cur.fetchall():
        if x == i[-1]:
            print("\nThis ID Already Exists\n")
            time.sleep(3)
            food()

    y = enter_correct("Enter Food Name: ")
    z = enter_correct("Enter Food Type: ")
    w = enter_correct("Enter Price: ",1)
    cur.execute("insert into food values({},'{}','{}',{});".format(x, y, z,w))
    del x,y,z,w
    con.commit()

# ------------------------------

# Delete -----------------------------

def delete(fno):                                                            # This function deals with the deletion of a food record from the menu.
    cur.execute(f"select * from food where fno = {fno};")

    for i in cur.fetchall():
        for j in i:
            print(j, end=" ")
        print("\n")
    waste = enter_correct("""Are you sure you want to delete
    Press enter to confirm/press b and enter to go back: """.title())
    if waste.upper() == "B":
        food()
    del waste
    cur.execute("delete from food where fno = {};".format(fno))
    con.commit()

# ------------------------------

def display():                                                              # Displays the entire menu of hotel.
    print("\n")
    dash = 0
    cur.execute("select * from food")
    na = cur.fetchall()
    if len(na) == 0:
        print("""
                        _____________________
                      /                 `   |
                      |  .-----------.  |   |-----.
                      |  |           |  |   |-=---|
                      |  | No one    |  |   |-----|
                      |  | Found  !  |  |   |-----|
                      |  |           |  |   |-----|
                      |  `-----------'  |   |-----'/|
                       \________________/___'     /  |
                          /                      / / /
                         / //               //  / / /
                        /                      / / /
                       / _/_/_/_/_/_/_/_/_/_/ /   /
                      / _/_/_/_/_/_/_/_/_/_/ /   /
                     / _/_/_/_______/_/_/_/ / __/
                    /______________________/ /    
                    \______________________\/
                    """)
        food()

    print("The following details will be printed out in the following maner:\n")
    print("FOOD ID \t FOOD NAME \t Type \t Price".upper())
    print("---------------------------------------")
    for i in na:
        print("\n", end="")
        for j in i:
            print(j, end="     |     ")
            dash += len(i)
        print("\n")
        print("---------------------------------------------------------------------------")
    else:
        del dash, na
        print("That's folks!")

#------------------------------

 
 def search(f_info):
    cur.execute("select * from food where fno like '%{}%' or fname like '%{}%';".format(f_info,f_info))     # This function helps to search for a specific food item and if it doesn't exist,
    if len(cur.fetchall())==0:                                                                              # it informs the user and returns to the previous menu.
        print("\n")
        print("Invalid Search Query Or List Is Empty.")
        print("If Not, Try Checking The Spelling Or The Food Number")
        time.sleep(1)
        print("returning to previous menu\n".title())
        time.sleep(1)

    else:
        cur.execute("select * from food where fno like '%{}%' or fname like '%{}%';".format(f_info,f_info))
        print("\n")
        for i in cur.fetchall():
            for j in i:
                print(j, end=" ")
            print("\n")
    con.commit()
    food()

#------------------------------

# Update------------------------------

def update():                                                           # Update function helps with the updation of a food item in the menu.
    fno = enter_correct("Enter Food ID: ",1)
    x=0
    try:
        cur.execute(f"select * from food where fno like {fno};")
        x = cur.fetchall()
    except c.errors as err:
        print("Error",print(str(err)))
    if len(x) == 0:
        print("\n")
        print("Invalid Search Query Or List Is Empty.")
        print("If Not, Try Checking The Food Number")
        time.sleep(2.5)
        print("returning to previous menu\n".title())
        time.sleep(1)
        food()
    for i in x:
        print("\n\nSure you want to update this entry: ")
        print(i)
    ch = enter_correct("Enter y to continue: ")
    if ch.lower() == 'y':
        pass
    else:
        print("\n\nReturning Back")
        food()
    fname = enter_correct("Enter Food Name: ")
    ftype = enter_correct("Enter Food Type: ")
    price = enter_correct("Enter Price: ",1)
    cur.execute(f"update food set fno={fno},fname='{fname}',type'{ftype}',price={price});")
    del x,ch,fname,ftype,price
    con.commit()

#--------------------------------

# Customer Relations---------------------
 
 
def customs(customer_name):                                                 #This function deals with the customer details includind the time of checkout
    with open('customer.csv', newline='', mode='r') as file2:
        row_count = len(list(csv.reader(file2, delimiter=","))) + 1
        file2.close()
    with open('customer.csv',newline='',mode='a+') as file:
        writer = csv.writer(file)
        t = time.localtime()
        current_time = time.strftime("%I:%M:%S %p , %d/%m/%Y", t)    # recording the time
        the_bill={}                                                # initialising the bill
        if enter_correct(f"Proceed Billing Of {customer_name}: ").lower()!='y':
            customer()
        else:
            while True:
                fno = enter_correct("Enter Food Number: ", 1)
                if fno == 0:
                    break
                else:
                    try:
                        cur.execute(f"select * from food where fno like {fno};")
                        res = cur.fetchall()
                    except c.errors:
                        pass
                    if len(res) != 0:
                        print('\n', res[0], '\n')
                        qun = enter_correct("Enter quantity: ", 1)
                        the_bill[res[0][0]] = [qun,res[0][1],res[0][2],res[0][3]]
                    else:
                        print("\n")
                        print("Invalid Search Query Or List Is Empty.")
                        print("If Not, Try Checking The Food Number")
                        time.sleep(2.5)
                        print("returning to previous menu\n".title())
                        time.sleep(1)
                        customer()
        billprint(the_bill)
        writer.writerow([row_count,current_time,customer_name,the_bill])
        del writer,t,current_time,the_bill,res,qun
        print("Success")
        time.sleep(2)


# noinspection PyBroadException
def billprint(bill):                                                                #This function is used to print the bill according to the above done entries in a structural manner
    global names
    cur.execute("select fname from food;")
    try:
        names=cur.fetchall()
    except:
        print("nothing")
        customer()
    x = 0
    for i in names:
        for j in i:
            if len(j) > x:
                x = len(j)

    print('-' * (x+40))
    print('|' + "LA KOCHI".center(x+38) + '|')
    print('-' * (x + 40))
    print("| Slno    Food name" + " "*(x-7) + "Qty    Unit Price    Price |")

    l=[]

    for i in bill.keys():
        cur.execute(f"select price from food where fname=\"{ bill[i][1] }\";")

        Food_Name=str(bill[i][1])+" "*(x+1-len(bill[i][1]))

        Unit_Price = cur.fetchall()[0][0]

        Final_Price= Unit_Price*(bill[i][0])
        l.append(Final_Price)

        Unit_Price = str(Unit_Price) + " "*(13-len(str(Unit_Price)))

        Final_Price= str(Final_Price) + " "*(6-len(str(Final_Price)))

        Quantity=str(bill[i][0])+" "*(6-len(str(bill[i][0])))

        print(f"| {i}"+" "*(7-len(str(i))) , Food_Name , Quantity,Unit_Price,Final_Price,end="|\n")

    TOTAL=0

    for j in l:
        TOTAL+=j

    print('-' * (x + 40))

    print("| TOTAL" + " " * (x + 30 - len(str(TOTAL) )) + f"{TOTAL}  |")

    print('-' * (x + 40))
    print("| HOPE YOU HAVE A WONDERFUL DAY AHEAD (*^▽^*)"+" "* (x - 6)+'|')
    print('-' * (x + 40))

    # Mail------------------------------------------

    ask=enter_correct("\nDo you Want the bill to be mailed to you?: ")


    if (ask.upper()).strip()=='Y':

        Body=str('-' * (x + 40))+'\n'
        Body+=str('|' + "LA KOCHI".center(x + 38) + '|')+'\n'
        Body+=str('-' * (x + 40))+'\n'
        Body+=str("| Slno    Food name" + " " * (x - 7) + "Qty    Unit Price    Price |")+'\n'

        l = []

        for i in bill.keys():
            cur.execute(f"select price from food where fname=\"{bill[i][1]}\";")

            Food_Name = str(bill[i][1]) + " " * (x + 1 - len(bill[i][1]))

            Unit_Price = cur.fetchall()[0][0]

            Final_Price = Unit_Price * (bill[i][0])
            l.append(Final_Price)

            Unit_Price = str(Unit_Price) + " " * (13 - len(str(Unit_Price)))

            Final_Price = str(Final_Price) + " " * (6 - len(str(Final_Price)))

            Quantity = str(bill[i][0]) + " " * (6 - len(str(bill[i][0])))

            Body+= f"| {i}{' ' * (7 - len(str(i)))} {Food_Name} {Quantity} {Unit_Price} {Final_Price}|\n"

        TOTAL = 0

        for j in l:
            TOTAL += j

        Body+=('-' * (x + 40))+'\n'

        Body+=("| TOTAL" + " " * (x + 30 - len(str(TOTAL))) + f"{TOTAL}  |")+'\n'

        Body+=('-' * (x + 40))+'\n'
        Body+=("| HOPE YOU HAVE A WONDERFUL DAY AHEAD (*^v^*)" + " " * (x - 6) + '|')+'\n'
        Body+=('-' * (x + 40))+'\n'
        mailid=enter_correct("Please Enter Your Email ID: ")
        mail(mailid,Body)

#-----------------------------------------

def customs_read():                                                         #Function helps to save the bill as ac csv file  to the hard disk of the computer
    with open('customer.csv',newline='',mode='r') as file:
        reader = csv.reader(file)
        if os.stat('customer.csv').st_size > 0:
            pass
        else:
            print("\n\nempty file".title())
            customer()
        for i in reader:
            print(i[1])
            print(i[2])
            print(i[3])
        print("Success")
        time.sleep(2)


#-----------------------------

# Connector ------------------------------

con = c.connect(host="localhost", user="root", passwd="1234", database="lakochi")
cur = con.cursor()

#-----------------------------

# Bills-----------------------

def mail(email_id,bill):                                                #This function will sent the bill to the intended recipient's email id
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "thelakochi@gmail.com"  # Enter your address
    receiver_email = str(email_id)  # Enter receiver address
    password = "thelakochi"
    message = f"""\
    Bill Recipt From The La Kochi Hotel ^_^

    {bill}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#-----------------------------

# This is the introduction part of the program
#all below include the part of the design

print("""

    █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀
    █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░
    
    █░░ ▄▀█   ▄▄   █▄▀ █▀█ █▀▀ █░█ █
    █▄▄ █▀█   ░░   █░█ █▄█ █▄▄ █▀█ █
""")
print("""
       __                        @@;,                {_}
      (  ;          ?           :  );                |(|
     _| |_  |  |   ||  |  |     _| |_                |=|
    |  \  \  \/    ||   \/ ___ /  /  |              /   |
  __|   |\ __||____||___||______/|   |              |.--|
  |||   | |_______    _________| |   |||            ||  |
  |||   |____     |   |      ____|   |||            ||  |    .    ' .    
  \ \______  )    |   |     /  ______/ /            |'--|  '     \~~~/
   ||    | | |    |   |    /___|     ||             '-=-' \~~~/   \_/  
   ||    | | |_  /| | |\   _| ||     ||                    \_/     Y
   ||    | \__, / | | |  \<__/ |     ||                     Y     _|_
                                                           _|_       
""")
# This is very important---
while True:
    print("""\n------------------------------------------------------------------------------------------------------\n""")
    main()
