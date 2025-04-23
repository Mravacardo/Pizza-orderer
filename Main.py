from tkinter import *
from tkinter.ttk import *

window=Tk()
window.title('pizza order')

title=Label(window, text = "Pizza orderer")
caption=Label(window, text = "Pizza and Amount:")

title.grid(row = 0, column = 0,columnspan = 3, pady=25)
caption.grid(column = 0,row = 1,padx=10)

list=["Veggie supreme", "Meat feast", "Hawian", "Triple cheese", "Spicey beef"]

thePizza = StringVar()
Pizzas=Combobox(window,textvariable = thePizza,width=10)
Pizzas['values'] = tuple(list)

Pizzas.grid(column = 1, row = 1)

endVal = StringVar()
r10=Radiobutton(window,text="small",variable=endVal,value="small")
r20=Radiobutton(window,text="medium",variable=endVal,value="medium")
r30=Radiobutton(window,text="large",variable=endVal,value="large")
endVal.set(10)

theNum = IntVar()
numbers=Combobox(window,textvariable = theNum,width=5)
numbers['values'] = tuple(range(101))

numbers.grid(column = 1, row = 2)

r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)

def generateMulTable():
    tables=""
    tables+=str("You have ordered the "+thePizza.get()+" "+endVal.get()+" "+str(theNum.get()))+"\n"
    table.configure(text=tables)

orderButton=Button(window,text="Order",command=generateMulTable)
table=Label(window,anchor="center")

orderButton.grid(row=4,column=1)
table.grid(row=5,column=1, pady = 25)

window.mainloop()
