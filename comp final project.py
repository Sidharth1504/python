from cgitb import text
from distutils.sysconfig import get_makefile_filename
import random
from tkinter import *
from tkinter import messagebox
from tkinter import font
from urllib import response
import csv  
fc=open('customer.csv','a+',newline='')
fa=open('administrator.csv','a+',newline='')
cwriter=csv.writer(fc)
awriter=csv.writer(fa)
creader=csv.reader(fc)
areader=csv.reader(fa)
root=Tk()
root.configure(bg='Orangered2')
titlelabel=Label(root,text='Courier Management Service',font=('Lucida calligraphy',36,'bold'),bg='Orangered2')
titlelabel.grid(row=0,column=0,columnspan=2) 
def Response():
    f6666=open('customer1.csv','r')
    f7777=open('customer3.csv','w',newline='')
    c6reader=csv.reader(f6666)
    c6writer=csv.writer(f7777)
    crec6=Toplevel() 
    crec6.configure(bg='grey15')
    r6=Response11.get()
    u2=user121.get()
    p2=passwd121.get()
    for rec in c6reader:
        if rec[1]==u2 and rec[2]==p2:
            l=[rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],r6]
            c6writer.writerow(l)
        else:
            c6writer.writerow(rec) 
    f6666.close()
    f7777.close()
    f8888=open('customer3.csv','r')
    f9999=open('customer1.csv','w',newline='') 
    c9reader=csv.reader(f8888)
    c9writer=csv.writer(f9999)
    for rec in c9reader:
        c9writer.writerow(rec)
    f8888.close()
    f9999.close()
    f101010=open('customer.csv','w',newline='')
    f111111=open('customer1.csv','r',newline='\r\n')
    c10reader=csv.reader(f111111)
    c10writer=csv.writer(f101010)
    for rec in c10reader:
        c10writer.writerow(rec)
    f101010.close()
    f111111.close()
    Q5=Label(crec6,text='Response updated',font=('Airial',18),fg='white',bg='grey15').pack()
def Status():
    f1111=open('customer1.csv','r')
    f1222=open('customer2.csv','w',newline='')
    c2reader=csv.reader(f1111)
    c2writer=csv.writer(f1222)
    crec2=Toplevel()
    crec2.configure(bg='grey15')
    u2=user121.get()
    p2=passwd121.get()
    s2=Status11.get()
    for rec in c2reader:
        if rec[1]==u2 and rec[2]==p2:
            l=[rec[0],rec[1],rec[2],rec[3],s2,rec[5],rec[6]]
            c2writer.writerow(l)
        else:
            c2writer.writerow(rec) 
    f1111.close()
    f1222.close()
    f11111=open('customer2.csv','r')
    f12222=open('customer1.csv','w',newline='') 
    c3reader=csv.reader(f11111)
    c3writer=csv.writer(f12222)
    for rec in c3reader:
        c3writer.writerow(rec)
    f11111.close()
    f12222.close()
    f13333=open('customer.csv','w',newline='')
    f14444=open('customer1.csv','r',newline='\r\n')
    c4reader=csv.reader(f14444)
    c4writer=csv.writer(f13333)
    for rec in c4reader:
        c4writer.writerow(rec)
    f13333.close()
    f14444.close()
    Q5=Label(crec2,text='Status updated',font=('Airial',18),fg='white',bg='grey15').pack()
def Update():
    global user121
    global passwd121
    global Status11
    global Response11
    cusc=Toplevel()
    cusc.configure(bg='grey15')
    userl=Label(cusc,text='Enter customer username:',font=('Airial',18),fg='white',bg='grey15').grid(row=0,column=0)
    user121=Entry(cusc,width=50,font=('Airial',18))
    user121.grid(row=0,column=1)
    passwdl=Label(cusc,text='Enter customer password:',font=('Airial',18),fg='white',bg='grey15').grid(row=1,column=0)
    passwd121=Entry(cusc,width=50,font=('Airial',18))
    passwd121.grid(row=1,column=1)
    Status_button=Button(cusc,text='Status update',padx=80,pady=1,command=Status,font=('Airel',18),fg='white',bg='orangered2')
    Status_button.grid(row=2,column=2)
    Statusl=Label(cusc,text='Enter status:',font=('Airial',18),fg='white',bg='grey15').grid(row=2,column=0)
    Status11=Entry(cusc,width=50,font=('Airial',18))
    Status11.grid(row=2,column=1)
    Response1=Label(cusc,text='Enter Response:',font=('Airial',18),fg='white',bg='grey15').grid(row=3,column=0)
    Response11=Entry(cusc,width=50,font=('Airial',18))
    Response11.grid(row=3,column=1)
    Response_button=Button(cusc,text='Response',padx=100,pady=1,command=Response,font=('Airel',18),fg='white',bg='orangered2')
    Response_button.grid(row=3,column=2)
