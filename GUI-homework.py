from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('Programme for study')
GUI.geometry('1200x600')

L1 = ttk.Label(GUI,text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack()

E1 = ttk.Entry(GUI,font=('Angsana New',20),width=50)
E1.pack()

L2 = ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',18))
L2.pack()

E2 = ttk.Entry(GUI,font=('Angsana New',20),width=50)
E2.pack()

T1 = Text(GUI,font=('Angsana New',18),height=8,width=56)
T1.pack()

B1 = ttk.Button(GUI,text='บันทึก')
B1.pack(ipadx=20,ipady=10)

E3 = Entry(GUI,font=('Angsana New',30),width=20)
E3.pack()

L3 = Label(GUI,text='the end',font=('Angsana New',18,'bold'))
L3.pack() 

GUI.mainloop()

