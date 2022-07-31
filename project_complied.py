import sys #exit
import os 
import csv
import msvcrt as m
clear= lambda:os.system('cls')
hold= lambda: input()

F=open("Lib2.csv","r")
L=F.read()
D=L.replace(',',' ')
D=D.strip()  
R=D.split('\n')

main=[]
main.append(R[0].split())
for i in R[1::]: 
 i=i.split() 
 l1=[]
 l1.append(int(i[0]))
 l1.append(i[1])
 l1.append(int(i[2]))
 l1.append(int(i[3]))
 l1.append(i[4])
 main.append(l1)

f2=open("LG.csv","r")
l=f2.read()
d=l.replace(',',' ')
d=d.strip()  
r=d.split('\n')
d=dict() #{ lgid:pass}
for f in r[1::]:
 f=f.split()
 d[f[0]]=f[1]

def stud():
    lgid=input("LOGIN ID: ")
    if(lgid in d):
        pas=input("PASSWORD: ")
        if(d[lgid]==pas): 
            #prog 
            clear()
            sopt=0
            print("\t\t\tWelcome Student: ",lgid)
            while(sopt!=4):
                print("\n1.View Available Books\n2.Borrow Book\n3.Return Book\n4.Request Book\n5.Exit")
                sopt=int(input("Enter the option: "))
                if(sopt==1):
                 studview()
                 hold()
                 clear()
                elif(sopt==2):
                 borrow(lgid)
                 hold()
                 clear()
                elif(sopt==3):
                 ret()
                 hold()
                 clear()
                elif(sopt==4):
                 req(lgid)
                 hold()
                 clear()
                elif(sopt==5):
                 sys.exit()
                else:
                 print("Enter Valid Option ")            
        else:    
          print("Wrong Password")
          hold()
    else:
         print("LOGIN ID Not Found ")

         
def lgpass(id):
 ch=""
 pasword=d[id]
 l=[]
 print("PASSWORD:",end="")
 while(1==1):
     ch=m.getch()
     if(ch!=8 and ch!=13):
         print("*",end="")
         l.append(ch)
     elif(ch==8):
         print("\b\b",end="")
         l.pop()
     elif(ch==13):
         l.append("\0")
     else: #enterkey
         break
 res=reduce(str.__add__,l)
 if(res==password):
     return True
 else:
     return False



    
def studview():
    print("\n",main[0][0],main[0][1],main[0][3])
    for i in main:
        if(i[4]=='1'): #if 1 then available
          print(i[0],i[1],i[3])

def borrow(sid):
    studview()
    b=int(input("Enter slno of book you want to borrow"))
    res=list(filter(lambda s:s[4]=='1',main))
    flag=0
    for u in res:
        if(b==u[0]):
            flag=1
            break
    if(flag==1):
     for i in main:
         if(b==i[0]):
             print("The details of the book you want to borrow are:")
             print(i[0],i[1],i[3])
             break
     c=input("Are you sure you want to borrow (Y/N)")
     if(c=='Y' or c=='y'):
        for i in main:
         if(b==i[0]):
             main[main.index(i)][4]=sid
             with open('Lib2.csv', 'w+', newline='') as file: #w-write(appends,opens a file then appends) #read (reads the file)
              writer = csv.writer(file)
              writer.writerows(main) #feeds list            
             break
     elif(c=='N' or c=='n'):
         borrow(id) #try
     else:
          print("Enter Valid Input")
          
def ret():
    b=int(input("Enter slno of book you want to return: "))
    res=list(filter(lambda s:s[4]!='1',main))
    flag=0
    for u in res:
        if(b==u[0]):
            flag=1
            break
    if(flag==1):
     for i in main:
         if(b==i[0]):
             print("The details of the book you want to return are:")
             print(i[0],i[1],i[3])
             break
     c=input("Are you sure you want to return (Y/N)")
     if(c=='Y' or c=='y'):
        for i in main:
         if(b==i[0]):
             main[main.index(i)][4]='1'
            # print(main) no problem here
             with open('Lib2.csv', 'w+', newline='') as file:
              writer = csv.writer(file)
              writer.writerows(main)
             break
     elif(c=='N' or c=='n'):
         ret()
     else:
          print("Enter Valid Input")
           
    else:
          print("Enter Valid Input")
    
