import mysql.connector as a 
mycon=a.connect(host="localhost",user="root",passwd="password",database="db name")
cur=mycon.cursor()



def stdin():
    while(True):
        while(True):
            admn=input("\nEnter admission number:")
            try:
                n=0
                admn=int(admn)
                cur.execute("Select Admn from student")
                data=cur.fetchall()
                for i in data:
                    if admn in i:
                        n+=1
                if (n!=0):
                    print("Admission already exist try a new one!")
                    continue
            except ValueError:
                print("\nAdmission number can only be integer")
                print("Please try again")
                continue
            else:
                break
    
        name=input("Enter student name:")
        rollno=int(input("Enter student RollNO:"))
        DOB=input("Enter date of birth in (YYYY-MM-DD)format:")
        while(True):
            phone=input("Enter phone number:")
            if len(phone)==9:       
                try:
                    phone=int(phone)
                except ValueError:
                    print("Value can only be integer")
                    print("Please try again!")
                    continue
                else:
                    break
            else:
                print("Enter 10 numbers only!")
        add=input("Enter the Address:")
        fees=input("Enter paid or Notpaid:")
        clss=input("Enter the student class:")
        st="insert into student values({},'{}',{},'{}',{},'{}','{}','{}')".format(admn,name,rollno,DOB,phone,add,fees,clss)
        cur.execute(st)
        cur.execute("commit")
        cur.execute("select * from student where admn={}".format(admn))
        data=cur.fetchone()
        print("\n")
        print(data)
        print("\nRecord Sucessfully Inserted")
        ch=input("press any alphabet to continue insertion (or) press (n) to stop:").lower()
        if ch=="n":
            break

def teachin():
    while(True):
        while(True):
            sno=input("\nEnter serial number:")
            try:
                n=0
                sno=int(sno)
                cur.execute("Select sno from teacher")
                data=cur.fetchall()
                for i in data:
                    if sno in i:
                        n+=1
                if (n!=0):
                    print("\nserial already exist try a new one!")
                    continue
            except ValueError:
                print("\nserial number can only be integer")
                print("Please try again")
                continue
            else:
                break
        name=input("Enter teacher name:")
        DOB=input("Enter date of birth in (YYYY-MM-DD)format:")
        while(True):
            phone=input("Enter phone number:")
            if len(phone)==10:
                try:
                    phone=int(phone)
                except ValueError:
                    print("Value can only be integer")
                    print("Please try again!")
                    continue
                else:
                    break
            else:
                print("Enter 10 numbers only!")
        add=input("Enter the Address:")
        income=int(input("Enter income:"))
        qualification=input("Enter Qualification:")
        experiences=int(input("Enter Experience:"))
        st="insert into teacher values({},'{}','{}',{},'{}',{},'{}',{})".format(sno,name,DOB,phone,add,income,qualification,experiences)
        cur.execute(st)
        cur.execute("commit")
        cur.execute("select * from teacher where sno={}".format(sno))
        data=cur.fetchone()
        print("\n")
        print(data)
        print("\nRecord Sucessfully Inserted")
        ch=input("press any alphabet to continue insertion (or) press (n) to stop:").lower()
        if ch=="n":
            break

def attin():
    while(True):
        while(True):
            sno=input("\nEnter serial number:")
            try:
                n=0
                sno=int(sno)
                cur.execute("Select sno from teacher")
                data=cur.fetchall()
                for i in data:
                    if sno in i:
                        n+=1
                if (n!=0):
                    print("\nserial already exist try a new one!")
                    continue
            except ValueError:
                print("\nserial number can only be integer")
                print("Please try again")
                continue
            else:
                break
        name=input("Enter name:")
        DOB=input("Enter date of birth in (YYYY-MM-DD)format:")
        while(True):
            phone=input("Enter phone number:")
            if len(phone)==10:       
                try:
                    phone=int(phone)
                except ValueError:
                    print("Value can only be integer")
                    print("Please try again!")
                    continue
                else:
                    break
            else:
                print("Enter 10 numbers only!")
        add=input("Enter the Address:")
        income=int(input("Enter income:"))
        work=input("Enter work:")
        st="insert into attenders values({},'{}','{}',{},'{}',{},'{}')".format(sno,name,DOB,phone,add,income,work)
        cur.execute(st)
        cur.execute("commit")
        cur.execute("select * from attenders where sno={}".format(sno))
        data=cur.fetchone()
        print("\n")
        print(data)
        print("\nRecord Sucessfully Inserted")
        ch=input("press any alphabet to continue insertion (or) press (n) to stop:").lower()
        if ch=="n":
            break

