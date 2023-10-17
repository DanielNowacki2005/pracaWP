import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
url = "https://www.ceneo.pl/Monitory;discount;0113-1.htm"
class Application():
    def __init__(self,url,window):
        self.url = url
        self.queryFull = ""
        self.amount = 25
            #Connect to targeted website and downoald from api
    def getData(self):
        request = requests.get(self.url,allow_redirects= True)
        self.queryFull = BeautifulSoup(request.text,"html.parser")
        
        
        #Sorts data
    #deletets everything outside important data
    def  findAll(self):
        self.price = self.queryFull.find_all('span',class_="value",string=True)
        self.name = self.queryFull.find_all('strong',class_="cat-prod-row__name")
        self.resolution = self.queryFull.find_all('strong',class_="",string=True)
        self.productScore = self.queryFull.find_all('span', class_="product-score")
        print(self.productScore)
        #Removes <span> and other from data
        j=0 
        for i in self.price:
            self.price[j] = i.text + "zł"
            j+=1
        j=0
        for k  in self.resolution:
            self.resolution[j] = k.text
            j+=1
        j=0
        for l  in self.productScore:
            self.productScore[j] = l.text
            j+=1
        j=0
        for n  in self.name:
            self.name[j] = n.text
            j+=1
    
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

window = tk.Tk() 
test = Application(url,window)
window.geometry("1800x900")
test.getData()
test.findAll()
test.displayData()
window.mainloop()
