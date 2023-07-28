from tkinter import *
from tkinter import messagebox,ttk
import math
import mysql.connector as mysql

def on_closing():
    global save_flag
    if  len(CompName)>0 and save_flag==False:
        ans = messagebox.askyesnocancel("Dividend Compare Tool","Do you want to save?")
        if ans:
            save()
            win.destroy()
        elif ans==False:
            win.destroy()
        
    else:
        win.destroy()

def click_enter(e):
    wf = win.focus_get()
    if str(wf)==".!frame.!entry2":
        add_dividend()
    elif str(wf)==".!entry3" or str(wf)==".!entry" or str(wf)==".!entry2" or str(wf)==".!frame.!entry":
        click_add()
    elif str(wf)==".!frame3.!entry" or str(wf)==".!frame3.!entry2":
        calc()
    elif str(wf)==".!frame2.!frame.!entry":
        on_click("=")
    else:
        print(wf)

def changestate():
    global win_max
    if win_max:
        win.geometry("879x540+400+120")
        maximise['text']="Maximise"
        win_max=False
    else:
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        win.geometry(f"{w}x{h}+0+0")
        maximise['text']="Minimise"
        win_max=True

def mouse_enter(e):
    maximise['bg']="#ffd14d"
    maximise['fg']="#000000"
    maximise['relief']=RAISED
def mouse_leave(e):
    maximise['bg']="#c00000"    
    maximise['fg']="#ffffff"
    maximise['relief']=RIDGE

def click_clear():
    companyName.set("")
    currentPrice.set("")
    dividend.set("")
    qShares.set("")
    companyinput.focus()

def text_enable():
    text['state']="normal"
    text0['state']="normal"
    text1['state']="normal"
    text2['state']="normal"
    text3['state']="normal"
    text4['state']="normal"
    text5['state']="normal"
    text6['state']="normal"
    text7['state']="normal"

def text_disable():
    text['state']="disabled"
    text0['state']="disabled"
    text1['state']="disabled"
    text2['state']="disabled"
    text3['state']="disabled"
    text4['state']="disabled"
    text5['state']="disabled"
    text6['state']="disabled"
    text7['state']="disabled"


def reset():
    global i
    global flag
    click_clear()
    calcClear()
    text_enable()
    text.delete('1.0',END)
    text0.delete('1.0',END)
    text1.delete('1.0',END)
    text2.delete('1.0',END)
    text3.delete('1.0',END)
    text4.delete('1.0',END)
    text5.delete('1.0',END)
    text6.delete('1.0',END)
    text7.delete('1.0',END)
    text_disable()
    CompName.clear()
    CurPrice.clear()
    Dividend.clear()
    QShares.clear()
    Investment.clear()
    Total_div.clear()
    percent_dict.clear()
    companyinput.focus()
    i=0
    flag=True
    
def validate(e):
    val = currentpriceinput.get()
    val1 = dividendinput.get()
    val1_1 = dividendinput1.get()
    val2 = qSharesinput.get()
    val3 = priceinput.get()
    val4 = sharesinput.get()
    
    if isFloat(val):
        pass
    else:
        txt = currentpriceinput.get()[:-1]
        currentpriceinput.delete(0,END)
        currentpriceinput.insert(0,txt)
        
    if isFloat(val1):
        pass
    else:
        txt1 = dividendinput.get()[:-1]
        dividendinput.delete(0,END)
        dividendinput.insert(0,txt1)
        
    if isFloat(val1_1):
        pass
    else:
        txt1_1 = dividendinput1.get()[:-1]
        dividendinput1.delete(0,END)
        dividendinput1.insert(0,txt1_1)
        
    if isFloat(val2):
        pass
    else:
        txt2 = qSharesinput.get()[:-1]
        qSharesinput.delete(0,END)
        qSharesinput.insert(0,txt2)
        
    if isFloat(val3):
        pass
    else:
        txt3 = priceinput.get()[:-1]
        priceinput.delete(0,END)
        priceinput.insert(0,txt3)
        
    if isFloat(val4):
        pass
    else:
        txt4 = sharesinput.get()[:-1]
        sharesinput.delete(0,END)
        sharesinput.insert(0,txt4)