def stdel():
    while (True):
        Admn=int(input("Enter the Admission No. to be deleted:"))
        st="Delete from student where Admn={}".format(Admn)
        cur.execute(st)
        cur.execute("commit")
        data=cur.fetchall()
        for row in data:
            print(row)
        print("Record Deleted Successfully")
        ch=input("press any alphabet to continue delete (or) press (n) to stop:").lower()
        if ch=="n":
            break

def teachdel():
    while (True):
        Sno=int(input("Enter the Serial No. to be deleted:"))
        st="Delete from teacher where sno={}".format(Sno)
        cur.execute(st)
        cur.execute("commit")
        data=cur.fetchall()
        for row in data:
            print(row)
        print("Record Deleted Successfully")
        ch=input("press any alphabet to continue delete (or) press (n) to stop:").lower()
        if ch=="n":
            break

def attdel():
    while (True):
        Sno=int(input("Enter the Serial No. to be deleted:"))
        st="Delete from attenders where sno={}".format(Sno)
        cur.execute(st)
        cur.execute("commit")
        data=cur.fetchall()
        for row in data:
            print(row)
        print("Record Deleted Successfully")
        ch=input("press any alphabet to continue delete (or) press (n) to stop:").lower()
        if ch=="n":
            break

def stdacc():
    while (True):
        admn=int(input("Enter the admn No. to access information:"))
        st="select * from student where admn={}".format(admn)
        cur.execute(st)
        data=cur.fetchall()
        for i in data:
            print(i)
        print("Record Accessed Successfully")
        ch=input("press any alphabet to continue access (or) press (n) to stop:").lower()
        if ch=="n":
            break

def teachacc():
    while (True):
        sno=int(input("Enter the serial No. to access information:"))
        st="select * from teacher where sno={}".format(sno)
        cur.execute(st)
        data=cur.fetchall()
        for row in data:
            print(row)
        print("Record Accessed Successfully")
        ch=input("press any alphabet to continue access (or) press (n) to stop:").lower()
        if ch=="n":
            break

def attacc():
    while (True):
        sno=int(input("Enter the serial No. to access information:"))
        st="select * from attenders where sno={}".format(sno)
        cur.execute(st)
        data=cur.fetchall()
        for row in data:
            print(row)
        print("Record Accessed Successfully")
        ch=input("press any alphabet to continue access (or) press (n) to stop:").lower()
        if ch=="n":
            break

def stdis():
    cur.execute("select * from student")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("Record Displayed Successfully")

def teachdis():
    cur.execute("select * from teacher")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("Record Displayed Successfully")

def attdis():
    cur.execute("select * from attenders")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("Record Displayed Successfully")

