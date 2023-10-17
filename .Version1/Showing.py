import re
import tkinter as tk
class Showing:
    #displays data
    def displayData(self):
         
        #headers of the table
        name = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor name.")
        name.grid(row=0, column=1)

        price = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor price.")
        price.grid(row=0, column=2)

        resolution = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor ratio.")
        resolution.grid(row=0, column=3)

        productScore = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text="Monitor Score.")
        productScore.grid(row=0, column=4)

        #table body
        totalRows = len(self.name)
        for i in range(totalRows-3):
                if i == self.amount: break
                self.e = tk.Entry(window, width=50, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=1)
                self.e.insert("end",self.name[i+3])
                
        totalRows = len(self.price)
        for i in range(totalRows):
                if i == self.amount: break
                self.e = tk.Entry(window, width=10, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=2)
                self.e.insert("end",self.price[i])
                

        totalRows = len(self.resolution)
        for i in range(totalRows-1):
                if i == self.amount: break
                self.e = tk.Entry(window, width=10, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=3)
                self.e.insert("end",self.resolution[i+1])

        totalRows = len(self.productScore)
        for i in range(totalRows):
                if i == self.amount: break
                totalRows = len(self.productScore)
                self.e = tk.Entry(window, width=10, fg='black',font=('Arial',12,'bold'))
                self.e.grid(row=i+1, column=4)
                self.e.insert("end",self.productScore[i])
                #writes data
        for i in range(5):
               print(self.name[i+3]+","+self.price[i]+","+self.resolution[i+1]+","+ self.productScore[i+5])