def Adminscreen():
    fc.close()
    crecd=Toplevel() 
    crecd.configure(bg='grey15')
    f33=open('customer.csv','r',newline='\r\n')
    creader=csv.reader(f33)
    r=line1.get()
    if r=='123':
        heading1=Label(crecd,text='ID',font=('Airial',20),bg='grey15',fg='orangered2').grid(row=0,column=0)
        heading2=Label(crecd,text='USERNAME',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=1)
        heading3=Label(crecd,text='PASSWORD',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=2)
        heading4=Label(crecd,text='MOBILE NUMBER',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=3)
        heading5=Label(crecd,text='STATUS',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=4)
        heading6=Label(crecd,text='FEEDBACK',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=5)
        heading7=Label(crecd,text='RESPONSE',font=('Airial',20),fg='orangered2',bg='grey15').grid(row=0,column=6)
        counts=0
        for rec1 in creader:
            counts=counts+1
            heading11=Label(crecd,text=rec1[0],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=0)
            heading22=Label(crecd,text=rec1[1],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=1)
            heading33=Label(crecd,text=rec1[2],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=2)
            heading44=Label(crecd,text=rec1[3],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=3)
            heading55=Label(crecd,text=rec1[4],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=4)
            heading66=Label(crecd,text=rec1[5],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=5)
            heading77=Label(crecd,text=rec1[6],font=('Airial',18),bg='grey15',fg='white').grid(row=counts,column=6)
        Update_button=Button(crecd,text='Update record',padx=100,command=Update,font=('Airial',18),bg='orangered2',fg='white')
        counts=counts+1
        Update_button.grid(row=counts,column=3)
        f33.close()
    else:
        heading29=Label(crecd,text='INCORRECT CODE',font=('Airial',18)).grid(row=0,column=0)
        f33.close()
def Cfinal():
    f11=open('customer.csv','r',newline='\r\n')
    f12=open('customer1.csv','w',newline='')
    creader=csv.reader(f11)
    cwriter=csv.writer(f12)
    crec1=Toplevel()
    crec1.configure(bg='grey15')
    q=q2.get()
    u1=user1.get()
    p1=passwd1.get()
    for rec in creader:
        if rec[1]==u1 and rec[2]==p1:
            l=[rec[0],rec[1],rec[2],rec[3],rec[4],q,rec[6]]
            cwriter.writerow(l) 
        else:
            cwriter.writerow(rec)
    f11.close()
    f12.close()
    f111=open('customer.csv','w+',newline='')
    f122=open('customer1.csv','r+',newline='\r\n')
    c1reader=csv.reader(f122)
    c1writer=csv.writer(f111)
    for row in c1reader:
        c1writer.writerow(row)
    f111.close()
    f122.close()
    Q3=Label(crec1,text='Feedback submitted',font=('Airial',18),bg='grey15',fg='white').pack()
def Create(): 
    f100=open('customer1.csv','a',newline='')
    c100writer=csv.writer(f100)
    Customercomplete=Toplevel()
    Customercomplete.configure(bg='grey15')
    u=user.get()
    p=passwd.get()
    m=Mno.get()
    l=[id,u,p,m,'NA','NA','NA'] 
    cwriter.writerow(l)
    c100writer.writerow(l)
    qr=Label(Customercomplete,text='Login created',font=('Airial',25),bg='grey15',fg='white').pack()
    f100.close()
def Ccreate():
    global user
    global passwd
    global Mno
    global id
    cuscreate=Toplevel()
    cuscreate.configure(bg='grey15')
    userl=Label(cuscreate,text='Enter username:',font=('Airial',18),bg='grey15',fg='white').grid(row=0,column=0)
    user=Entry(cuscreate,width=50,font=('Airial',18))
    user.grid(row=0,column=1)
    passwdl=Label(cuscreate,text='Enter password:',font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=0)
    passwd=Entry(cuscreate,width=50,font=('Airial',18))
    passwd.grid(row=1,column=1)
    Mno1=Label(cuscreate,text='Enter mobile number:',font=('Airial',18),bg='grey15',fg='white').grid(row=2,column=0)
    Mno=Entry(cuscreate,width=50,font=('Airial',18))
    Mno.grid(row=2,column=1)
    Create_button=Button(cuscreate,text='Create login',font=('Airial',12),padx=100,command=Create,bg='orangered2',fg='white')
    Create_button.grid(row=3,column=1) 
    id=random.randint(0,1000) 