def stdup():
    while(True):
        while(True):
            admn=input("Enter the Admission no.:")
            try:
                admn=int(admn)
            except ValueError:
                print("\nAdmission number only contains numbers")
                print("Please try again....\n")
                continue
            else:
                break

        print("\n1.Name")
        print("2.Rollno.")
        print("3.DOB")
        print("4.Phone.no")
        print("5.Address")
        print("6.fees details")
        print("7.class")
        print("8.Stop")
        while(True):
            while(True):
                choice=input("Enter your choice:")
                try:
                    choice=int(choice)
                except ValueError:
                    print("\nNumbers only accepted")
                    print("Please try again....\n")
                    continue
                else:
                    break
            if(0<choice<9):
                break
            else:
                print("Invalid option enter the valid one!")
        if choice==1:
            name=input("Enter Name:")
            st="update student set name='{}' where Admn={}".format(name,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==2:
            rollno=int(input("Enter rollno.:"))
            st="update student set rollno={} where Admn={}".format(rollno,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==3:
            DOB=input("Enter Date Of Birth in (YYYY-MM-DD) format:")
            st="update student set dob='{}' where Admn={}".format(DOB,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==4:
            while(True):
                phone=input("Enter phone number:")
                if len(phone)==10:       
                    try:
                        phone=int(phone)
                    except ValueError:
                        print("Value can only be integer")
                        print("Please try again!")
                        continue
                    else:
                        break
                else:
                    print("Enter 10 numbers only!")
            st="update student set phone={} where Admn={}".format(phone,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==5:
            address=input("Enter Address:")
            st="update student set address='{}' where Admn={}".format(address,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==6:
            fees=input("Enter fees paid(or)Not paid:")
            st="update student set fees='{}' where Admn={}".format(fees,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==7:
            clss=input("Enter class:")
            st="update student set class='{}' where Admn={}".format(clss,admn)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        else:
            print("successfully stopped")
            break

def teachup():
    while(True):
        while(True):
            sno=input("Enter the Serial no.:")
            try:
                sno=int(sno)
            except ValueError:
                print("\nSerial number only contains numbers")
                print("Please try again....\n")
                continue
            else:
                break

        print("\n1.Name")
        print("2.DOB")
        print("3.Phone.no")
        print("4.Address")
        print("5.Income")
        print("6.Qualification")
        print("7.Experiences")
        print("8.Stop")
        while(True):
            while(True):
                choice=input("Enter your choice:")
                try:
                    choice=int(choice)
                except ValueError:
                    print("\nNumbers only accepted")
                    print("Please try again....\n")
                    continue
                else:
                    break
            if(0<choice<9):
                break
            else:
                print("Invalid option enter the valid one!")
        if choice==1:
            name=input("Enter Name:")
            st="update teacher set name='{}' where sno={}".format(name,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==2:
            DOB=input("Enter Date Of Birth in (YYYY-MM-DD) format:")
            st="update teacher set dob='{}' where sno={}".format(DOB,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==3:
            while(True):
                phone=input("Enter phone number:")
                if len(phone)==10:       
                    try:
                        phone=int(phone)
                    except ValueError:
                        print("Value can only be integer")
                        print("Please try again!")
                        continue
                    else:
                        break
                else:
                    print("Enter 10 numbers only!")
            st="update teacher set phonenumber={} where sno={}".format(phone,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==4:
            address=input("Enter Address:")
            st="update teacher set address='{}' where sno={}".format(address,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update(or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==5:
            income=int(input("Enter income:"))
            st="update teacher set income={} where sno={}".format(income,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue upate (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==6:
            qualification=input("Enter qualification:")
            st="update teacher set qualification='{}' where sno={}".format(qualification,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==7:
            experiences=input("Enter experiences:")
            st="update teacher set experiences='{}' where sno={}".format(experiences,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        else:
            print("successfully stopped")
            break

def attup():
    while(True):
        while(True):
            sno=input("Enter the Serial no.:")
            try:
                sno=int(sno)
            except ValueError:
                print("\nSerial number only contains numbers")
                print("Please try again....\n")
                continue
            else:
                break

        print("\n1.Name")
        print("2.DOB")
        print("3.Phone.no")
        print("4.Address")
        print("5.Income")
        print("6.Work")
        print("7.Stop")
        while(True):
            while(True):
                choice=input("Enter your choice:")
                try:
                    choice=int(choice)
                except ValueError:
                    print("\nNumbers only accepted")
                    print("Please try again....\n")
                    continue
                else:
                    break
            if(0<choice<8):
                break
            else:
                print("Invalid option enter the valid one!")
        if choice==1:
            name=input("Enter Name:")
            st="update attenders set name='{}' where sno={}".format(name,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==2:
            DOB=input("Enter Date Of Birth in (YYYY-MM-DD) format:")
            st="update attenders set dob='{}' where sno={}".format(DOB,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==3:
            while(True):
                phone=input("Enter phone number:")
                if len(phone)==10:       
                    try:
                        phone=int(phone)
                    except ValueError:
                        print("Value can only be integer")
                        print("Please try again!")
                        continue
                    else:
                        break
                else:
                    print("Enter 10 numbers only!")
            st="update attenders set phonenumber={} where sno={}".format(phone,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==4:
            address=input("Enter Address:")
            st="update attenders set address='{}' where sno={}".format(address,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==5:
            income=int(input("Enter income:"))
            st="update attenders set income={} where sno={}".format(income,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        elif choice==6:
            work=input("Enter Work:")
            st="update attenders set work='{}' where sno={}".format(work,sno)
            cur.execute(st)
            cur.execute("commit")
            data=cur.fetchall()
            for row in data:
                print(row)
            print("Record updated successfully")
            print("Do you want to continue?")
            ch=input("press any alphabet to continue update (or) press (n) to stop:").lower()
            if ch=="n":
                break
        else:
            print("successfully stopped")
            break





print("**********************************************")
print("\t \t ABC School")
print("**********************************************")
while(True):
    print("\n")
    print("1. Student Table")
    print("2. Teacher Table")
    print("3. Attenders Table")

    while(True):
        while(True):
            selection=input("Enter your choice:")
            try:
                selection=int(selection)
            except ValueError:
                print("\nNumbers only accepted")
                print("Please try again....\n")
                continue
            else:
                break
        if(0<selection<5):
            break
        else:
            print("Invalid option enter the valid one!\n")

    if selection==1:
        while(True):
            print("\n*******Student********")
            print("1. Insertion")
            print("2. Update")
            print("3. Delete")
            print("4. Access")
            print("5. Display")
            print("6. Back")
            while(True):
                while(True):
                    choice=input("Enter your choice:")
                    try:
                        choice=int(choice)
                    except ValueError:
                        print("\nNumbers only accepted")
                        print("Please try again....\n")
                        continue
                    else:
                        break
                if(0<choice<7):
                    break
                else:
                    print("invalid option enter the valid one!")            
            if choice==1:
                stdin()
            elif choice==2:
                stdup()
            elif choice==3:
                stdel()
            elif choice==4:
                stdacc()
            elif choice==5:
                stdis()
            else:
                break
                
    elif selection==2:
        while(True):
            print("\n*******Teacher********")
            print("1. Insertion")
            print("2. Update")
            print("3. Delete")
            print("4. Access")
            print("5. Display")
            print("6. Back")
            while(True):
                while(True):
                    choice=input("Enter your choice:")
                    try:
                        choice=int(choice)
                    except ValueError:
                        print("\nNumbers only accepted")
                        print("Please try again....\n")
                        continue
                    else:
                        break
                if(0<choice<7):
                    break
                else:
                    print("invalid option enter the valid one!\n")
            if choice==1:
                teachin()
            elif choice==2:
                teachup()
            elif choice==3:
                teachdel()
            elif choice==4:
                teachacc()
            elif choice==5:
                teachdis()
            else:
                break

    elif selection==3:
        while(True):
            print("\n*******Attenders********")
            print("1. Insertion")
            print("2. Update")
            print("3. Delete")
            print("4. Access")
            print("5. Display")
            print("6. Back")
            while(True):
                while(True):
                    choice=input("Enter your choice:")
                    try:
                        choice=int(choice)
                    except ValueError:
                        print("\nNumbers only accepted")
                        print("Please try again....\n")
                        continue
                    else:
                        break
                if(0<choice<7):
                    break
                else:
                    print("invalid option enter the valid one!\n")
            if choice==1:
                attin()
            elif choice==2:
                attup()
            elif choice==3:
                attdel()
            elif choice==4:
                attacc()
            elif choice==5:
                attdis()
            else:
                break
    else:
        break