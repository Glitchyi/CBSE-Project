# imports---------------------

import mysql.connector as c
import csv
from random import randint as rint

# OUT OF SYLABUSS (～￣▽￣)～

import smtplib, ssl
import os
import time

# Functions--------------------

# noinspection PyBroadException
def main():
    print ("Choose Category".upper())
    print("---------------")
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
def food():
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
        ch = enter_correct("Choose the option: ",1)
        if ch == 1:
            add()
        elif ch == 2:
            x=enter_correct("Fno: ",1)
            delete(x)
        elif ch == 3:
            update()
        elif ch==4:
            display()
        elif ch == 5:
            search(enter_correct("Enter Food No or Food Name: ",1))
        elif ch == 6:
            main()
        else:
            print("\n--------------\nInvalid Option\n--------------")

#---------------------------------

def customer():
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

def enter_correct(var_msg,var=0):
    val = input(var_msg)
    if var==1:
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
            if rint(0,10000)==420:
                print("Mistakes Happen")
            else:
                print("\n--------------\nInvalid Option\n--------------\n")
            enter_correct(var_msg)
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

def add():
    x=enter_correct("Enter Food ID: ",1)
    cur.execute("select fno from food;")
    for i in cur.fetchall():
        if x == i[-1]:
            print("\nThis ID Already Exists\n")
            time.sleep(3)
            food()

    y = enter_correct("Enter Food Name: ")
    z = enter_correct("Enter Food Type: ")
    w=enter_correct("Enter Price: ",1)
    cur.execute("insert into food values({},'{}','{}',{});".format(x, y, z,w))
    con.commit()

# ------------------------------

# Delete -----------------------------

def delete(fno):
    cur.execute(f"select * from food where fno = {fno};")

    for i in cur.fetchall():
        for j in i:
            print(j, end=" ")
        print("\n")
    waste = enter_correct("""Are you sure you want to delete
    Press enter to confirm/press b and enter to go back: """.title())
    if waste.upper() == "B":
        food()
    cur.execute("delete from food where fno = {};".format(fno))
    con.commit()

# ------------------------------

# Display------------------------------

def display():
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
        print("That's folks!")

#------------------------------

# Search ------------------------------

def search(f_info):
    cur.execute("select * from food where fno like '%{}%' or fname like '%{}%';".format(f_info,f_info))
    if len(cur.fetchall())==0:
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

def update():
    fno = enter_correct("Enter Food ID: ",1)
    x=0
    try:
        cur.execute(f"select * from food where fno like {fno};")
        x = cur.fetchall()
    except c.errors as err:
        print("Errer",print(str(err)))
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
    con.commit()

#--------------------------------

# Customer Relations---------------------

def customs(customer_name):
    with open('customer.csv',newline='',mode='a+') as file:
        writer = csv.writer(file)
        t = time.localtime()
        current_time = time.strftime("%I:%M:%S %p , %d/%m/%Y", t)    # recording the time
        the_bill={}                                                # initialising the bill
        if enter_correct(f"Proceed Billing Of {customer_name}: ").lower()=='y':
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
                    if len(res) == 0:
                        print("\n")
                        print("Invalid Search Query Or List Is Empty.")
                        print("If Not, Try Checking The Food Number")
                        time.sleep(2.5)
                        print("returning to previous menu\n".title())
                        time.sleep(1)
                        customer()
                    else:
                        print('\n',res[0],'\n')
                        qun=enter_correct("Enter quantity: ",1)
                        the_bill[qun]=res[0]
        reader=csv.reader(file)
        writer.writerow([len(list(reader))+1,current_time,customer_name,the_bill])
        print("Success")
        time.sleep(2)

def customs_read():
    with open('customer.csv',newline='',mode='r') as file:
        reader = csv.reader(file)
        if os.stat('D:\Advaith\Python\Project\customer.csv').st_size > 0:
            pass
        else:
            print("\n\nempty file".title())
            customer()
        for i in reader:
            #if i[0]==sno:
            print(i)
        print("Success")
        time.sleep(2)


#-----------------------------

# Connector ------------------------------

con = c.connect(host="localhost", user="root", passwd="1234", database="lakochi")
cur = con.cursor()

#-----------------------------

# Bills-----------------------

def mail(email_id,bill):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "thelakochi@gmail.com"  # Enter your address
    receiver_email = f"{email_id}"  # Enter receiver address
    password = "thelakochi"
    message = f"""\
    Subject: Bill Recipt From The La Kochi Hotel ^_^

    {bill}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#-----------------------------

# Intro-------------------------

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