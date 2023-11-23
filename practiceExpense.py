from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

def writecsv(data):
    with open ('ex.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

def SaveData(event=None):
    expense = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [expense,amount,timestamp]
    writecsv(data)
    E1.focus()

def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')

def readcsv():
    with open('ex.csv',newline='',encoding='utf-8') as file:
        fr = list(csv.reader(file))
    return fr

data = readcsv()

GUI = Tk()
GUI.title('Programme for expense')
GUI.geometry('600x600')

FONT1 = ('Angsana New',25)
#####################################################################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_tab1 = PhotoImage(file = '1.png')
icon_tab2 = PhotoImage(file = '2.png')

Tab.add(T1,text='บันทึกค่าใช้จ่าย',image=icon_tab1,compound='left')
Tab.add(T2,text='ประวัติค่าใช้จ่าย',image=icon_tab2,compound='left')
###################################################################
icon = 'C:\\Users\\ouyna\\Desktop\\python for everyone\\dr house icon size72.png'
iconimage = PhotoImage(file=icon)
L = Label(T1,image=iconimage)
L.pack(pady=50)

L = Label(T1,text='รายการค่าใช้จ่าย',font=(None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(T1,textvariable=v_expense,font=FONT1)
E1.pack(pady=5)

L = Label(T1,text='จำนวนเงิน(บาท)',font=(None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(T1,textvariable=v_amount,font=FONT1)
E2.pack(pady=5)

B1 = ttk.Button(T1,text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)
###################################################################
header = ['ลำดับ','รายการ','ค่าใช้จ่าย','วัน-เวลา']
hwidth = [50,200,70,80]

table = ttk.Treeview(T2,columns=header , show='headings',height=20)
table.pack()

style = ttk.Style()
style.configure('Treeview.Heading',font=(None,10))
style.configure('Treeview',font=(None,10),rowheight=30)

for h,w in zip(header,hwidth):
    table.column(h,width=w)
    table.heading(h,text=h)

table.insert('','end',values=['A','B','C','D'])

for i,d in enumerate(data,start=1):
    table.insert('','end',values=[i,d[0],d[1],d[2]])

E2.bind('<Return>',SaveData)
E1.bind('<Return>',lambda x:E2.focus())

GUI.bind('<F1>',Fav1)



GUI.mainloop()