def add_dividend():
    if dividend1.get()!="":
        if dividend.get()=="":
            div1 = float(0)
        else:
            div1 = float(dividend.get())
        div2 = float(dividend1.get())
        dividend.set(str(math.ceil(div1+div2)))
        dividend1.set("")
    

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def click_avg(e):
    if currentPrice.get() != "":
        price.set(currentPrice.get())
        sharesinput.focus()

def click_shares(e):
    if shares.get() != "":
        qShares.set(shares.get())
        calcClear()
        qSharesinput.focus()

def calc():
    Share = shares.get()
    Price = price.get()
    if Price!="" or Share!="":
        if Price=="":
            Price=1
            price.set("1")
        if Share=="":
            Share=1
            shares.set("1")
        res = math.ceil(float(Share)*float(Price))
        resultlbl['text']="Total Price: "+str(res)

def calcClear():
    shares.set("")
    price.set("")
    resultlbl['text']=""
    priceinput.focus()
    
def click_add():
    global save_flag
    name = companyName.get()
    price = currentPrice.get()
    div = dividend.get()
    share = qShares.get()
    
    if name=="" or price=="" or div=="" or share=="":
       messagebox.showerror("Error","All fields are required!")
    else:
        investment_req = math.ceil(float(price)*float(share))
        total_dividend = math.ceil(float(share)*float(div))
    
        CompName.append(name)
        CurPrice.append(price)
        Dividend.append(div)
        QShares.append(share)
        Investment.append(str(investment_req))
        Total_div.append(str(total_dividend))
        companyName.set("")
        currentPrice.set("")
        dividend.set("")
        qShares.set("")
        setInTable()
        save_flag=False
    if name=="":
        companyinput.focus()
    elif price=="":
        currentpriceinput.focus()
    elif div=="":
        dividendinput.focus()
    elif share=="":
        qSharesinput.focus()
    
    
    

def setInTable():
    global i
    text_enable()
    if i==0:
        text0.insert(END,str(i+1)+"."+"\n")
        text1.insert(END,CompName[i].capitalize()+"\n")
        text2.insert(END,CurPrice[i]+"\n")
        text3.insert(END,Dividend[i]+"\n")
        text4.insert(END,QShares[i]+"\n")
        text5.insert(END,Investment[i]+"\n")
        text6.insert(END,Total_div[i]+"\n")
        
    else:
        text0.insert(END,"\n"+str(i+1)+"."+"\n")
        text1.insert(END,"\n"+CompName[i].capitalize()+"\n")
        text2.insert(END,"\n"+CurPrice[i]+"\n")
        text3.insert(END,"\n"+Dividend[i]+"\n")
        text4.insert(END,"\n"+QShares[i]+"\n")
        text5.insert(END,"\n"+Investment[i]+"\n")
        text6.insert(END,"\n"+Total_div[i]+"\n")
        
    for j in range(0,20):
            text1.insert(END,"_")
            if j<3:
                text0.insert(END,"_")
            if j<10:
                text2.insert(END,"_")
                text3.insert(END,"_")
                text4.insert(END,"_")
            if j<13:
                text6.insert(END,"_")
            if j<16:
                text5.insert(END,"_")
    text_disable()
    i = i+1
        
def compare():
    text_enable()
    text.delete("1.0","end-1c")
    text7.delete("1.0","end-1c")
    for k in range(0,len(Investment)):
        percent = math.ceil((float(Total_div[k])*100)/float(Investment[k]))
        percent_dict[k]=percent
        if k==0:
            text7.insert(END,str(percent)+"%\n")
        else:
            text7.insert(END,"\n"+str(percent)+"%\n")
        for j in range(0,7):
            text7.insert(END,"_")

    sorted_comp = sorted(percent_dict.items(),key=lambda item: item[1],reverse=True)
    sorted_dict = {k:v for k, v in sorted_comp}
    key_list = list(sorted_dict.keys())
    num = 0
    for key in key_list:
        num = num+1
        text.insert(END,str(num)+". "+CompName[key].capitalize()+" - "+str(percent_dict.get(key))+"%\n")
    text_disable( )