def Crecord(): 
    global q2
    fc.close()
    f1=open('customer.csv','r+',newline='\r\n')
    creader=csv.reader(f1)
    crec=Toplevel()
    crec.configure(bg='grey15')
    u1=user1.get()
    p1=passwd1.get()
    condition=0
    for rec in creader:
        if rec[1]==u1 and rec[2]==p1:
            heading1=Label(crec,text='ID',font=('Airial',18,'bold'),bg='grey15',fg='orangered2').grid(row=0,column=0)
            heading2=Label(crec,text='USERNAME',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=1)
            heading3=Label(crec,text='PASSWORD',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=2)
            heading4=Label(crec,text='MOBILE NUMBER',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=3)
            heading5=Label(crec,text='STATUS',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=4)
            heading6=Label(crec,text='FEEDBACK',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=5)
            heading7=Label(crec,text='RESPONSE',font=('Airial',18),bg='grey15',fg='orangered2').grid(row=0,column=6)
            heading11=Label(crec,text=rec[0],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=0)
            heading22=Label(crec,text=rec[1],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=1)
            heading33=Label(crec,text=rec[2],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=2)
            heading44=Label(crec,text=rec[3],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=3)
            heading55=Label(crec,text=rec[4],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=4)
            heading66=Label(crec,text=rec[5],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=5)
            heading77=Label(crec,text=rec[6],font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=6) 
            condition=1
        else:
            pass
    if condition==1:
        pass
    else:
        heading88=Label(crec,text='No matching record',font=('Airial',26,'bold'),bg='grey15',fg='red2').grid(row=0,column=1)
    f1.close() 
    Q1=Label(crec,text='Enter feedback',font=('Airial',18),bg='grey15',fg='white').grid(row=2,column=0)
    q2=Entry(crec,width=50,font=('Airial',18))
    q2.grid(row=2,column=1)
    Cfinal_button=Button(crec,text='Submit feedback',command=Cfinal,padx=150,pady=10,font=('Times',16),bg='orangered2',fg='white')
    Cfinal_button.grid(row=3,column=1)
def AdminLogin():
    global line1
    admlog=Toplevel()
    admlog.configure(bg='grey15')
    userl1=Label(admlog,text='Enter Admin code:',font=('Airial',18),bg='grey15',fg='white').grid(row=0,column=0)
    line1=Entry(admlog,width=50,font=('Airial',18))
    line1.grid(row=0,column=1)
    Acreate_button=Button(admlog,text='Login',command=Adminscreen,bg='orangered2',fg='white',font=('Airial',12),padx=100)
    Acreate_button.grid(row=1,column=1)
def CustomerLogin():
    global user1
    global passwd1
    cuslog=Toplevel()
    cuslog.configure(bg='grey15')
    userl1=Label(cuslog,text='Enter username:',font=('Airial',18),bg='grey15',fg='white').grid(row=0,column=0)
    user1=Entry(cuslog,width=50,font=('Airial',18))
    user1.grid(row=0,column=1)
    passwdl2=Label(cuslog,text='Enter password:',font=('Airial',18),bg='grey15',fg='white').grid(row=1,column=0)
    passwd1=Entry(cuslog,width=50,font=('Airial',18))
    passwd1.grid(row=1,column=1)
    CRecord_button=Button(cuslog,text='Next',command=Crecord,padx=100,bg='orangered2',fg='white',font=('Times',12))
    Ccreate_button=Button(cuslog,text='Create login',command=Ccreate,font=('Airial',12),padx=100,bg='orangered2',fg='white')
    Ccreate_button.grid(row=3,column=0)
    CRecord_button.grid(row=3,column=1)
admin_button=Button(root,text='Admin Login',font=('Times',20),padx=150,pady=50,command=AdminLogin,fg='white',bg='grey15')
customer_button=Button(root,text='Customer Login',font=('Times',20),padx=150,pady=50,command=CustomerLogin,fg='white',bg='grey15')
admin_button.grid(row=1,column=0)
customer_button.grid(row=1,column=1)
root.mainloop()
fc.close()
fa.close()
