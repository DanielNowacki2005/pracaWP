import re
import tkinter as tk
class Showing:
    def __init__(self,window,name,price,productScore):
           self.window = window
           self.name = name
           self.price = price
           self.productScore = productScore
    #displays data
    def displayData(self):
        self.amount = 25
        #headers of the table
        name = tk.Label(self.window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor name.")
        name.grid(row=0, column=1)

        price = tk.Label(self.window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor price.")
        price.grid(row=0, column=2)

        resolution = tk.Label(self.window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor ratio.")
        resolution.grid(row=0, column=3)

        productScore = tk.Label(self.window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor Score.")
        productScore.grid(row=0, column=4)

        #table body
        totalRows = len(self.name)
        for i in range(totalRows-3):
                if i == self.amount: break
                self.e = tk.Entry(self.window, width=50, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=1)
                self.e.insert("end",self.name[i+3])
                
        totalRows = len(self.price)
        for i in range(totalRows):
                if i == self.amount: break
                self.e = tk.Entry(self.window, width=10, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=2)
                self.e.insert("end",self.price[i])
                
        totalRows = len(self.productScore)
        for i in range(totalRows):
                if i == self.amount: break
                self.e = tk.Entry(self.window, width=10, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=4)
                self.e.insert("end",self.productScore[i])