def save():
    global save_flag
    if len(CompName)>0 and save_flag==False:
        con = mysql.connect(host="localhost", user = "root",password="root123",database="dividend",port="3307")
        cur = con.cursor()
        cur.execute("delete from dividend")
        cur.execute("commit")
        for n in range(0,len(CompName)):
            cur.execute("insert into dividend values('"+CompName[n]+"','"+CurPrice[n]+"','"+Dividend[n]+"','"+QShares[n]+"')")
            cur.execute("commit")
        messagebox.showinfo("Success","Saved successfully")
        con.close()
        save_flag=True

def open():
    global flag
    global save_flag
    if flag:
        con = mysql.connect(host="localhost", user = "root",password="root123",database="dividend",port="3307")
        cur = con.cursor()
        cur.execute("select * from dividend")
        all_data = cur.fetchall()
        for tup in range(0,len(all_data)):
            companyName.set(all_data[tup][0])
            currentPrice.set(all_data[tup][1])
            dividend.set(all_data[tup][2])
            qShares.set(all_data[tup][3])
            click_add()
        con.close()
        flag = False
        save_flag=True
    
    

win = Tk()
win.title("Dividend Compare Tool")
win.geometry("879x540+400+120")
win.resizable(width=False,height=False)
win.config(bg="#dfcfbe")
Grid.rowconfigure(win,0,weight=0)
Grid.rowconfigure(win,1,weight=0)
Grid.rowconfigure(win,2,weight=0)
Grid.rowconfigure(win,3,weight=0)
Grid.rowconfigure(win,4,weight=0)
Grid.rowconfigure(win,5,weight=0)
Grid.rowconfigure(win,6,weight=0)
Grid.rowconfigure(win,7,weight=0)
Grid.rowconfigure(win,8,weight=0)
Grid.rowconfigure(win,9,weight=0)
Grid.rowconfigure(win,10,weight=0)
Grid.columnconfigure(win,1,weight=1)
Grid.columnconfigure(win,2,weight=1)
Grid.columnconfigure(win,3,weight=0)
Grid.columnconfigure(win,4,weight=0)
Grid.columnconfigure(win,5,weight=0)
Grid.columnconfigure(win,6,weight=0)
Grid.columnconfigure(win,7,weight=0)

win_max=False
flag=True
i=0
save_flag = False
companyName = StringVar()
currentPrice = StringVar()
dividend = StringVar()
dividend1 = StringVar()
shares = StringVar()
qShares = StringVar()
price = StringVar()

CompName = []
CurPrice = []
Dividend = []
QShares =  []
Investment = []
Total_div = []
percent_dict = {}

title = Label(win,text="Dividend Compare Tool",bg="#c00000",fg="#ffffff",height=1,width=70,font=("arial",15,"bold"))
title.grid(row=0,column=1,pady=0,columnspan=7,sticky="EW")
maximise = Button(win,text="Maximise",bg="#c00000",fg="#f0f0f0",font=("arial",8,"normal"),width=10,height=1,relief=RIDGE,command=changestate)
maximise.grid(row=0,column=6,padx=10,sticky="E")
maximise.bind("<Enter>",mouse_enter)
maximise.bind("<Leave>",mouse_leave)


bgcolor1 = Label(win,text="",bg="#ff6f61",fg="#ffffff",height=1,width=70,font=("arial",15,"bold"))
bgcolor1.grid(row=1,column=1,pady=5,columnspan=5,sticky="EW")
bgcolor2 = Label(win,text="",bg="#ff6f61",fg="#ffffff",height=1,width=70,font=("arial",15,"bold"))
bgcolor2.grid(row=2,column=1,columnspan=5,sticky="EW")

