import mysql.connector
import datetime
db=mysql.connector.connect(host='localhost',user='root',password='tiger',database='train',charset='utf8')
crs=db.cursor()
print('''                                              SOUTH WESTERN RAILWAYS
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                 HUBLI DIVISION
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                            Welcome To Belgaum Railway Station\'s Online Reservation Website
========================================================================'
HERE YOU CAN BOOK TICKETS FOR SPECIAL TRAINS SCHEDULED TO RUN FROM BELGAUM TO
DADAR ,PUNE JN. & BANGLORE CITY AND BACK SCHEDULED ON 25/12/2020

THE DETAILS OF TRAINS , FARES , AVAILABLE SEATS ARE GIVEN BELOW''')
print('TRAINS:')
print('(TRAIN_NO,              TRAIN                          ,    ORIGIN   , PF, DESTINATION, PF')
crs.execute('select* from trains;')
r=crs.fetchall()
for z in r:
    print(z,' ')
order=input('TYPE Y TO CONTINUE:')
while order=='Y':
    print('''SELECT THE CODE FOR THE OPERATION YOU WANT TO PERFORM
OPERATION        CODE
BOOK A TICKET      1
CANCEL TICKET      2''')
    a=int(input('ENTER CODE:'))
    if a==1:
        na=input('ENTER NAME:')
        g=input('GENDER (M/F):')
        age=int(input('ENTER AGE:'))
        print('SELECT BETWEEN SL , IIIAC, IIAC, IAC')
        c=input('SELECT CLASS:')
        tno=int(input('ENTER TRAIN NO.:'))
        int1=(tno,pnr,na,age,g,c)
        int2=(tno,)
        int3=(na,)
        print('NAME:',na,'        TRAIN NO.:',tno,'                 CLASS:',c)
        print('AGE:',age,'          GENDER',g)
        con=input('TO CONFIRM BOOKING PRESS Y:')
        if con=='Y':
            
            crs.execute('update seats set IIIAC=IIIAC-1 where TRAIN_NO=%s;',int2)
            db.commit()
            print('BOOKING SUCCESFULL')
            print('''SEAT NUMBER WILL BE AVAILABLE TO YOU AT THE BOARDING STATION
YOUR JOURNEY IS CONFIRMED''')
        else:
            print('PRINT TRY AGAIN')
    elif a==2:
        p=int(input('ENTER PNR NUMBER':))
        pn=(p,)
        crs.execute('SELECT* FROM PASSENGERS WHERE PNR_NO=%s;',p)
        print('DO YOU WANT TO CANCEL TICKET WITH ABOVE DETAILS?')
        c=input('IF YES TYPE Y:')
        crs.execute('')
        crs.execute('')
        print('TICKET CANCELLATION SUCCESFULL')
        print('REFUND AMOUNT WILL BE TRANSFERRED TO YOUR ACCOUNT AS SOON AS POSSIBLE')
