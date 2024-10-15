import pandas as pd
import mysql.connector as sql
# def connect():
conn=sql.connect(host='localhost',user='root',password=input('MySQL Password :-- '))
#   while True :
#     if conn.is_connected():
#       print('successfully connected')
#       break
#     else :
#       w=conn.cursor()
#       errorr=w.fetchwarnings()
#       print(errorr)
#       connect()
#       break

# connect()




# Empty lists
db_list = []

# Adds all databases in db_list
def check_db():
     sdb = "show databases;"
     c = conn.cursor()
     c.execute(sdb)
     data=c.fetchall ()
     for i in data:
          db_list.append(i)
          
          
# Creates new database
def create_db():
    cdb = "create database project"
    c = conn.cursor()
    c.execute(cdb)
     
# Uses exisiting database
def use_db():
     udb = "use project"
     c = conn.cursor()
     c.execute(udb)

# Checks if a db named hospital already exists
def unduplicate_db():
  while True:
    if ("project",) in db_list:
        use_db()
        break
    else:
        create_db()
        use_db()
        break

check_db()
unduplicate_db()

tb_list = []


def check_tb():
     sdb = "show tables;"
     c = conn.cursor()
     c.execute(sdb)
     data=c.fetchall()
     for i in data:
          tb_list.append(i)






# Creates Table patients
def create_tb_patient():
    ct = 'create table patient_details(p_id int not null auto_increment ,p_name varchar(25) ,p_age int(3),p_problems varchar(40),p_phono int(15),drf varchar(150),primary key(p_id))'
    c = conn.cursor()
    c.execute(ct)



# Checks if a tb named patients already exists
def unduplicate_patients_tb():
    while True: 

        if ("patient_details",) in tb_list:
            break
        else:
            create_tb_patient()
            break






#Doctor
def create_tb_doctors():
    ct = 'create table doctor_details(d_id int not null auto_increment primary key,d_name varchar(25),d_age int(3),d_department varchar(40),d_phono int(15))'
    c = conn.cursor()
    c.execute(ct)

    ctw = "INSERT INTO doctor_details (d_name,d_age,d_department,d_phono) VALUES ('Dr.ALi',39,'Ophthalmologist',0574327090),('Dr.Salman',64,'General physician ',0578678090),('Dr. Oliver Golder',56,'Pediatrician',0576536803),('Dr. Tristen Bliss',56,'Pulmonologist',0576536803),('Dr.Nadia',44,'Gynecologist',0576554333),('Dr.Aman',46,'Gastroenterologist',0576554333),('Dr.Suman',49,'Oncologist',0577654333),('Dr.Afaq',56,'General physician ',0578678090),('Dr.Arif',55,'General physician ',0578633440);"
    c.execute(ctw)



# Checks if a tb named doctor already exists
def unduplicate_doctors_tb():
    while True: 

        if ("doctor_details",) in tb_list:
            break
        else:
            create_tb_doctors()
            break







# Creates Table patients
def create_tb_Employee():
    ct = 'create table empolyee_details(w_id int not null auto_increment primary key,w_name varchar(25) ,w_age int(3),w_workname varchar(40),w_phono int(15))'
    c = conn.cursor()
    c.execute(ct)



# Checks if a tb named patients already exists
def unduplicate_Employee_tb():
    while True: 

        if ( "empolyee_details",) in tb_list:
            break
        else:
            create_tb_Employee()
            break


check_tb()

unduplicate_patients_tb()
unduplicate_doctors_tb()
unduplicate_Employee_tb()                                





     
c1=conn.cursor()
print('---------------------------------------------')
print('''                     

  _   _                 _ _        _     ____  ____  __  __ ____  
 | | | | ___  ___ _ __ (_) |_ __ _| |   |  _ \| __ )|  \/  / ___| 
 | |_| |/ _ \/ __| '_ \| | __/ _` | |   | | | |  _ \| |\/| \___ \ 
 |  _  | (_) \__ \ |_) | | || (_| | |   | |_| | |_) | |  | |___) |
 |_| |_|\___/|___/ .__/|_|\__\__,_|_|   |____/|____/|_|  |_|____/ 
                 |_|                                                                                                                                                                                                                                                     



''')
print('---------------------------------------------')

print('''           
❶.START
  ''')
print('''          
❷.EXIT



''')
choice=int(input(''' ENTER YOUR CHOICE:'''))