companylbl = Label(win,text="Company Name",bg="#bfbfbf",fg="#000000",height=1,width=25,font=("arial",10,"normal"),justify="left")
companylbl.grid(row=1,column=1,pady=1,sticky="EW",padx=10)
companyinput = Entry(win,textvariable=companyName,width=25,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
companyinput.grid(row=2,column=1,sticky="EW",padx=10,pady=1)
companyinput.focus()

currentpricelbl = Label(win,text="Share Price",bg="#bfbfbf",fg="#000000",height=1,width=15,font=("arial",10,"normal"))
currentpricelbl.grid(row=1,column=2,pady=1,sticky="EW",padx=10)
currentpriceinput = Entry(win,textvariable=currentPrice,width=15,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
currentpriceinput.grid(row=2,column=2,sticky="EW",padx=10,pady=1)


dividendlbl = Label(win,text="Annual Dividend",bg="#bfbfbf",fg="#000000",height=1,width=15,font=("arial",10,"normal"))
dividendlbl.grid(row=1,column=3,pady=1,sticky="EW",padx=10)
div_frame = Frame(win,bg="#ff6f61",width=200,height=20)
div_frame.grid(row=2,column=3,sticky="EW")
dividendinput = Entry(div_frame,textvariable=dividend,width=15,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
dividendinput.grid(row=0,column=1,sticky="EW")
add_div = Button(div_frame,text="+",bg="lightgray",fg="#000000",font=("times new roman",10,"bold"),width=1,height=1,relief=GROOVE,command=add_dividend)
add_div.grid(row=0,column=2,sticky="EW")
dividendinput1 = Entry(div_frame,textvariable=dividend1,width=6,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
dividendinput1.grid(row=0,column=3,sticky="EW")

qShareslbl = Label(win,text="Shares",bg="#bfbfbf",fg="#000000",height=1,width=15,font=("arial",10,"normal"))
qShareslbl.grid(row=1,column=4,sticky="EW",padx=10,pady=1)
qSharesinput = Entry(win,textvariable=qShares,width=15,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
qSharesinput.grid(row=2,column=4,sticky="EW",padx=10,pady=1)

open_btn = Button(win,text="Open",bg="#955251",fg="#ffffff",font=("arial",10,"normal"),width=8,height=1,relief=FLAT,command=open)
open_btn.grid(row=1,column=6,sticky="EW",padx=10,pady=5)

save_btn = Button(win,text="Save",bg="maroon",fg="#ffffff",font=("arial",10,"normal"),width=8,height=1,relief=FLAT,command=save)
save_btn.grid(row=1,column=7,sticky="EW",padx=10,pady=5)

add_btn = Button(win,text="Add",bg="#2f5597",fg="#ffffff",font=("arial",10,"normal"),width=8,height=1,relief=FLAT,command=click_add)
add_btn.grid(row=2,column=6,sticky="EW",padx=10)

clear_btn = Button(win,text="Clear",bg="#2f5597",fg="#ffffff",font=("arial",10,"normal"),width=8,height=1,relief=FLAT,command=click_clear)
clear_btn.grid(row=2,column=7,sticky="EW",padx=10)

frame1 = Frame(win,bg="#bfbfbf",width=620,height=420)
frame1.grid(row=3,column=1,sticky="EW",columnspan=5,rowspan=10,pady=5,padx=10)
lbl0 = Label(frame1,text=" SNO.",bg="#1b3952",fg="#ffffff",height=1,width=3,font=("arial",9,"bold"))
lbl0.grid(row=0,column=0,sticky="E")
lbl1 = Label(frame1,text=" Company Name ",bg="#1b3952",fg="#ffffff",height=1,width=20,font=("arial",9,"bold"))
lbl1.grid(row=0,column=1,sticky="E")
lbl2 = Label(frame1,text="Share Price",bg="#1b3952",fg="#ffffff",height=1,width=10,font=("arial",9,"bold"))
lbl2.grid(row=0,column=2,sticky="E")
lbl3 = Label(frame1,text="Annual Div.",bg="#1b3952",fg="#ffffff",height=1,width=10,font=("arial",9,"bold"))
lbl3.grid(row=0,column=3,sticky="E")
lbl4 = Label(frame1,text="Shares",bg="#1b3952",fg="#ffffff",height=1,width=10,font=("arial",9,"bold"))
lbl4.grid(row=0,column=4,sticky="E")
lbl5 = Label(frame1,text="Investment",bg="#1b3952",fg="#ffffff",height=1,width=16,font=("arial",9,"bold"))
lbl5.grid(row=0,column=5,sticky="E")
lbl6 = Label(frame1,text="Total Dividend",bg="#1b3952",fg="#ffffff",height=1,width=13,font=("arial",9,"bold"))
lbl6.grid(row=0,column=6,sticky="E")
lbl7 = Label(frame1,text="Comp.",bg="#1b3952",fg="#ffffff",height=1,width=7,font=("arial",9,"bold"))
lbl7.grid(row=0,column=7,sticky="E")
text0 = Text(frame1,bg="#9cb0c0",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=3,height=26,state="disabled")
text0.grid(row=1,column=0,sticky="E")
text1 = Text(frame1,bg="#9cb0c0",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=20,height=26,state="disabled")
text1.grid(row=1,column=1,sticky="E")
text2 = Text(frame1,bg="#9cb0c0",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=10,height=26,state="disabled")
text2.grid(row=1,column=2,sticky="E")
text3 = Text(frame1,bg="#9cb0c0",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=10,height=26,state="disabled")
text3.grid(row=1,column=3,sticky="E")
text4 = Text(frame1,bg="#9cb0c0",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=10,height=26,state="disabled")
text4.grid(row=1,column=4,sticky="E")
text5 = Text(frame1,bg="#ee90bf",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=16,height=26,state="disabled")
text5.grid(row=1,column=5,sticky="E")
text6 = Text(frame1,bg="#ee9090",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=13,height=26,state="disabled")
text6.grid(row=1,column=6,sticky="E")
text7 = Text(frame1,bg="#90EE90",font=("arial",9,"bold"),relief=FLAT,cursor="arrow",width=7,height=26,state="disabled")
text7.grid(row=1,column=7,sticky="E")


# /----------------------------------Calc-----------------------------------/
def on_click(key):
    if key == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif key == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + key)

def click_addToDiv():
    if isFloat(entry_var.get()):
        dividend.set(entry_var.get())
        entry_var.set("")

frame_calc= Frame(frame1,bg="red",width=430,height=430)
frame_calc.grid(row=0,rowspan=10,column=8,sticky="E",padx=150)
entry_var = StringVar()
calc_title = Label(frame_calc,text="Calculator",bg="red",fg="#ffffff",height=1,width=30,font=("arial",15,"bold"))
calc_title.grid(row=0,column=0,columnspan=4,sticky="EW",pady=10)
entry_widget = Entry(frame_calc, textvariable=entry_var, font=("Arial", 20), justify="right")
entry_widget.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="EW")
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 6, 0), ("Add to Annual Div.",6,1)
]

for btn_text, row, col in buttons:
    if row==6 and col==1:
        btn = Button(frame_calc, text=btn_text, font=("Arial", 18), command=click_addToDiv,relief=GROOVE)
        btn.grid(row=row, column=col,columnspan=3, padx=5, pady=5, sticky="EW")
    else:
        btn = Button(frame_calc, text=btn_text, font=("Arial", 18), command=lambda key=btn_text: on_click(key),relief=GROOVE)
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="EW")