def req(sid):
    c=input("Enter Title of Book you want to request ")
    c=c+"req by~"+sid
    f=open("Req.txt","w")
    f.write(c)
    f.close()

def tea():
    lgidt=input("LOGIN ID: ")
    if(lgidt in d):
        past=input("PASSOWRD: ")
        if(d[lgidt]==past):
            #prog 
            clear()
            topt=0
            print("\t\t\tWelcome Faculty: ",lgidt)
            while(topt!=4):
                print("\n1.View Available Books\n2.Borrow Book\n3.Return Book\n4.Request Book\n5.Exit")
                topt=int(input("Enter the option: "))
                if(topt==1):
                 teaview()
                elif(topt==2):
                 teaborrow(lgidt)
                elif(topt==3):
                 tearet()
                elif(topt==4):
                 req(lgidt)
                elif(topt==5):
                 sys.exit() 
                else:
                 print("Enter Valid Option ")            
        else:    
          print("Wrong Password")
    else:
         print("LOGIN ID Not Found ")

def teaview():
    print("\n",main[0][0],main[0][1],main[0][3])
    for i in main:
     print(i)

def teaborrow(id):
    studview()
    b=int(input("Enter slno of book you want to borrow"))
    res=list(filter(lambda s:s[4]=='1',main))
    flag=0
    for u in res:
        if(b==u[0]):
            flag=1
            break
    if(flag==1):
     for i in main:
         if(b==i[0]):
             print("The details of the book you want to borrow are:")
             print(i[0],i[1],i[3])
             break
     c=input("Are you sure you want to borrow (Y/N)")
     if(c=='Y' or c=='y'):
        for i in main:
         if(b==i[0]):
             main[main.index(i)][4]=id
             with open('Lib2.csv', 'r+', newline='') as file:
              writer = csv.writer(file)
              writer.writerows(main)
             break
     elif(c=='N' or c=='n'):
         teaborrow(id)
     else:
          print("Enter Valid Input")
     
def teareturn():
    b=int(input("Enter slno of book you want to return: "))
    res=list(filter(lambda s:s[4]!='1',main))
    print(res)
    flag=0
    for u in res:
        if(b==u[0]):
            flag=1
            break
    if(flag==1):
     for i in main:
         if(b==i[0]):
             print("The details of the book you want to return are:")
             print(i[0],i[1],i[3])
             break
     c=input("Are you sure you want to return (Y/N)")
     if(c=='Y' or c=='y'):
        for i in main:
         if(b==i[0]):
             main[main.index(i)][4]='1'
             with open('Lib2.csv', 'r+', newline='') as file:
              writer = csv.writer(file)
              writer.writerows(main)
             break
    elif(c=='N' or c=='n'):
         ret() 
    else:
          print("Enter Valid Input")

def lib():
     lgi=input("LOGIN ID: ")
     if(lgi in d):
        pasl=input("PASSOWRD: ")
        if(d[lgi]==pasl):
            #prog 
            clear()
            lopt=0
            print("\t\t\tWelcome Librarian: ",lgi)
            while(lopt!=4):
                print("\n1.View Books\n2.Edit Book List\n3.View Requested Books\n4.Exit") 
                lopt=int(input("Enter the option: "))
                if(lopt==1):
                 libview()
                elif(lopt==2):
                 edit()
                elif(lopt==3):
                  yes()
                elif(lopt==4):
                 viewreq()
                else:
                 print("Enter Valid Option ")            
        else:    
          print("Wrong Password")
     else:
         print("LOGIN ID Not Found ")

def libview():
    for i in main:
        print (i)

        

def edit():
    c=input("Enter sl no of book to edit")
    
#main has all data
opt=0
while(opt!=4):
    clear()
    print("\t\t\tWELCOME TO LIB SOFTWARE")
    print("1.Student\n2.Teacher\n3.Librarian\n4.Exit")
    opt=int(input("Enter the option "))
    if(opt==1): 
     clear()
     stud()
    elif(opt==2):
      clear()
      tea()
    elif(opt==3):
      clear()
      lib()
    elif(opt==4):
     sys.exit()
    else:
        print("Enter Valid Input")
        hold()
        