def RegPatient():
  p_name=input('Enter Patient Name:')
  p_age=int(input('Enter Age:'))
  print('''                
                                             --TREATEMENT's  AVAILAIBLE FOR-- 

     【 1】Eye irritation         【11】Stomach Aches          【21】Depression          【000】OTHERS          
     【 2】Runny nose             【12】Diarrhea               【22】Diabetes          
     【 3】fever (100° F)         【13】Asthma                 【23】Dry mouth
     【 4】headache               【14】Bronchitis             【24】Down's syndrome
     【 5】pain and fatigue       【15】Breast cancer          【25】Ear_ache
     【 6】sore throat            【16】Chest pain             【26】Earwax build-up
     【 7】cough                  【17】Chickenpox             【27】Endometriosis 
     【 8】Viral infection        【18】Chronic pain           【28】Eye cancer
     【 9】Menstrual cramps       【19】Constipation           【29】Flu
     【10】Pediatric              【20】Dehydration            【30】Gallstones 
     
      ''')
  p_problems=int(input('Enter the Problem/Disease by no. :'))
  if p_problems==1:
    p_problems="Eye irritation"
    drf='Dr.ALi'
  elif p_problems==2:
    p_problems="Runny nose"
    drf='Dr.Salman'
  elif p_problems==3:
    p_problems="Fever (100° F)"
    drf='Dr.Salman'
  elif p_problems==4:
    p_problems="headache" 
    drf='Dr.Salman'
  elif p_problems==5: 
    p_problems="pain and fatigue"
    drf='Dr.Salman'
  elif p_problems==6:
    p_problems="sore throat"
    drf='Dr.Salman'
  elif p_problems==7:
    drf='Dr.Salman'
    p_problems="cough"
  elif p_problems==8: 
    p_problems="Viral infection"
    drf='Dr.Arif'
  elif p_problems==9:
    p_problems="Menstrual cramps"
    drf='Dr.Nadia'
  elif p_problems==10:
    p_problems="Pediatric"
    drf='Dr.  Oliver Golder'
  elif p_problems==11:
    p_problems="Stomach Aches" 
    drf='Dr.Aman'
  elif p_problems==12:
    p_problems="Diarrhea"
    drf='Dr.Aman'
  elif p_problems==13: 
    p_problems="Asthma"
    drf='Dr.Tristen Bliss'
  elif p_problems==14:
    p_problems="Bronchitis"
    drf='Dr.Tristen Bliss'
  elif p_problems==15:
    p_problems="Breast cancer"
    drf='Dr.Suman'
  elif p_problems==16: 
    p_problems="Chest pain"
    drf='Dr.Tristen Bliss'
  elif p_problems==17:
    p_problems="Chickenpox"
    drf='Dr.Salman'
  elif p_problems==18:
    p_problems="Chronic pain"
    drf='Dr.Arif'
  elif p_problems==19: 
    p_problems="Constipation"
    drf='Dr.Aman'
  elif p_problems==20:
    p_problems="Dehydration"
    drf='Dr.Afaq'
  elif p_problems==21:
    p_problems="Depression"
    drf='Dr.Salman'
  elif p_problems==22: 
    p_problems="Diabetes"
    drf='Dr.Afaq'
  elif p_problems==23:
    p_problems="Dry mouth"
    drf='Dr.Aman'
  elif p_problems==24: 
    p_problems="Down's syndrome"
    drf='Dr.Afaq'
  elif p_problems==25: 
    p_problems="Ear_ache"
    drf='Dr.Salman'
  elif p_problems==26:
    p_problems="Earwax build-up"
    drf='Dr.Afaq'
  elif p_problems==27: 
    p_problems="Endometriosis"
    drf='Dr.Arif'
  elif p_problems==28:
    p_problems="Eye cancer"
    drf='Dr.Suman'
  elif p_problems==29:
    p_problems="Flu"
    drf='Dr.Afaq'
  elif p_problems==30: 
    p_problems="Gallstones"
    drf='Dr.Aman'
  elif p_problems==000:
    p_problems="General (OTHER)"
    drf='Dr.Arif'
  else:
    print("INVALID ENTERY")
  print ('Disease     -- '), print(p_problems)
  print ('Reffered to -- '), print(drf) 
  p_phono=int(input('Enter Moblie number:'))
  data1 =(p_name,p_age,p_problems,p_phono,drf)
  sql_insert="insert into patient_details (p_name,p_age,p_problems,p_phono,drf) values(%s,%s,%s,%s,%s)"
  c1.execute(sql_insert,data1)
  print('SUCCESSFULLY REGISTERED')
  conn.commit()

  plisttr = []
  sql_w='select*from patient_details where p_phono=("{}")'.format(p_phono)
  c1.execute(sql_w)
  r = c1.fetchall()
  for i in r :
    plisttr.append(i)
  df2 = pd.DataFrame(plisttr,columns=['ID','Name','AGE','Disease','PatientMobile','Reffered to - '])
  print(df2)
      
      
def RegDoctor():
  d_name=input('Enter Doctor Name:')
  d_age=int(input('Enter Age:'))
  d_department=input('Enter the Department:')
  d_phono=int(input('Enter Moblie number:'))
  data2 =(d_name,d_age,d_department,d_phono)
  sql_insert="insert into doctor_details (d_name,d_age,d_department,d_phono) values(%s,%s,%s,%s)"
  c1.execute(sql_insert,data2)
  print('successfully registered')
  conn.commit()

