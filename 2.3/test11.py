
from tkinter import *

window =Tk()
window.title('hello world')
window.geometry('500x500')
window.bg = 'Red'
#window.resizable(width=False, height=True) #宽不可变, 高可变,默认为True

#---------------------------label
# var = StringVar()
# lbl = Label(window,text = 'hello' ,textvariable = var, bg = 'green',width =15,height =5)
# lbl.pack(side=TOP)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

#----------------------------button
# def printfun():
#     var.set('hellp label')
# btn_label = Button(window,text='test',width =20 ,height =10 ,
#                command = printfun)
# btn_label.pack(side = RIGHT)
#-----------------------------

#---------------------------entry,text,button
# v = StringVar
#
# entry = Entry(window,show = None)
# entry.pack()
#
#
# text = Text(window,height =6,width =20,bg ='black' ,fg = 'white')
# text.pack()
#
# def insert():  #顺序插入
#     v = entry.get()
#     text.insert(INSERT,v)
#
# def insert_custom():  #插入2行2列
#     v= entry.get()
#     text.insert(2.2,v)
#
# btn_insert =Button(window,text ='insert',width =20,height =10,
#                   command = insert)
# btn_insert_custom =Button(window,text ='insert custom',width =20,height =10,
#                   command = insert_custom)
#
# btn_insert.pack()
# btn_insert_custom.pack()


#-------------------------list
# var_list =StringVar
#
#
# def insert_list():
#     l = ['python','delph','c','ruby','javascript','web','photoshop']
#     for i in l:
#         list1.insert(END,i)
#
# list1 = Listbox(window,height = 10 ,width = 40 ,listvariable = var_list)
# list1.pack()
#
#
# btn_list = Button(window,text ='insert LIST',width =20,height =10,
#                   command = insert_list)
# btn_list.pack()
#-------------------------frame

frm1 = Frame(window,bg = 'red',width =400,height =100)
frm1.pack()

frm2 = Frame(window,bg = 'blue',width =400,height =100)
frm2.pack()

frm3 = Frame(window,bg = 'yellow',width =400,height =100)
frm3.pack()

lbl1 =Text(frm1,bg = 'black' ,width=50,height =5,fg = 'yellow')
lbl1.pack(side = LEFT)

def insert_list():

    lbl1.insert(3.5,'abcde')


btn_list = Button(window,text ='insert LIST',width =20,height =10,
                  command = insert_list)
btn_list.pack()





window.focus_set()
window.mainloop()