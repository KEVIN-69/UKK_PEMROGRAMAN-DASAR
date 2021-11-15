from tkinter import *

#Window
root = Tk()
root.title("Kalkulator Sederhana")
root.geometry("312x324")
root.resizable(0, 0)

#Fungsi Clear
def clear_btn():
    global expression
    expression = ""
    input_text.set("")

#Fungsi Input
def click_btn(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Fungsi Samadengan
def samadengan_btn():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression =result
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):#ErrorHandling
        input_text.set("Error, BRO!")
    
expression = ""

#Data Input
input_text = StringVar()

#Frame input
input_frame = Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=TOP)

#Frame input field
input_field = Entry(input_frame, font=("Times New Roman", 18, "bold"),
                textvariable=input_text, width=50, bg="#fff", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#Frame button
btn_frame = Frame(root, width=312, height=272)
btn_frame.pack()

#Row ke satu
clear = Button(btn_frame, text="C", fg= "black", width= 21, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: clear_btn()
        ).grid(row=0, column=0,columnspan=2, padx=1, pady=1)

sisabagi = Button(btn_frame, text="%", fg= "black", width= 10, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: click_btn("%")
        ).grid(row=0, column=2, padx=1, pady=1)

bagi = Button(btn_frame, text="/", fg= "black", width= 10, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: click_btn("/")
        ).grid(row=0, column=3, padx=1, pady=1)


#Row ke dua
tujuh = Button(btn_frame,  text="7", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("7")
        ).grid(row=1, column=0, padx=1, pady=1)

delapan = Button(btn_frame,  text="8", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("8")
        ).grid(row=1, column=1, padx=1, pady=1)

sembilan = Button(btn_frame,  text="9", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("9")
        ).grid(row=1, column=2, padx=1, pady=1)

kali = Button(btn_frame,  text="*", fg= "black", width= 10, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: click_btn("*")
        ).grid(row=1, column=3, padx=1, pady=1)

#Row ke tiga
empat = Button(btn_frame,  text="4", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("4")
        ).grid(row=2, column=0, padx=1, pady=1)

lima = Button(btn_frame,  text="5", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("5")
        ).grid(row=2, column=1, padx=1, pady=1)

enam = Button(btn_frame,  text="6", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("6")
        ).grid(row=2, column=2, padx=1, pady=1)

kurang = Button(btn_frame,  text="-", fg= "black", width= 10, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: click_btn("-")
        ).grid(row=2, column=3, padx=1, pady=1)

#Row ke empat
satu = Button(btn_frame,  text="1", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("1")
        ).grid(row=3, column=0, padx=1, pady=1)

dua = Button(btn_frame,  text="2", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("2")
        ).grid(row=3, column=1, padx=1, pady=1)

tiga = Button(btn_frame,  text="3", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("3")
        ).grid(row=3, column=2, padx=1, pady=1)

tambah = Button(btn_frame,  text="+", fg= "black", width= 10, height=3, bd=0,
        bg="ghostwhite", cursor="hand2", command= lambda: click_btn("+")
        ).grid(row=3, column=3, padx=1, pady=1)

#Row ke lima
nol = Button(btn_frame,  text="0", fg= "black", width= 21, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn("0")
        ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

koma = Button(btn_frame,  text=".", fg= "black", width= 10, height=3, bd=0,
        bg="#fff", cursor="hand2", command= lambda: click_btn(".")
        ).grid(row=4, column=2, padx=1, pady=1)

samadengan = Button(btn_frame,  text="=", fg= "white", width= 10, height=3, bd=0,
        bg="dodgerblue", cursor="hand2", command= lambda: samadengan_btn()
        ).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()