def Reg_Employee():
  w_name=input('Enter Employee Name:')
  w_age=int(input('Enter Age:'))
  w_workname=input('Enter type of work:')
  w_phono=int(input('Enter Moblie number:'))
  data3 =(w_name,w_age,w_workname,w_phono)
  sql_insert="insert into empolyee_details(w_name,w_age,w_workname,w_phono) values(%s,%s,%s,%s)"
  c1.execute(sql_insert,data3)
  print('successfully registered')
  conn.commit()

def pllisst():
    plistt = []
    sql_w='select*from patient_details'
    c1.execute(sql_w)
    r = c1.fetchall()
    for i in r:
        plistt.append(i)
    # print(plistt)
    df3 = pd.DataFrame(plistt,columns=['ID','Name','AGE','Disease','PatientMobile','Reffered to - '])
    print(df3)       

def dllisst():
    dlistt = []        
    sql_x="select*from doctor_details"
    c1.execute(sql_x)
    s=c1.fetchall()
    for i in s:
     dlistt.append(i)

    df2 = pd.DataFrame(dlistt,columns=['ID','Doctor_Name','Doctor_AGE','Department','Doctor_Moblie_Number'])
    print (df2)

def wllisst():

    wlistt = []

    sql_y="select*from empolyee_details"
    c1.execute(sql_y)
    t=c1.fetchall()
    for i in t:
        wlistt.append(i)

    df3 = pd.DataFrame(wlistt,columns=[ 'ID','Employee_Name', 'Employee_AGE','working_sector', 'Employee_Moblie_Number'])
    print (df3)
        
def sP_Detail():
      h=input("Enter Patients ID :")
      sql_w='select*from patient_details where p_id=("{}")'.format(h)
      c1.execute(sql_w)
      u = c1.fetchall()
      for i in u:
        print(i)
        
def sD_Detail():
      d=input("Enter Doctors ID:")
      sql_d='select*from doctor_details where d_id=("{}")'.format(d)
      c1.execute(sql_d)
      v=c1.fetchall()
      for i in v:
        print(i)
        
def sW_Detail():
      f=input("Enter Doctors ID:")
      sql_f='select*from empolyee_details where w_id=("{}")'.format(f)
      c1.execute(sql_f)
      w=c1.fetchall()
      for i in w:
        print(i)

def pmain():
    while True:
        print('''
        1. Registering Patient 
        2. Total patient
        3. Patient detail by ID
        4. Back''')
        choice=(input('ENTER YOUR CHOICE:'))
        if(choice=='1'):
            RegPatient()
        elif(choice=='2'):
            pllisst()
        elif(choice=='3'):
            sP_Detail()
        elif choice=='4':
            main()    
        else:
            print('INVALID ENTRY!')

def dmain():
    while True:
        print('''
        1. Registering Doctor 
        2. Total Doctor
        3. Doctor detail by ID
        4. Back''')
        choice=(input('ENTER YOUR CHOICE:'))
        if(choice=='1'):
            RegDoctor()
        elif(choice=='2'):
            dllisst()
        elif(choice=='3'):
            sD_Detail()
        elif choice=='4':
            main()    
        else:
            print('INVALID ENTRY!')

def Emain():
    while True:
        print('''
        1. Registering Empoloyee 
        2. Total Empoloyee
        3. Empoloyee detail by ID
        4. Back''')
        choice=(input('ENTER YOUR CHOICE:'))
        if(choice=='1'):
            Reg_Employee()
        elif(choice=='2'):
            wllisst()
        elif(choice=='3'):
            sW_Detail()   
        elif choice=='4':
            main()                
        else:
            print('INVALID ENTRY!')
            
                
def main():
    while True:
        print('''
        1. PATIENT
        2. DOCTORS
        3. EMOLOYEES
        4. Exit''')
        choice=(input('ENTER YOUR CHOICE:'))

        if choice=='1':
            pmain()
             
        elif choice=='2':
            dmain()
            
        elif choice=='3':
            Emain()
            
        elif choice=='4':
            exit()
            
        else:
            print('INVALID ENTRY!')
            
            
if choice==1:
  print('''                                                                      ╔═══════╦╦══════════════╗
                                                                      ║╔╦╦╗╔═╗║║ ╔═╗╔═╗╔══╗╔═╗║
                                                                      ║║║║║║╩╣║╚╗║╠╣║║║║║║║║╩╣║
                                                                      ║╚══╝╚═╝╚═╝╚═╝╚═╝╚╩╩╝╚═╝║
                                                                      ╚═══════════════════════╝''')
if choice==1:
  main()

elif choice==2:
    exit
    
else:
    print("INVALID ENTERY")