for nm in range(4):
    frame_calc.columnconfigure(nm, weight=1)
for nm in range(7):
    frame_calc.rowconfigure(nm, weight=1)
# /----------------------------------Calc-----------------------------------/


compare_btn = Button(win,text="Compare",bg="#611e67",fg="#ffffff",font=("arial",10,"bold"),width=8,height=1,relief=FLAT,command=compare)
compare_btn.grid(row=3,column=6,sticky="EW",padx=10,pady=20)

reset_btn = Button(win,text="Reset",bg="#b30000",fg="#ffffff",font=("arial",10,"bold"),width=8,height=1,relief=FLAT,command=reset)
reset_btn.grid(row=3,column=7,sticky="EW",padx=10,pady=20)

frame2 = Frame(win,bg="#ffc327",width=170,height=150)
frame2.grid(row=4,column=6,columnspan=7,sticky="NS")
calclbl = Label(frame2,text="Price Calculator",bg="#7719aa",fg="#ffffff",height=1,width=23,font=("arial",9,"bold"))
calclbl.grid(row=0,column=1,columnspan=2)
pricelbl = Label(frame2,text="Avg. Price",bg="#ffc327",fg="#000000",height=1,width=8,font=("arial",8,"italic"))
pricelbl.grid(row=1,column=1,sticky="EW",pady=5)
pricelbl.bind("<Button-1>",click_avg)
priceinput = Entry(frame2,textvariable=price,width=10,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
priceinput.grid(row=2,column=1,sticky="EW")
shareslbl = Label(frame2,text="Shares",bg="#ffc327",fg="#000000",height=1,width=5,font=("arial",8,"italic"))
shareslbl.grid(row=1,column=2,sticky="EW",pady=5)
shareslbl.bind("<Button-1>",click_shares)
sharesinput = Entry(frame2,textvariable=shares,width=10,font=("arial",10,"normal"),highlightthickness=1,highlightbackground="#000000")
sharesinput.grid(row=2,column=2,sticky="EW")
calc_btn = Button(frame2,text="Calculate",bg="#7719aa",fg="#ffffff",font=("arial",8,"bold"),width=8,height=1,relief=FLAT,command=calc)
calc_btn.grid(row=3,column=1,sticky="EW",pady=5)
calcClear_btn = Button(frame2,text="Clear",bg="#fe7e34",fg="#ffffff",font=("arial",8,"bold"),width=5,height=1,relief=FLAT,command=calcClear)
calcClear_btn.grid(row=3,column=2,sticky="EW",pady=5)
resultlbl = Label(frame2,text="",bg="#e6e6e6",fg="#000000",height=1,width=22,font=("arial",8,"bold"))
resultlbl.grid(row=4,column=1,sticky="EW",columnspan=2,pady=5)

frame3 = Frame(win,bg="#c6dff3",width=170,height=213)
frame3.grid(row=5,column=6,columnspan=7,sticky="NS",pady=20)
bestlbl = Label(frame3,text="Best Dividend Companies",bg="#417b4e",fg="#ffffff",height=1,width=23,font=("arial",9,"bold"))
bestlbl.grid(row=0,column=1,columnspan=2,sticky="EW")
text = Text(frame3,bg="#d4f8d4",font=("arial",10,"bold"),relief=FLAT,cursor="arrow",width=23,height=11,state="normal")
text.grid(row=1,column=1,columnspan=2,sticky="EW")


document = Frame(win,width=win.winfo_screenwidth()-15,height=280,bg="#dfcfbe")
document.grid(row=16,column=1,columnspan=7,sticky="S")
d_title = Label(document,text="Read this",bg="purple",fg="#ffffff",height=1,width=200,font=("arial",10,"bold"),justify=CENTER)
d_title.grid(row=0,column=1,columnspan=7,sticky="w")
pic = PhotoImage(file = "F:\\Vs_code\\python\\gui\\.img\\tutorial.png")
read ="1. 'Open' button, open the previously saved details of companies.\n2. 'Save' button, save the details of companies.\n3. 'Add' button, add the entries to the table.\n4. 'Clear' button, clear the entries from all input boxes.\n5. 'Compare' button, Compare the details of companies and output the results in the 'Comp.' column as a percentage. Additionally, analyze the best dividend-paying companies.\n6. 'Reset' button, reset all entries in the table and the input boxes.\n7. In Price Calculator, 'Avg. Price' is the same as 'Share Price'; it is used to multiply the shares with their average price. Click on 'Avg. Price' to copy the values from 'Share Price', and \n click on 'Shares' to paste the values into the 'Shares' entry above.\n\n* For any report or feedback, please contact us at 'cr3992@gmail.com' and use the subject 'Dividend Compare Tool Software'."
doc= Text(document,bg="#dfcfbe",fg="gray",height=10,width=270,font=("arial",10,"italic"),bd=0,cursor="arrow")
doc.grid(row=1,column=1,columnspan=7,sticky="W",pady=10,padx=20)
doc.insert(END,read)
doc['state']="disabled"
win.bind('<Key>',validate)
win.protocol("WM_DELETE_WINDOW",on_closing)
win.bind("<Return>",click_enter)
win.mainloop()